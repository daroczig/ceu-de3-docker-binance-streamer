from binance.websockets import BinanceSocketManager
from binance.client import Client
client = Client('foo', 'bar')
bm = BinanceSocketManager(client)

import json
import sys
def print_json(msg):
    print(json.dumps(msg['data']))
    sys.stdout.flush()

bm.start_multiplex_socket([
    'btcusdt@trade', 'ethusdt@trade', 'ltcusdt@trade', 'neousdt@trade', 'bnbusdt@trade',
    'ethbtc@trade', 'ltcbtc@trade', 'neobtc@trade', 'bnbbtc@trade', 'ltceth@trade',
    'neoeth@trade', 'bnbeth@trade', 'neobnb@trade', 'ltcbnb@trade'], print_json)

bm.start()
