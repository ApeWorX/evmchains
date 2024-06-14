import os
import random
import re
from typing import List

from evmchains.chains import PUBLIC_CHAIN_META
from evmchains.types import Chain

ENV_VAR_REGEX = re.compile(r"\$\{([A-Za-z0-9_]+)\}")


def get_chain_meta(ecosystem: str, network: str) -> Chain:
    """Return a Chain instance with metadata for an EVM chain"""
    if (
        ecosystem not in PUBLIC_CHAIN_META
        or network not in PUBLIC_CHAIN_META[ecosystem]
    ):
        raise KeyError(f"Unknown ecosystem:network: {ecosystem}:{network}")

    return Chain(**PUBLIC_CHAIN_META[ecosystem][network])


def get_rpcs(ecosystem: str, network: str) -> List[str]:
    """Get a list of valid RPC endpoints for an ecosystem:network pair"""
    rpcs = []

    chain = get_chain_meta(ecosystem, network)

    for rpc in chain.rpc:
        # Look for env var replacements in the endpoint URL
        match = ENV_VAR_REGEX.search(rpc)
        if match:
            to_replace = match.group(0)
            env_var = match.group(1)
            # Include them only if the env var is available
            if env_var in os.environ:
                rpcs.append(rpc.replace(to_replace, os.environ[env_var]))
        else:
            rpcs.append(rpc)

    return rpcs


def get_random_rpc(ecosystem: str, network: str) -> str:
    """Return a random RPC endpoint for an ecosystem:network pair"""
    rpcs = get_rpcs(ecosystem, network)
    return random.choice(rpcs)


__all__ = ["PUBLIC_CHAIN_META", "Chain", "get_chain_meta", "get_random_rpc", "get_rpcs"]
