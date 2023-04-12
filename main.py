import ccxt.pro
from asyncio import run
import time
import sys
import requests
from config import *
from colorama import Fore, Back, Style, init
init()

sys.stdin.reconfigure(encoding="utf-8")
sys.stdout.reconfigure(encoding="utf-8")

async def search(exchange:str,pair:str,speed:str):
    if speed == "supersonic":
        delay = 0
        limit = 1000000
    if speed == "fast":
        delay = 0.003
        limit = 9000
    if speed == "medium":
        delay = 0.008
        limit = 5000
    if speed == "slow":
        delay = 0.012
        limit = 1500
    print(" ")
    echange = getattr(ccxt.pro, exchange)()
    l=1
    while True:
        i=0
        while i<limit:
            time.sleep(delay)
            i+=1
            try:
                symbol = await echange.watch_ticker(pair)
                print(f"{Style.DIM}[{time.strftime('%H:%M:%S', time.gmtime(time.time()))}]{Style.RESET_ALL} {Fore.YELLOW}[Update n°{i}]{Style.RESET_ALL} {Fore.BLUE}[Loop n°{l}]{Style.RESET_ALL} {pair} is listed!")
                send_to_telegram(f"[{time.strftime('%H:%M:%S', time.gmtime(time.time()))}] [Update n°{i}] [Loop n°{l}] {pair} is listed!")
                if i==1:
                    print(f"{Style.DIM}[{time.strftime('%H:%M:%S', time.gmtime(time.time()))}]{Style.RESET_ALL} {Fore.RED}Warning:{Style.RESET_ALL} It seems to be an old symbol. Be cautious while buying this asset.")
                    if exit_on_warning:
                        print(" ")
                        await echange.close()
                        sys.exit(1)
                await echange.close()
                return symbol
            except Exception as e:
                if str(e) == f"{exchange} does not have market symbol {pair}":
                    if delete_new_line:
                        sys.stdout.write("\033[F")
                        sys.stdout.write("\033[K")
                    print(f"{Style.DIM}[{time.strftime('%H:%M:%S', time.gmtime(time.time()))}]{Style.RESET_ALL} {Fore.YELLOW}[Update n°{i}]{Style.RESET_ALL} {Fore.BLUE}[Loop n°{l}]{Style.RESET_ALL} {pair} not listed on {exchange} yet.")
                else:
                    print(f"{Fore.RED}error: {e}{Style.RESET_ALL}")
                    sys.exit(1)
        print(f"{Style.DIM}[{time.strftime('%H:%M:%S', time.gmtime(time.time()))}]{Style.RESET_ALL} Pausing to avoid API polling/banning...")
        await echange.close()
        print(f"{Style.DIM}[{time.strftime('%H:%M:%S', time.gmtime(time.time()))}]{Style.RESET_ALL} Relaunching...\n")
        time.sleep(2)
        l+=1

async def main(exchange:str,pair:str, how_much_to_invest:float,speed:str):
    symbol = await search(exchange,pair,speed)
    tick_size = get_precision_min(pair,exchange)
    print(f"{Style.DIM}[{time.strftime('%H:%M:%S', time.gmtime(time.time()))}]{Style.RESET_ALL} If that was the full version, orders would be sent here at {str(symbol['ask']-tick_size)} for {str(round(how_much_to_invest/symbol['ask'],2))} {symbol['symbol'][:-5]}")


print("""
█▄▄ ▄▀█ █▀█ █▄▄ █▀█ ▀█▀ █ █▄░█ █▀▀   █░░ █ █▀ ▀█▀ █ █▄░█ █▀▀   █▄▄ █▀█ ▀█▀
█▄█ █▀█ █▀▄ █▄█ █▄█ ░█░ █ █░▀█ ██▄   █▄▄ █ ▄█ ░█░ █ █░▀█ █▄█   █▄█ █▄█ ░█░""")
print(" \nUnder Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) license, for personal-use only.\n \nGithub: nelso0\nTwitter: @nelsodot\n")

if len(sys.argv) != 5:
    echangeur = input(f"exchange{Style.DIM} >>> {Style.RESET_ALL}")
    paire = input(f"pair to snipe{Style.DIM} >>> {Style.RESET_ALL}")
    investment = input(f"amount of USDT to invest (available balance: {str(round(get_balance(echangeur,'USDT'),2))} USDT){Style.DIM} >>> {Style.RESET_ALL}")
    speed = input(f"speed of requests (slow, medium, fast, supersonic){Style.DIM} >>> {Style.RESET_ALL}")
else:
    echangeur = sys.argv[1]
    paire = sys.argv[2]
    investment = float(sys.argv[3])
    speed = sys.argv[4]

run(main(echangeur,paire,investment,speed=speed))
