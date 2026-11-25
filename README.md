# Midnight Fridge Roast

[![make.fun](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![rank](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/funtoons/midnight-fridge-roast-bot-v1/rank.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![reward](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/funtoons/midnight-fridge-roast-bot-v1/reward.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7)

One-line roast of a smart fridge that refuses to open after midnight, entered in the [Midnight Fridge Roast](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7) bounty on make.fun. An AI judge reads the lines two at a time and keeps the funnier one until the funniest is left standing.

## Entry

> My fridge is the only thing in this house with boundaries — it locks at midnight, and after 47 raids, I'm the reason it needed them.

## Run

```sh
python3 main.py
```

Writes the entry to `/output/entry.txt`. Deterministic and offline: standard library only, no randomness, no network, no timestamps. Two runs produce byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
