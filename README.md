# Python EVM Chains Metadata

Provides general metadata on EVM-compatible chains organized by Ape-style ecosystem and network.

Original source data: https://github.com/ethereum-lists/chains

## Quick Start

## Dependencies

- [python3](https://www.python.org/downloads) version 3.8 up to 3.12.

## Installation

### via `pip`

You can install the latest release via [`pip`](https://pypi.org/project/pip/):

```bash
pip install evmchains
```

### via `setuptools`

You can clone the repository and use [`setuptools`](https://github.com/pypa/setuptools) for the most up-to-date version:

```bash
git clone https://github.com/ApeWorX/evmchains.git
cd evmchains
python3 setup.py install
```

## Quick Usage

```
from evmchains import get_chain_meta
chain = get_chain_meta("ethereum", "mainnet")
assert chain.chainId == 1
```

## Development

Please see the [contributing guide](CONTRIBUTING.md) to learn more how to contribute to this project.
Comments, questions, criticisms and pull requests are welcomed.

### Adding Chains

To add a chain to the metadata, please open a pull request with the following changes:

- Update `CHAIN_IDS` in `scripts/update.py` with the chain IDs you want to add
- Run `python scripts/update.py`
- Submit a PR with the updated script and updated `evmchain/chains.py` metdata file

**Do not edit `evmchain/chains.py` manually.** Any manual changes are likely to be overwritten later.
