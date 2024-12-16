"""Script updates chains.py constants file with up to date data.

To add new chains to this module, update CHAIN_IDS below and re-run the script. See
README.md for more details.
"""

import logging
from datetime import datetime, timezone
from pathlib import Path
from pprint import PrettyPrinter
from typing import Any, Dict
from urllib.parse import urljoin

import black
import requests

from evmchains.types import Chain

INCLUDE_PROTOCOLS = ["http", "https"]
SOURCE_URL = (
    "https://raw.githubusercontent.com/ethereum-lists/chains/master/_data/chains/"
)
CHAIN_CONST_FILE = Path(__file__).parent.parent / "evmchains" / "chains.py"
BLACKLIST_STRINGS = [
    # 2024-01-19: Node appears to be broken.  Returning errors on simple requests.
    "rpc.blocknative.com",
    # 2024-09-05: Node returning 504s for days.
    "rpc-sepolia.rockx.com",
]

# Mapping of Ape ecosystem:network to chain IDs. These are the chains that we will be
# fetching.
CHAIN_IDS = {
    "abstract": {
        "mainnet": 2741,
        "testnet": 11124,
    },
    "apechain": {
        "mainnet": 33139,
        "curtis": 33111,
    },
    "arbitrum": {
        "mainnet": 42161,
        "goerli": 421613,
        "sepolia": 421614,
        "nova": 42170,
    },
    "astar": {
        "mainnet": 592,
    },
    "avalanche": {
        "mainnet": 43114,
        "fuji": 43113,
    },
    "base": {
        "mainnet": 8453,
        "sepolia": 84532,
    },
    "berachain": {
        "bartio": 80084,
    },
    "blast": {
        "mainnet": 81457,
        "sepolia": 168587773,
        "testnet": 23888,
    },
    "bsc": {
        "mainnet": 56,
        "testnet": 97,
        "opbnb": 204,
        "opbnb-testnet": 5611,
    },
    "bttc": {
        "mainnet": 199,
        "donau": 1028,
    },
    "celo": {
        "mainnet": 42220,
        "alfajores": 44787,
    },
    "cronos": {
        "mainnet": 25,
        "testnet": 338,
    },
    "cronos-zkevm": {
        "mainnet": 388,
        "testnet": 282,
    },
    "crossfi": {
        "mainnet": 4158,
        "testnet": 4157,
    },
    "ethereum": {
        "mainnet": 1,
        "goerli": 5,
        "holesky": 17000,
        "sepolia": 11155111,
    },
    "fantom": {
        "mainnet": 250,
        "testnet": 4002,
    },
    "flow-evm": {
        "mainnet": 747,
        "testnet": 545,
    },
    "fraxtal": {
        "mainnet": 252,
        "holesky": 2522,
    },
    "geist": {
        "mainnet": 63157,
        "polter": 631571,
    },
    "gnosis": {
        "chiado": 10200,
        "mainnet": 100,
    },
    "kroma": {
        "mainnet": 255,
        "sepolia": 2358,
    },
    "lens": {
        "sepolia": 37111,
    },
    "linea": {
        "mainnet": 59144,
        "sepolia": 59141,
    },
    "lumia": {
        "prism": 994873017,
        "testnet": 1952959480,
    },
    "mantle": {
        "mainnet": 5000,
        "testnet": 5001,
        "sepolia": 5003,
    },
    "metis": {
        "mainnet": 1088,
    },
    "moonbeam": {
        "mainnet": 1284,
        "moonbase": 1287,
        "moonriver": 1285,
    },
    "optimism": {
        "mainnet": 10,
        "goerli": 420,
        "sepolia": 11155420,
    },
    "oort": {
        "mainnet": 970,
        "dev": 9700,
    },
    "palm": {
        "mainnet": 11297108109,
        "testnet": 11297108099,
    },
    "polygon": {
        "mainnet": 137,
        "mumbai": 80001,
        "amoy": 80002,
    },
    "polygon-zkevm": {
        "mainnet": 1101,
        "testnet": 1442,
        "cardona": 2442,
    },
    "polynomial": {
        "mainnet": 8008,
        "sepolia": 80008,
    },
    "rootstock": {
        "mainnet": 30,
        "testnet": 31,
    },
    "shibarium": {
        "mainnet": 109,
        "puppynet": 157,
    },
    "scroll": {
        "mainnet": 534352,
        "sepolia": 534351,
    },
    "shape": {
        "mainnet": 360,
        "sepolia": 11011,
    },
    "soneium": {
        "minato": 1946,
    },
    "taiko": {
        "mainnet": 167000,
        "hekla": 167009,
    },
    "unichain": {
        "sepolia": 1301,
    },
    "wemix": {
        "mainnet": 1111,
        "testnet": 1112,
    },
    "world-chain": {
        "mainnet": 480,
        "sepolia": 4801,
    },
    "xai": {
        "mainnet": 660279,
        "sepolia": 37714555429,
    },
    "xmtp": {
        "mainnet": 24132016,
        "sepolia": 241320161,
    },
    "zetachain": {
        "mainnet": 7000,
        "testnet": 7001,
    },
    "zksync": {
        "mainnet": 324,
        "sepolia": 300,
    },
    "zora": {
        "mainnet": 7777777,
        "sepolia": 999999999,
    },
}

pp = PrettyPrinter(indent=4)
logger = logging.getLogger("update")
logger.setLevel(logging.DEBUG)


def stamp() -> str:
    """UTC timestamp for file header."""
    return str(datetime.now(tz=timezone.utc))


def ensure_dict(d: Dict[str, Any], key: str):
    """Ensures a dict value at key."""
    if key in d and isinstance(d[key], dict):
        return
    d[key] = dict()


def is_uri_blacklisted(uri: str) -> bool:
    """Check if a URI is blacklisted."""
    for blacklisted in BLACKLIST_STRINGS:
        if blacklisted in uri:
            return True
    return False


def fetch_chain(chain_id: int) -> Chain:
    """Fetch a chain from the ethereum-lists repo."""
    url = urljoin(SOURCE_URL, f"eip155-{chain_id}.json")

    logger.info(f"GET {url}")
    response = requests.get(url)
    response.raise_for_status()

    chain = Chain.model_validate_json(response.text)

    # Filter out blacklisted URIs
    chain.rpc = list(filter(lambda rpc: not is_uri_blacklisted(rpc), chain.rpc))

    # Filter out unwanted protocols (e.g. websocket)
    chain.rpc = list(
        filter(lambda rpc: rpc.split(":")[0] in INCLUDE_PROTOCOLS, chain.rpc)
    )

    return chain


def fetch_chains() -> Dict[str, Dict[str, Chain]]:
    """Fetch all chains from the ethereum-lists repo."""
    chains: Dict[str, Dict[str, Chain]] = {}
    for ecosystem in CHAIN_IDS.keys():
        for network, chain_id in CHAIN_IDS[ecosystem].items():
            logger.info(f"Fetching chain {ecosystem}:{network} ({chain_id})")
            ensure_dict(chains, ecosystem)
            chains[ecosystem][network] = fetch_chain(chain_id)
    return chains


def write_chain_const(chains: Dict[str, Dict[str, Chain]]):
    """Write the file with Python constant."""
    stamp_str = stamp()
    file_str = '"""Constants containing metadata for EVM-comaptitble chains.\n\n'
    file_str += "!!!!!!!!!!!!!!!!!!!!!!!!! WARNING !!!!!!!!!!!!!!!!!!!!!!!!!\n"
    file_str += "!!!! DO NOT EDIT THIS FILE DIRECTLY!                   !!!!\n"
    file_str += "!!!! This file is auto-generated by scripts/update.py  !!!!\n"
    file_str += f"!!!! {stamp_str}{' ' * (50 - len(stamp_str))}!!!!\n"
    file_str += "!!!!!!!!!!!!!!!!!!!!!!!!! WARNING !!!!!!!!!!!!!!!!!!!!!!!!!\n"
    file_str += '"""\n\n'
    file_str += "from typing import Any, Dict\n\n"
    file_str += "PUBLIC_CHAIN_META: Dict[str, Dict[str, Dict[str, Any]]] = {\n"

    for ecosystem in chains.keys():
        file_str += f'    "{ecosystem}": {{\n'
        for network, chain in chains[ecosystem].items():
            # pprint to make a somewhat pythonic string output
            file_str += f'        "{network}": {pp.pformat(chain.model_dump())},\n'
        file_str += "    },\n"
    file_str += "}\n"

    # black to make it actually readable
    file_str = black.format_file_contents(file_str, fast=False, mode=black.FileMode())

    with CHAIN_CONST_FILE.open("w") as const_file:
        const_file.write(file_str)


def main():
    """Fetch data and update the constants file."""
    logger.info("Fetching chain data...")
    logger.info(f"    Source: {SOURCE_URL}")
    logger.info(f"    Dest: {CHAIN_CONST_FILE}")
    chains = fetch_chains()
    write_chain_const(chains)


if __name__ == "__main__":
    main()
