import random

from evmchains.chains import PUBLIC_CHAIN_META
from evmchains.types import Chain


def get_chain_meta(ecosystem: str, network: str) -> Chain:
    """Return a Chain instance with metadata for an EVM chain"""
    if (
        ecosystem not in PUBLIC_CHAIN_META
        or network not in PUBLIC_CHAIN_META[ecosystem]
    ):
        raise KeyError(f"Unknown ecosystem:network: {ecosystem}:{network}")

    return Chain(**PUBLIC_CHAIN_META[ecosystem][network])


def get_random_rpc(ecosystem: str, network: str) -> str:
    """Return a random RPC endpoint for an ecosystem:network pair"""
    chain = get_chain_meta(ecosystem, network)
    return random.choice(chain.rpc)


__all__ = ["PUBLIC_CHAIN_META", "Chain", "get_chain_meta"]
