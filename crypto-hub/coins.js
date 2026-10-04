/* Crypto hub coin list
 * Fetched 2026-10-04 (America/New_York).
 * Do not treat this file as a price board. No prices are stored here.
 *
 * Listing sources read that day:
 * - Coinbase, US (incl. NY) trading assets:
 *   https://www.coinbase.com/legal/digital-asset-disclosures
 *   The page says Coinbase holdings are as of March 31, 2026, and that
 *   assets are added as they are supported for trading in New York.
 * - Robinhood crypto availability (row included only when
 *   "Tradable in-app and on web classic with market maker routing" was Yes):
 *   https://robinhood.com/us/en/support/articles/coin-availability/
 * - Uphold public asset list, status open, buy enabled, crypto or stablecoin:
 *   https://api.uphold.com/v0/assets
 * - Kraken supported cryptocurrencies (page last updated August 23, 2026):
 *   https://support.kraken.com/articles/360000678446-cryptocurrencies-available-on-kraken
 * - Gemini USD symbols from https://api.gemini.com/v1/symbols
 *   cross-checked with
 *   https://support.gemini.com/hc/en-us/articles/115005868106-What-cryptos-are-supported-on-the-Gemini-Exchange
 *
 * A coin is included only if at least two of those five list it.
 * This file keeps 40, ordered by how many of the five list it.
 * Ties are broken by CoinGecko market-cap rank fetched the same day
 * (https://api.coingecko.com/api/v3/coins/markets), used only to order.
 * Market cap is not published here. Coins that could not be verified are omitted.
 */
window.COINS = [
  {
    "id": "btc",
    "ticker": "BTC",
    "name": "Bitcoin",
    "exchanges": [
      "coinbase",
      "robinhood",
      "uphold",
      "kraken",
      "gemini"
    ]
  },
  {
    "id": "eth",
    "ticker": "ETH",
    "name": "Ethereum",
    "exchanges": [
      "coinbase",
      "robinhood",
      "uphold",
      "kraken",
      "gemini"
    ]
  },
  {
    "id": "doge",
    "ticker": "DOGE",
    "name": "Dogecoin",
    "exchanges": [
      "coinbase",
      "robinhood",
      "uphold",
      "kraken",
      "gemini"
    ]
  },
  {
    "id": "link",
    "ticker": "LINK",
    "name": "Chainlink",
    "exchanges": [
      "coinbase",
      "robinhood",
      "uphold",
      "kraken",
      "gemini"
    ]
  },
  {
    "id": "bch",
    "ticker": "BCH",
    "name": "Bitcoin Cash",
    "exchanges": [
      "coinbase",
      "robinhood",
      "uphold",
      "kraken",
      "gemini"
    ]
  },
  {
    "id": "ltc",
    "ticker": "LTC",
    "name": "Litecoin",
    "exchanges": [
      "coinbase",
      "robinhood",
      "uphold",
      "kraken",
      "gemini"
    ]
  },
  {
    "id": "avax",
    "ticker": "AVAX",
    "name": "Avalanche",
    "exchanges": [
      "coinbase",
      "robinhood",
      "uphold",
      "kraken",
      "gemini"
    ]
  },
  {
    "id": "aave",
    "ticker": "AAVE",
    "name": "Aave",
    "exchanges": [
      "coinbase",
      "robinhood",
      "uphold",
      "kraken",
      "gemini"
    ]
  },
  {
    "id": "dot",
    "ticker": "DOT",
    "name": "Polkadot",
    "exchanges": [
      "coinbase",
      "robinhood",
      "uphold",
      "kraken",
      "gemini"
    ]
  },
  {
    "id": "arb",
    "ticker": "ARB",
    "name": "Arbitrum",
    "exchanges": [
      "coinbase",
      "robinhood",
      "uphold",
      "kraken",
      "gemini"
    ]
  },
  {
    "id": "atom",
    "ticker": "ATOM",
    "name": "Cosmos",
    "exchanges": [
      "coinbase",
      "robinhood",
      "uphold",
      "kraken",
      "gemini"
    ]
  },
  {
    "id": "inj",
    "ticker": "INJ",
    "name": "Injective",
    "exchanges": [
      "coinbase",
      "robinhood",
      "uphold",
      "kraken",
      "gemini"
    ]
  },
  {
    "id": "fet",
    "ticker": "FET",
    "name": "Artificial Superintelligence Alliance",
    "exchanges": [
      "coinbase",
      "robinhood",
      "uphold",
      "kraken",
      "gemini"
    ]
  },
  {
    "id": "crv",
    "ticker": "CRV",
    "name": "Curve DAO",
    "exchanges": [
      "coinbase",
      "robinhood",
      "uphold",
      "kraken",
      "gemini"
    ]
  },
  {
    "id": "bonk",
    "ticker": "BONK",
    "name": "Bonk",
    "exchanges": [
      "coinbase",
      "robinhood",
      "uphold",
      "kraken",
      "gemini"
    ]
  },
  {
    "id": "grt",
    "ticker": "GRT",
    "name": "The Graph",
    "exchanges": [
      "coinbase",
      "robinhood",
      "uphold",
      "kraken",
      "gemini"
    ]
  },
  {
    "id": "jto",
    "ticker": "JTO",
    "name": "Jito",
    "exchanges": [
      "coinbase",
      "robinhood",
      "uphold",
      "kraken",
      "gemini"
    ]
  },
  {
    "id": "bnb",
    "ticker": "BNB",
    "name": "BNB",
    "exchanges": [
      "robinhood",
      "uphold",
      "kraken",
      "gemini"
    ]
  },
  {
    "id": "xrp",
    "ticker": "XRP",
    "name": "Ripple",
    "exchanges": [
      "coinbase",
      "robinhood",
      "kraken",
      "gemini"
    ]
  },
  {
    "id": "usdc",
    "ticker": "USDC",
    "name": "USD Coin",
    "exchanges": [
      "coinbase",
      "robinhood",
      "kraken",
      "gemini"
    ]
  },
  {
    "id": "sol",
    "ticker": "SOL",
    "name": "Solana",
    "exchanges": [
      "coinbase",
      "robinhood",
      "kraken",
      "gemini"
    ]
  },
  {
    "id": "zec",
    "ticker": "ZEC",
    "name": "Zcash",
    "exchanges": [
      "coinbase",
      "robinhood",
      "kraken",
      "gemini"
    ]
  },
  {
    "id": "hype",
    "ticker": "HYPE",
    "name": "Hyperliquid",
    "exchanges": [
      "robinhood",
      "uphold",
      "kraken",
      "gemini"
    ]
  },
  {
    "id": "ada",
    "ticker": "ADA",
    "name": "Cardano",
    "exchanges": [
      "coinbase",
      "robinhood",
      "uphold",
      "kraken"
    ]
  },
  {
    "id": "near",
    "ticker": "NEAR",
    "name": "NEAR Protocol",
    "exchanges": [
      "coinbase",
      "robinhood",
      "uphold",
      "kraken"
    ]
  },
  {
    "id": "uni",
    "ticker": "UNI",
    "name": "Uniswap",
    "exchanges": [
      "coinbase",
      "robinhood",
      "kraken",
      "gemini"
    ]
  },
  {
    "id": "sui",
    "ticker": "SUI",
    "name": "Sui",
    "exchanges": [
      "coinbase",
      "robinhood",
      "kraken",
      "gemini"
    ]
  },
  {
    "id": "hbar",
    "ticker": "HBAR",
    "name": "Hedera",
    "exchanges": [
      "coinbase",
      "robinhood",
      "uphold",
      "kraken"
    ]
  },
  {
    "id": "qnt",
    "ticker": "QNT",
    "name": "Quant",
    "exchanges": [
      "coinbase",
      "robinhood",
      "kraken",
      "gemini"
    ]
  },
  {
    "id": "shib",
    "ticker": "SHIB",
    "name": "Shiba Inu",
    "exchanges": [
      "coinbase",
      "robinhood",
      "kraken",
      "gemini"
    ]
  },
  {
    "id": "sky",
    "ticker": "SKY",
    "name": "Sky",
    "exchanges": [
      "coinbase",
      "robinhood",
      "kraken",
      "gemini"
    ]
  },
  {
    "id": "morpho",
    "ticker": "MORPHO",
    "name": "Morpho",
    "exchanges": [
      "coinbase",
      "robinhood",
      "uphold",
      "kraken"
    ]
  },
  {
    "id": "pepe",
    "ticker": "PEPE",
    "name": "Pepecoin",
    "exchanges": [
      "coinbase",
      "robinhood",
      "kraken",
      "gemini"
    ]
  },
  {
    "id": "algo",
    "ticker": "ALGO",
    "name": "Algorand",
    "exchanges": [
      "coinbase",
      "robinhood",
      "uphold",
      "kraken"
    ]
  },
  {
    "id": "fil",
    "ticker": "FIL",
    "name": "Filecoin",
    "exchanges": [
      "coinbase",
      "uphold",
      "kraken",
      "gemini"
    ]
  },
  {
    "id": "aero",
    "ticker": "AERO",
    "name": "Aerodrome Finance",
    "exchanges": [
      "coinbase",
      "robinhood",
      "uphold",
      "kraken"
    ]
  },
  {
    "id": "flr",
    "ticker": "FLR",
    "name": "Flare",
    "exchanges": [
      "coinbase",
      "robinhood",
      "uphold",
      "kraken"
    ]
  },
  {
    "id": "pyth",
    "ticker": "PYTH",
    "name": "Pyth Network",
    "exchanges": [
      "coinbase",
      "robinhood",
      "kraken",
      "gemini"
    ]
  },
  {
    "id": "pengu",
    "ticker": "PENGU",
    "name": "Pudgy Penguins",
    "exchanges": [
      "coinbase",
      "robinhood",
      "kraken",
      "gemini"
    ]
  },
  {
    "id": "mon",
    "ticker": "MON",
    "name": "Monad",
    "exchanges": [
      "coinbase",
      "uphold",
      "kraken",
      "gemini"
    ]
  }
];
window.EXTRA_STUBS = [
  {
    "id": "mstr",
    "ticker": "MSTR",
    "name": "Strategy",
    "kind": "stock",
    "note": "Common stock. Not a coin on the exchange list above."
  }
];
