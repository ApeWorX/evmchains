from evmchains.chains import PUBLIC_CHAIN_RPCS
from evmchains.types import Chain


def get_chain_meta(ecosystem: str, network: str) -> Chain:
    """Return a Chain instance with metadata for an EVM chain"""
    if (
        ecosystem not in PUBLIC_CHAIN_RPCS
        or network not in PUBLIC_CHAIN_RPCS[ecosystem]
    ):
        raise KeyError(f"Unknown ecosystem:network: {ecosystem}:{network}")

    return Chain(**PUBLIC_CHAIN_RPCS[ecosystem][network])


__all__ = ["PUBLIC_CHAIN_RPCS", "Chain", "get_chain_meta"]
