# This file is auto-generated by scripts/update.py
# 2024-04-09 14:08:35.326760
# Do not edit this file directly.
from typing import Any, Dict

PUBLIC_CHAIN_META: Dict[str, Dict[str, Dict[str, Any]]] = {
    "arbitrum": {
        "mainnet": {
            "chain": "ETH",
            "chainId": 42161,
            "ens": None,
            "explorers": [
                {
                    "name": "Arbiscan",
                    "standard": "EIP3091",
                    "url": "https://arbiscan.io",
                },
                {
                    "name": "Arbitrum Explorer",
                    "standard": "EIP3091",
                    "url": "https://explorer.arbitrum.io",
                },
                {
                    "icon": "dexguru",
                    "name": "dexguru",
                    "standard": "EIP3091",
                    "url": "https://arbitrum.dex.guru",
                },
            ],
            "faucets": [],
            "features": None,
            "icon": None,
            "infoURL": "https://arbitrum.io",
            "name": "Arbitrum One",
            "nativeCurrency": {"decimals": 18, "name": "Ether", "symbol": "ETH"},
            "networkId": 42161,
            "rpc": [
                "https://arbitrum-mainnet.infura.io/v3/${INFURA_API_KEY}",
                "https://arb-mainnet.g.alchemy.com/v2/${ALCHEMY_API_KEY}",
                "https://arb1.arbitrum.io/rpc",
                "https://arbitrum-one.publicnode.com",
            ],
            "shortName": "arb1",
            "slip44": None,
        },
        "goerli": {
            "chain": "ETH",
            "chainId": 421613,
            "ens": None,
            "explorers": [
                {
                    "name": "Arbitrum Goerli Arbiscan",
                    "standard": "EIP3091",
                    "url": "https://goerli.arbiscan.io",
                }
            ],
            "faucets": [],
            "features": None,
            "icon": None,
            "infoURL": "https://arbitrum.io/",
            "name": "Arbitrum Goerli",
            "nativeCurrency": {
                "decimals": 18,
                "name": "Arbitrum Goerli Ether",
                "symbol": "AGOR",
            },
            "networkId": 421613,
            "rpc": [
                "https://goerli-rollup.arbitrum.io/rpc",
                "https://arbitrum-goerli.publicnode.com",
            ],
            "shortName": "arb-goerli",
            "slip44": 1,
        },
        "sepolia": {
            "chain": "ETH",
            "chainId": 421614,
            "ens": None,
            "explorers": [
                {
                    "name": "Arbitrum Sepolia Rollup Testnet Explorer",
                    "standard": "EIP3091",
                    "url": "https://sepolia-explorer.arbitrum.io",
                }
            ],
            "faucets": [],
            "features": None,
            "icon": None,
            "infoURL": "https://arbitrum.io",
            "name": "Arbitrum Sepolia",
            "nativeCurrency": {
                "decimals": 18,
                "name": "Sepolia Ether",
                "symbol": "ETH",
            },
            "networkId": 421614,
            "rpc": [
                "https://sepolia-rollup.arbitrum.io/rpc",
                "https://arbitrum-sepolia.infura.io/v3/${INFURA_API_KEY}",
            ],
            "shortName": "arb-sep",
            "slip44": 1,
        },
    },
    "avalanche": {
        "mainnet": {
            "chain": "AVAX",
            "chainId": 43114,
            "ens": None,
            "explorers": [
                {
                    "name": "snowtrace",
                    "standard": "EIP3091",
                    "url": "https://snowtrace.io",
                }
            ],
            "faucets": [],
            "features": [{"name": "EIP1559"}],
            "icon": "avax",
            "infoURL": "https://www.avax.network/",
            "name": "Avalanche C-Chain",
            "nativeCurrency": {"decimals": 18, "name": "Avalanche", "symbol": "AVAX"},
            "networkId": 43114,
            "rpc": [
                "https://api.avax.network/ext/bc/C/rpc",
                "https://avalanche-c-chain-rpc.publicnode.com",
            ],
            "shortName": "avax",
            "slip44": 9005,
        },
        "fuji": {
            "chain": "AVAX",
            "chainId": 43113,
            "ens": None,
            "explorers": [
                {
                    "name": "snowtrace",
                    "standard": "EIP3091",
                    "url": "https://testnet.snowtrace.io",
                }
            ],
            "faucets": ["https://faucet.avax-test.network/"],
            "features": None,
            "icon": "avax",
            "infoURL": "https://cchain.explorer.avax-test.network",
            "name": "Avalanche Fuji Testnet",
            "nativeCurrency": {"decimals": 18, "name": "Avalanche", "symbol": "AVAX"},
            "networkId": 1,
            "rpc": [
                "https://api.avax-test.network/ext/bc/C/rpc",
                "https://avalanche-fuji-c-chain-rpc.publicnode.com",
            ],
            "shortName": "Fuji",
            "slip44": 1,
        },
    },
    "base": {
        "mainnet": {
            "chain": "ETH",
            "chainId": 8453,
            "ens": None,
            "explorers": [
                {"name": "basescan", "standard": "none", "url": "https://basescan.org"},
                {
                    "icon": "blockscout",
                    "name": "basescout",
                    "standard": "EIP3091",
                    "url": "https://base.blockscout.com",
                },
                {
                    "icon": "dexguru",
                    "name": "dexguru",
                    "standard": "EIP3091",
                    "url": "https://base.dex.guru",
                },
            ],
            "faucets": [],
            "features": None,
            "icon": "base",
            "infoURL": "https://base.org",
            "name": "Base",
            "nativeCurrency": {"decimals": 18, "name": "Ether", "symbol": "ETH"},
            "networkId": 8453,
            "rpc": [
                "https://mainnet.base.org/",
                "https://developer-access-mainnet.base.org/",
                "https://base.gateway.tenderly.co",
                "https://base-rpc.publicnode.com",
            ],
            "shortName": "base",
            "slip44": None,
        },
        "sepolia": {
            "chain": "ETH",
            "chainId": 84532,
            "ens": None,
            "explorers": [
                {
                    "icon": "blockscout",
                    "name": "basescout",
                    "standard": "EIP3091",
                    "url": "https://base-sepolia.blockscout.com",
                }
            ],
            "faucets": [],
            "features": None,
            "icon": "baseTestnet",
            "infoURL": "https://base.org",
            "name": "Base Sepolia Testnet",
            "nativeCurrency": {
                "decimals": 18,
                "name": "Sepolia Ether",
                "symbol": "ETH",
            },
            "networkId": 84532,
            "rpc": [
                "https://sepolia.base.org",
                "https://base-sepolia-rpc.publicnode.com",
            ],
            "shortName": "basesep",
            "slip44": 1,
        },
    },
    "blast": {
        "mainnet": {
            "chain": "ETH",
            "chainId": 81457,
            "ens": None,
            "explorers": [
                {
                    "icon": "blast",
                    "name": "Blastscan",
                    "standard": "EIP3091",
                    "url": "https://blastscan.io",
                },
                {
                    "icon": "blast",
                    "name": "Blast Explorer",
                    "standard": "EIP3091",
                    "url": "https://blastexplorer.io",
                },
            ],
            "faucets": [],
            "features": None,
            "icon": "blast",
            "infoURL": "https://blast.io/",
            "name": "Blast",
            "nativeCurrency": {"decimals": 18, "name": "Ether", "symbol": "ETH"},
            "networkId": 81457,
            "rpc": [
                "https://rpc.blast.io",
                "https://rpc.ankr.com/blast",
                "https://blast.din.dev/rpc",
                "https://blastl2-mainnet.public.blastapi.io",
                "https://blast.blockpi.network/v1/rpc/public",
            ],
            "shortName": "blastmainnet",
            "slip44": None,
        },
        "sepolia": {
            "chain": "ETH",
            "chainId": 168587773,
            "ens": None,
            "explorers": [
                {
                    "icon": "blast",
                    "name": "Blast Sepolia Explorer",
                    "standard": "EIP3091",
                    "url": "https://testnet.blastscan.io",
                }
            ],
            "faucets": ["https://faucet.quicknode.com/blast/sepolia"],
            "features": None,
            "icon": "blast",
            "infoURL": "https://blast.io/",
            "name": "Blast Sepolia Testnet",
            "nativeCurrency": {
                "decimals": 18,
                "name": "Sepolia Ether",
                "symbol": "ETH",
            },
            "networkId": 168587773,
            "rpc": ["https://sepolia.blast.io", "https://blast-sepolia.drpc.org"],
            "shortName": "blastsepolia",
            "slip44": None,
        },
    },
    "bsc": {
        "mainnet": {
            "chain": "BSC",
            "chainId": 56,
            "ens": None,
            "explorers": [
                {
                    "name": "bscscan",
                    "standard": "EIP3091",
                    "url": "https://bscscan.com",
                },
                {
                    "icon": "dexguru",
                    "name": "dexguru",
                    "standard": "EIP3091",
                    "url": "https://bnb.dex.guru",
                },
            ],
            "faucets": [],
            "features": None,
            "icon": None,
            "infoURL": "https://www.bnbchain.org/en",
            "name": "BNB Smart Chain Mainnet",
            "nativeCurrency": {
                "decimals": 18,
                "name": "BNB Chain Native Token",
                "symbol": "BNB",
            },
            "networkId": 56,
            "rpc": [
                "https://bsc-dataseed1.bnbchain.org",
                "https://bsc-dataseed2.bnbchain.org",
                "https://bsc-dataseed3.bnbchain.org",
                "https://bsc-dataseed4.bnbchain.org",
                "https://bsc-dataseed1.defibit.io",
                "https://bsc-dataseed2.defibit.io",
                "https://bsc-dataseed3.defibit.io",
                "https://bsc-dataseed4.defibit.io",
                "https://bsc-dataseed1.ninicoin.io",
                "https://bsc-dataseed2.ninicoin.io",
                "https://bsc-dataseed3.ninicoin.io",
                "https://bsc-dataseed4.ninicoin.io",
                "https://bsc-rpc.publicnode.com",
            ],
            "shortName": "bnb",
            "slip44": 714,
        },
        "testnet": {
            "chain": "BSC",
            "chainId": 97,
            "ens": None,
            "explorers": [
                {
                    "name": "bscscan-testnet",
                    "standard": "EIP3091",
                    "url": "https://testnet.bscscan.com",
                }
            ],
            "faucets": ["https://testnet.bnbchain.org/faucet-smart"],
            "features": None,
            "icon": None,
            "infoURL": "https://www.bnbchain.org/en",
            "name": "BNB Smart Chain Testnet",
            "nativeCurrency": {
                "decimals": 18,
                "name": "BNB Chain Native Token",
                "symbol": "tBNB",
            },
            "networkId": 97,
            "rpc": [
                "https://data-seed-prebsc-1-s1.bnbchain.org:8545",
                "https://data-seed-prebsc-2-s1.bnbchain.org:8545",
                "https://data-seed-prebsc-1-s2.bnbchain.org:8545",
                "https://data-seed-prebsc-2-s2.bnbchain.org:8545",
                "https://data-seed-prebsc-1-s3.bnbchain.org:8545",
                "https://data-seed-prebsc-2-s3.bnbchain.org:8545",
                "https://bsc-testnet-rpc.publicnode.com",
            ],
            "shortName": "bnbt",
            "slip44": 1,
        },
    },
    "ethereum": {
        "mainnet": {
            "chain": "ETH",
            "chainId": 1,
            "ens": {"registry": "0x00000000000C2E074eC69A0dFb2997BA6C7d2e1e"},
            "explorers": [
                {
                    "name": "etherscan",
                    "standard": "EIP3091",
                    "url": "https://etherscan.io",
                },
                {
                    "icon": "blockscout",
                    "name": "blockscout",
                    "standard": "EIP3091",
                    "url": "https://eth.blockscout.com",
                },
                {
                    "icon": "dexguru",
                    "name": "dexguru",
                    "standard": "EIP3091",
                    "url": "https://ethereum.dex.guru",
                },
            ],
            "faucets": [],
            "features": [{"name": "EIP155"}, {"name": "EIP1559"}],
            "icon": "ethereum",
            "infoURL": "https://ethereum.org",
            "name": "Ethereum Mainnet",
            "nativeCurrency": {"decimals": 18, "name": "Ether", "symbol": "ETH"},
            "networkId": 1,
            "rpc": [
                "https://mainnet.infura.io/v3/${INFURA_API_KEY}",
                "https://api.mycryptoapi.com/eth",
                "https://cloudflare-eth.com",
                "https://ethereum-rpc.publicnode.com",
                "https://mainnet.gateway.tenderly.co",
                "https://rpc.flashbots.net",
                "https://rpc.flashbots.net/fast",
                "https://rpc.mevblocker.io",
                "https://rpc.mevblocker.io/fast",
                "https://rpc.mevblocker.io/noreverts",
                "https://rpc.mevblocker.io/fullprivacy",
                "https://eth.drpc.org",
            ],
            "shortName": "eth",
            "slip44": 60,
        },
        "goerli": {
            "chain": "ETH",
            "chainId": 5,
            "ens": {"registry": "0x112234455c3a32fd11230c42e7bccd4a84e02010"},
            "explorers": [
                {
                    "name": "etherscan-goerli",
                    "standard": "EIP3091",
                    "url": "https://goerli.etherscan.io",
                },
                {
                    "icon": "blockscout",
                    "name": "blockscout-goerli",
                    "standard": "EIP3091",
                    "url": "https://eth-goerli.blockscout.com",
                },
            ],
            "faucets": [
                "http://fauceth.komputing.org?chain=5&address=${ADDRESS}",
                "https://goerli-faucet.slock.it?address=${ADDRESS}",
                "https://faucet.goerli.mudit.blog",
            ],
            "features": None,
            "icon": None,
            "infoURL": "https://goerli.net/#about",
            "name": "Goerli",
            "nativeCurrency": {"decimals": 18, "name": "Goerli Ether", "symbol": "ETH"},
            "networkId": 5,
            "rpc": [
                "https://goerli.infura.io/v3/${INFURA_API_KEY}",
                "https://rpc.goerli.mudit.blog/",
                "https://ethereum-goerli-rpc.publicnode.com",
                "https://goerli.gateway.tenderly.co",
            ],
            "shortName": "gor",
            "slip44": 1,
        },
        "sepolia": {
            "chain": "ETH",
            "chainId": 11155111,
            "ens": None,
            "explorers": [
                {
                    "name": "etherscan-sepolia",
                    "standard": "EIP3091",
                    "url": "https://sepolia.etherscan.io",
                },
                {
                    "name": "otterscan-sepolia",
                    "standard": "EIP3091",
                    "url": "https://sepolia.otterscan.io",
                },
            ],
            "faucets": [
                "http://fauceth.komputing.org?chain=11155111&address=${ADDRESS}"
            ],
            "features": None,
            "icon": None,
            "infoURL": "https://sepolia.otterscan.io",
            "name": "Sepolia",
            "nativeCurrency": {
                "decimals": 18,
                "name": "Sepolia Ether",
                "symbol": "ETH",
            },
            "networkId": 11155111,
            "rpc": [
                "https://rpc.sepolia.org",
                "https://rpc2.sepolia.org",
                "https://rpc-sepolia.rockx.com",
                "https://rpc.sepolia.ethpandaops.io",
                "https://sepolia.infura.io/v3/${INFURA_API_KEY}",
                "https://sepolia.gateway.tenderly.co",
                "https://ethereum-sepolia-rpc.publicnode.com",
                "https://sepolia.drpc.org",
            ],
            "shortName": "sep",
            "slip44": 1,
        },
    },
    "fantom": {
        "mainnet": {
            "chain": "FTM",
            "chainId": 250,
            "ens": None,
            "explorers": [
                {
                    "icon": "ftmscan",
                    "name": "ftmscan",
                    "standard": "EIP3091",
                    "url": "https://ftmscan.com",
                },
                {
                    "icon": "dexguru",
                    "name": "dexguru",
                    "standard": "EIP3091",
                    "url": "https://fantom.dex.guru",
                },
            ],
            "faucets": [],
            "features": None,
            "icon": "fantom",
            "infoURL": "https://fantom.foundation",
            "name": "Fantom Opera",
            "nativeCurrency": {"decimals": 18, "name": "Fantom", "symbol": "FTM"},
            "networkId": 250,
            "rpc": [
                "https://rpc.ftm.tools",
                "https://fantom-rpc.publicnode.com",
                "https://fantom.drpc.org",
            ],
            "shortName": "ftm",
            "slip44": None,
        },
        "testnet": {
            "chain": "FTM",
            "chainId": 4002,
            "ens": None,
            "explorers": [
                {
                    "icon": "ftmscan",
                    "name": "ftmscan",
                    "standard": "EIP3091",
                    "url": "https://testnet.ftmscan.com",
                }
            ],
            "faucets": ["https://faucet.fantom.network"],
            "features": None,
            "icon": "fantom",
            "infoURL": "https://docs.fantom.foundation/quick-start/short-guide#fantom-testnet",
            "name": "Fantom Testnet",
            "nativeCurrency": {"decimals": 18, "name": "Fantom", "symbol": "FTM"},
            "networkId": 4002,
            "rpc": [
                "https://rpc.testnet.fantom.network",
                "https://fantom-testnet-rpc.publicnode.com",
                "https://fantom-testnet.drpc.org",
            ],
            "shortName": "tftm",
            "slip44": 1,
        },
    },
    "gnosis": {
        "mainnet": {
            "chain": "GNO",
            "chainId": 100,
            "ens": None,
            "explorers": [
                {
                    "name": "gnosisscan",
                    "standard": "EIP3091",
                    "url": "https://gnosisscan.io",
                },
                {
                    "icon": "blockscout",
                    "name": "blockscout",
                    "standard": "EIP3091",
                    "url": "https://gnosis.blockscout.com",
                },
                {
                    "icon": "dexguru",
                    "name": "dexguru",
                    "standard": "EIP3091",
                    "url": "https://gnosis.dex.guru",
                },
            ],
            "faucets": [
                "https://gnosisfaucet.com",
                "https://stakely.io/faucet/gnosis-chain-xdai",
                "https://faucet.prussia.dev/xdai",
            ],
            "features": None,
            "icon": "gnosis",
            "infoURL": "https://docs.gnosischain.com",
            "name": "Gnosis",
            "nativeCurrency": {"decimals": 18, "name": "xDAI", "symbol": "XDAI"},
            "networkId": 100,
            "rpc": [
                "https://rpc.gnosischain.com",
                "https://rpc.gnosis.gateway.fm",
                "https://rpc.ankr.com/gnosis",
                "https://gnosischain-rpc.gateway.pokt.network",
                "https://gnosis-mainnet.public.blastapi.io",
                "https://gnosis.api.onfinality.io/public",
                "https://gnosis.blockpi.network/v1/rpc/public",
                "https://web3endpoints.com/gnosischain-mainnet",
                "https://gnosis.oat.farm",
                "https://gnosis-rpc.publicnode.com",
            ],
            "shortName": "gno",
            "slip44": 700,
        },
    },
    "optimism": {
        "mainnet": {
            "chain": "ETH",
            "chainId": 10,
            "ens": None,
            "explorers": [
                {
                    "name": "etherscan",
                    "standard": "EIP3091",
                    "url": "https://optimistic.etherscan.io",
                },
                {
                    "icon": "blockscout",
                    "name": "blockscout",
                    "standard": "EIP3091",
                    "url": "https://optimism.blockscout.com",
                },
                {
                    "icon": "dexguru",
                    "name": "dexguru",
                    "standard": "EIP3091",
                    "url": "https://optimism.dex.guru",
                },
            ],
            "faucets": [],
            "features": None,
            "icon": None,
            "infoURL": "https://optimism.io",
            "name": "OP Mainnet",
            "nativeCurrency": {"decimals": 18, "name": "Ether", "symbol": "ETH"},
            "networkId": 10,
            "rpc": [
                "https://mainnet.optimism.io",
                "https://optimism-rpc.publicnode.com",
                "https://optimism.gateway.tenderly.co",
                "https://optimism.drpc.org",
            ],
            "shortName": "oeth",
            "slip44": None,
        },
        "goerli": {
            "chain": "ETH",
            "chainId": 420,
            "ens": None,
            "explorers": [
                {
                    "icon": "blockscout",
                    "name": "blockscout",
                    "standard": "EIP3091",
                    "url": "https://optimism-goerli.blockscout.com",
                }
            ],
            "faucets": [],
            "features": None,
            "icon": None,
            "infoURL": "https://optimism.io",
            "name": "Optimism Goerli Testnet",
            "nativeCurrency": {"decimals": 18, "name": "Goerli Ether", "symbol": "ETH"},
            "networkId": 420,
            "rpc": [
                "https://goerli.optimism.io",
                "https://optimism-goerli-rpc.publicnode.com",
                "https://optimism-goerli.gateway.tenderly.co",
                "https://optimism-testnet.drpc.org",
            ],
            "shortName": "ogor",
            "slip44": 1,
        },
        "sepolia": {
            "chain": "ETH",
            "chainId": 11155420,
            "ens": None,
            "explorers": [
                {
                    "icon": "blockscout",
                    "name": "opscout",
                    "standard": "EIP3091",
                    "url": "https://optimism-sepolia.blockscout.com",
                }
            ],
            "faucets": ["https://app.optimism.io/faucet"],
            "features": None,
            "icon": None,
            "infoURL": "https://optimism.io",
            "name": "OP Sepolia Testnet",
            "nativeCurrency": {
                "decimals": 18,
                "name": "Sepolia Ether",
                "symbol": "ETH",
            },
            "networkId": 11155420,
            "rpc": ["https://sepolia.optimism.io", "https://optimism-sepolia.drpc.org"],
            "shortName": "opsep",
            "slip44": 1,
        },
    },
    "oort": {
        "mainnet": {
            "chain": "Oort Mainnet",
            "chainId": 970,
            "ens": None,
            "explorers": [
                {
                    "icon": "oort",
                    "name": "Oort Mainnet Explorer",
                    "standard": "none",
                    "url": "https://mainnet-scan.oortech.com",
                }
            ],
            "faucets": [],
            "features": None,
            "icon": "oort",
            "infoURL": "https://oortech.com",
            "name": "Oort Mainnet",
            "nativeCurrency": {"decimals": 18, "name": "Oort", "symbol": "OORT"},
            "networkId": 970,
            "rpc": ["https://mainnet-rpc.oortech.com"],
            "shortName": "ccn",
            "slip44": None,
        },
        "dev": {
            "chain": "MainnetDev",
            "chainId": 9700,
            "ens": None,
            "explorers": [
                {
                    "icon": "oort",
                    "name": "Oort MainnetDev Scan",
                    "standard": "none",
                    "url": "https://dev-scan.oortech.com",
                }
            ],
            "faucets": [],
            "features": None,
            "icon": "oort",
            "infoURL": "https://oortech.com",
            "name": "Oort MainnetDev",
            "nativeCurrency": {"decimals": 18, "name": "Oort", "symbol": "OORT"},
            "networkId": 9700,
            "rpc": ["https://dev-rpc.oortech.com"],
            "shortName": "MainnetDev",
            "slip44": None,
        },
    },
    "polygon": {
        "mainnet": {
            "chain": "Polygon",
            "chainId": 137,
            "ens": None,
            "explorers": [
                {
                    "name": "polygonscan",
                    "standard": "EIP3091",
                    "url": "https://polygonscan.com",
                },
                {
                    "icon": "dexguru",
                    "name": "dexguru",
                    "standard": "EIP3091",
                    "url": "https://polygon.dex.guru",
                },
            ],
            "faucets": [],
            "features": None,
            "icon": "polygon",
            "infoURL": "https://polygon.technology/",
            "name": "Polygon Mainnet",
            "nativeCurrency": {"decimals": 18, "name": "MATIC", "symbol": "MATIC"},
            "networkId": 137,
            "rpc": [
                "https://polygon-rpc.com/",
                "https://rpc-mainnet.matic.network",
                "https://matic-mainnet.chainstacklabs.com",
                "https://rpc-mainnet.maticvigil.com",
                "https://rpc-mainnet.matic.quiknode.pro",
                "https://matic-mainnet-full-rpc.bwarelabs.com",
                "https://polygon-bor-rpc.publicnode.com",
                "https://polygon.gateway.tenderly.co",
                "https://polygon.drpc.org",
            ],
            "shortName": "matic",
            "slip44": 966,
        },
        "mumbai": {
            "chain": "Polygon",
            "chainId": 80001,
            "ens": None,
            "explorers": [
                {
                    "name": "polygonscan",
                    "standard": "EIP3091",
                    "url": "https://mumbai.polygonscan.com",
                }
            ],
            "faucets": ["https://faucet.polygon.technology/"],
            "features": None,
            "icon": "polygon",
            "infoURL": "https://polygon.technology/",
            "name": "Mumbai",
            "nativeCurrency": {"decimals": 18, "name": "MATIC", "symbol": "MATIC"},
            "networkId": 80001,
            "rpc": [
                "https://rpc-mumbai.maticvigil.com",
                "https://polygon-mumbai-bor-rpc.publicnode.com",
                "https://polygon-mumbai.gateway.tenderly.co",
            ],
            "shortName": "maticmum",
            "slip44": 1,
        },
    },
    "polygon-zkevm": {
        "mainnet": {
            "chain": "Polygon",
            "chainId": 1101,
            "ens": None,
            "explorers": [
                {
                    "icon": "zkevm",
                    "name": "blockscout",
                    "standard": "EIP3091",
                    "url": "https://zkevm.polygonscan.com",
                }
            ],
            "faucets": [],
            "features": None,
            "icon": "zkevm",
            "infoURL": "https://polygon.technology/polygon-zkevm",
            "name": "Polygon zkEVM",
            "nativeCurrency": {"decimals": 18, "name": "Ether", "symbol": "ETH"},
            "networkId": 1101,
            "rpc": ["https://zkevm-rpc.com", "https://polygon-zkevm.drpc.org"],
            "shortName": "zkevm",
            "slip44": None,
        },
        "testnet": {
            "chain": "Polygon",
            "chainId": 1442,
            "ens": None,
            "explorers": [
                {
                    "name": "Polygon zkEVM explorer",
                    "standard": "EIP3091",
                    "url": "https://explorer.public.zkevm-test.net",
                }
            ],
            "faucets": [],
            "features": None,
            "icon": None,
            "infoURL": "https://polygon.technology/solutions/polygon-zkevm/",
            "name": "Polygon zkEVM Testnet",
            "nativeCurrency": {"decimals": 18, "name": "Ether", "symbol": "ETH"},
            "networkId": 1442,
            "rpc": [
                "https://rpc.public.zkevm-test.net",
                "https://polygon-zkevm-testnet.drpc.org",
            ],
            "shortName": "testnet-zkEVM-mango",
            "slip44": 1,
        },
    },
    "linea": {
        "mainnet": {
            "chain": "ETH",
            "chainId": 59144,
            "ens": None,
            "explorers": [
                {
                    "icon": "linea",
                    "name": "Etherscan",
                    "standard": "EIP3091",
                    "url": "https://lineascan.build",
                },
                {
                    "icon": "linea",
                    "name": "Blockscout",
                    "standard": "EIP3091",
                    "url": "https://explorer.linea.build",
                },
                {
                    "icon": "linea",
                    "name": "L2scan",
                    "standard": "EIP3091",
                    "url": "https://linea.l2scan.co",
                },
            ],
            "faucets": [],
            "features": None,
            "icon": "linea",
            "infoURL": "https://linea.build",
            "name": "Linea",
            "nativeCurrency": {"decimals": 18, "name": "Linea Ether", "symbol": "ETH"},
            "networkId": 59144,
            "rpc": [
                "https://rpc.linea.build",
                "https://linea-mainnet.infura.io/v3/${INFURA_API_KEY}",
            ],
            "shortName": "linea",
            "slip44": None,
        },
        "sepolia": {
            "chain": "ETH",
            "chainId": 59141,
            "ens": None,
            "explorers": [
                {
                    "icon": "linea",
                    "name": "Etherscan",
                    "standard": "EIP3091",
                    "url": "https://sepolia.lineascan.build",
                },
                {
                    "icon": "linea",
                    "name": "Blockscout",
                    "standard": "EIP3091",
                    "url": "https://explorer.sepolia.linea.build",
                },
            ],
            "faucets": [],
            "features": None,
            "icon": "linea",
            "infoURL": "https://linea.build",
            "name": "Linea Sepolia",
            "nativeCurrency": {"decimals": 18, "name": "Linea Ether", "symbol": "ETH"},
            "networkId": 59141,
            "rpc": [
                "https://rpc.sepolia.linea.build",
                "https://linea-sepolia.infura.io/v3/${INFURA_API_KEY}",
            ],
            "shortName": "linea-sepolia",
            "slip44": 1,
        },
    },
}
