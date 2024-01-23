from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class Chain(BaseModel):
    chainId: int
    networkId: int
    name: str
    shortName: str
    chain: str
    infoURL: str
    rpc: List[str]
    faucets: List[str]
    nativeCurrency: Dict[str, Any]
    explorers: List[Dict[str, str]]
    icon: Optional[str] = None
    features: Optional[List[Dict[str, str]]] = None
    slip44: Optional[int] = None
    ens: Optional[Dict[str, str]] = None
