 
from alpaca.trading.client import TradingClient
from alpaca.broker.client import BrokerClient
from alpaca.data.historical import StockHistoricalDataClient, CryptoHistoricalDataClient
from alpaca.data.requests import CryptoLatestQuoteRequest 
from alpaca.data.live.crypto import CryptoDataStream
from alpaca.data.timeframe import TimeFrame
import sys
import os



# Get the absolute path to the root directory 
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add it to sys.path if not already added
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

# Now you can safely import creds
try:
    import creds
except ImportError:
    raise ImportError("Could not find creds.py. Ensure it's in the project root and not renamed.")

API_KEY = creds.api_key
SECRET_KEY = creds.api_secret_key
BASE_URL = creds.api_base_URL

#Paper trading client 
trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)

#Market Data 
stock_client = StockHistoricalDataClient(API_KEY, SECRET_KEY)
crypto_client = CryptoHistoricalDataClient()

#Broker API client 
broker_client = BrokerClient(API_KEY, SECRET_KEY, sandbox=True)

#CryptoDataStream client 
crypto_data_stream = CryptoDataStream(API_KEY, SECRET_KEY, raw_data=False)

