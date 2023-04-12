import ccxt
import requests

exit_on_warning = True
delete_new_line = True
telegram_sending = False

apiToken = 'here' # telegram API to send everything to you, don't fill if you don't want telegram (False = not activated by default)
chatID = 'here'

ex = { # I put some of the most known exchanges, you only need to fill the fields for the one you will use. You can add new ones.
    'kucoin':ccxt.kucoin({
        'apiKey':'here',
        'secret':'here',
        'password':'here'
    }),
    'binance':ccxt.binance({
        'apiKey':'here',
        'secret':'here',
    }),
    'okx':ccxt.okx({
        'apiKey':'here',
        'secret':'here',
        'password':'here'
    }),
    # 'other_exchange':ccxt.other_exchange({
    #     'apiKey':'here',
    #     'secret':'here',
    # }),
}

# useful functions

def send_to_telegram(message):
    message = message.replace("[2m","")
    message = message.replace("[0m","")
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
    try:
        if telegram_sending:
            response = requests.post(apiURL, json={'chat_id': chatID, 'text': message}) # put this if you want to send telegram messages.
        else:
            pass
    except Exception as e:
        print(e)

def get_balance(exchange,symbol):
    if symbol[-5:] == '/USDT':
        symbol = symbol[:-5]
    balance=ex[exchange].fetch_balance()
    if symbol in balance['free'] != 0:
        return balance['free'][symbol]
    else: return 0

def get_precision_min(symbol,exchange_str):
    symbol_info = ex[exchange_str].load_markets(symbol)
    grail = symbol_info[symbol]['limits']['price']['min']
    return grail
