from qume_client import qume_api_methods
import ast
from qume_client import qume_api_methods
import ast
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, wait
import grpc
import engine_pb2
import engine_pb2_grpc

api_path = "https://api.qume.io"
timeout = 10

# insert account-specific api keys
api_key = "09524c02-f900-4c83-add3-94c54d78ce96"
api_secret = "74e9484aa7dd6b1a864dc4ed1a19531e"
api_passphrase = "spen"

# initialize instance of client
qume_client = qume_api_methods(api_path, api_key=api_key, api_secret=api_secret, api_passphrase=api_passphrase, show_raw_request=False, timeout=timeout)

symbol = "BTCUSDQ"
side = "BUY"
price = int(round(1 / 3980.00 * 100000000))
qty = 1
type = "LIMIT"
time_in_force = "UNTIL_CANCEL"
post_only = False

def place_order(x):
    return qume_client.place_order(symbol, side, price, qty, type, time_in_force, post_only)[0]

executor = ThreadPoolExecutor(1)
numRequests = 1
futures = [executor.submit(place_order(), x) for x in range(numRequests)]
wait(futures)

print("place_order:\n", frame.describe())
