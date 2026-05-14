"""Types used in the evmchains package."""

# ruff: noqa: N815
from typing import Any

from pydantic import BaseModel


class Chain(BaseModel):
    """Chain object format for chain data from ethereum-lists/chains."""

    chainId: int
    networkId: int
    name: str
    shortName: str
    chain: str
    infoURL: str
    rpc: list[str]
    faucets: list[str]
    nativeCurrency: dict[str, Any]
    explorers: list[dict[str, str]] = []
    icon: str | None = None
    features: list[dict[str, str]] | None = None
    slip44: int | None = None
    ens: dict[str, str] | None = None
