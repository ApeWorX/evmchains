import os
from contextlib import contextmanager

import pytest

from evmchains import PUBLIC_CHAIN_META, Chain, get_chain_meta, get_rpcs


@pytest.fixture()
def env():
    @contextmanager
    def inner(environ=dict(), unset=list()):
        old_environ = os.environ.copy()
        os.environ.update(environ)
        for key in unset:
            try:
                del os.environ[key]
            except KeyError:
                pass
        yield
        os.environ = old_environ

    return inner


def test_chain_structure():
    assert "ethereum" in PUBLIC_CHAIN_META
    assert "mainnet" in PUBLIC_CHAIN_META["ethereum"]

    chain = PUBLIC_CHAIN_META["ethereum"]["mainnet"]
    assert isinstance(chain, dict)
    assert len(chain["rpc"]) > 0
    assert chain["chainId"] == 1
    assert chain["networkId"] == 1
    assert chain["shortName"] == "eth"
    assert chain["name"] == "Ethereum Mainnet"
    assert chain["nativeCurrency"]["symbol"] == "ETH"
    assert len(chain["explorers"]) > 0


def test_get_chain_meta():
    chain = get_chain_meta("arbitrum", "mainnet")
    assert isinstance(chain, Chain)
    assert len(chain.rpc) > 0
    assert chain.chainId == 42161
    assert chain.networkId == 42161
    assert chain.shortName == "arb1"
    assert chain.name == "Arbitrum One"
    assert chain.nativeCurrency["symbol"] == "ETH"
    assert len(chain.explorers) > 0


def test_get_rpcs_alchemy(env):
    alchemy_key = "alchemistsayswhat"
    expected_rpc = f"https://arb-mainnet.g.alchemy.com/v2/{alchemy_key}"

    def find_rpc(rpcs, expected):
        for rpc in rpcs:
            if rpc == expected:
                return True
        return False

    with env({"ALCHEMY_API_KEY": alchemy_key}, unset=["INFURA_API_KEY"]):
        rpcs = get_rpcs("arbitrum", "mainnet")
        assert isinstance(rpcs, list)
        assert len(rpcs) > 0
        assert find_rpc(rpcs, expected_rpc)
        # Ensure the infura endpoint was also filtered out
        assert len([rpc for rpc in rpcs if "infura" in rpc]) == 0


def test_get_rpcs_infura(env):
    infura_key = "infuraaaaaa"
    expected_rpc = f"https://arbitrum-mainnet.infura.io/v3/{infura_key}"

    def find_rpc(rpcs, expected):
        for rpc in rpcs:
            if rpc == expected:
                return True
        return False

    with env({"INFURA_API_KEY": infura_key}, unset=["ALCHEMY_API_KEY"]):
        rpcs = get_rpcs("arbitrum", "mainnet")
        assert isinstance(rpcs, list)
        assert len(rpcs) > 0
        assert find_rpc(rpcs, expected_rpc)
        # Ensure the alchemy endpoint was also filtered out
        assert len([rpc for rpc in rpcs if "alchemy" in rpc]) == 0
