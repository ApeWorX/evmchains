from evmchains import PUBLIC_CHAIN_META, Chain, get_chain_meta


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
