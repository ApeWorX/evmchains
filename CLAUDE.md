# evmchains

Python package providing EVM chain metadata, organized by Ape-style ecosystem and network.

## How updates work

`evmchains/chains.py` is **auto-generated** — do not edit it directly. It is rewritten by `scripts/update.py`, which fetches metadata from the [ethereum-lists/chains](https://github.com/ethereum-lists/chains) repo at `https://raw.githubusercontent.com/ethereum-lists/chains/master/_data/chains/eip155-<chain_id>.json`.

### Adding a new chain

1. Edit the `CHAIN_IDS` dict in `scripts/update.py` — add the ecosystem key and `network: chain_id` entries.
2. Verify each chain ID has a corresponding file at `https://raw.githubusercontent.com/ethereum-lists/chains/master/_data/chains/eip155-<id>.json` (the script will hard-fail on 404).
3. Run `python scripts/update.py` from the repo root. This re-fetches **every** chain and rewrites `evmchains/chains.py` (then runs `ruff format` on it).
4. Commit both `scripts/update.py` and the regenerated `evmchains/chains.py`.

### Other things to know

- `BLACKLIST_STRINGS` in `scripts/update.py` filters out broken RPC URLs — append entries here when nodes are persistently down.
- Only `http`/`https` RPC endpoints are kept; websockets are stripped.
- The header timestamp in `chains.py` updates on every run, so a "no-op" run will still produce a diff on that line.
