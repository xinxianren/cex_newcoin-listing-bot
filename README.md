<p align="left">
  <img alt="Barbotine Logo" width="30%" height="30%" src="https://cdn.discordapp.com/attachments/876447732259225612/1095369391052443708/bas.svg">
</p>

[![Twitter @nelsodot](https://img.shields.io/twitter/url/https/twitter.com/nelsodot.svg?style=social&label=%20%40nelsodot)](https://twitter.com/nelsodot)
[![GitHub @nelso0](https://img.shields.io/github/followers/nelso0?label=follow&style=social)](https://github.com/nelso0)

Barbotine Listing is the fastest listing bot on the market because it uses websockets to check if a crypto asset is listed on the exchange or not. It works on all exchanges ([CCXT](https://github.com/ccxt/ccxt) exchanges). You just have to tell it the crypto that is about to be listed on the exchange and it will check endlessly and then send the stop-loss and take-profit orders you want at the best price.

## Table of content
* [Features](#features)
* [Demo](#demo)
* [Prerequisites](#prerequis)
* [Installation](#installation)
* [Usage](#usage)
* [Contact](#contact)
* [Real version](#full-version)
<a name="features"/>
 
## Features

* Compatible with almost any exchange (all [ccxt](https://github.com/ccxt/ccxt) exchanges).
* Websockets usage (makes it much faster)
* Customizable
* Full live tracking on Telegram
* Intuitive UI

<a name="demo"/>
 
## Demo

![Barbotine Listing Bot demo](https://cdn.discordapp.com/attachments/876447732259225612/1095807659082518579/listing.gif)

[video demo](https://youtu.be/MBRManvUWhI)

<a name="prerequis"/>
 
## Prerequisites

The things you need before installing the software.

* Python 3.9+ (for windows users: if python or pip isn't recognized as a command, make sure you have installed python by checking the box "add to PATH")
* Nothing else lol

<a name="installation"/>
 
## Installation

1. Clone the repository 
```sh
git clone https://github.com/nelso0/barbotine-listing-bot # you can also download the zip file
```
2. Go to the repository you just cloned
```sh
cd barbotine-listing-bot
```
3. Install all the requirements to run the arbitrage system
```sh
pip install -r requirements.txt
```
6. Set your configuration details in [config.py](config.py)
5. Run with:
```sh
python main.py
```

<a name="usage"/>
 
## Usage

You can also run it with one line like this:

```sh
python main.py <exchange> <crypto-pair> <balance-usdt-to-use> <requests-speed>
```


* ```<exchange>``` = the exchange you wanna use among all [ccxt](https://github.com/ccxt/ccxt) exchanges.
  
* ```<crypto-pair>``` = the crypto-pair you wanna launch the bot on. Example: NELSO/USDT (it doesn't exist)

* ```<balance-usdt-to-use>``` = how to be clearer? 

* ```<requests-speed>``` = the requests speed you wanna use among ```slow```,```medium```,```fast```,```supersonic```. (```supersonic``` is really faster than ```fast```, be careful for your CPU)

Examples:

```sh
python main.py kucoin NELSO/USDT 500 medium
```
```sh
python main.py binance NELSO/USDT 140 supersonic 
```
```sh
python main.py binance NELSO/USDT 10000 low 
```

## Contact

If you have any questions or you want to discuss of the bot with me, let's talk!

Discord: nelso#1800

Email: [nelso@barbotine.capital](mailto:nelso@barbotine.capital)

<a name="full-version"/>
 
## Full version

There is also a full version which operates with real dollars. (soon)

It will soon be available for purchase for $25, stay updated on [barbotine.capital](https://barbotine.capital)
