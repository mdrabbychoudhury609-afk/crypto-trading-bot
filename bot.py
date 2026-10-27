import ccxt
import time
import os

# বাইনান্স এপিআই কনফিগারেশন (আপনার বাইনান্স অ্যাকাউন্ট থেকে API Key এবং Secret এখানে দিতে হবে)
# সিকিউরিটির জন্য এগুলো আমরা রেন্ডারের Environment Variables থেকেও লোড করতে পারি
API_KEY = os.getenv('BINANCE_API_KEY', 'YOUR_API_KEY_HERE')
API_SECRET = os.getenv('BINANCE_API_SECRET', 'YOUR_API_SECRET_HERE')

exchange = ccxt.binance({
    'apiKey': API_KEY,
    'secret': API_SECRET,
    'enableRateLimit': True,
    'options': {
        'defaultType': 'spot'
    }
})

SYMBOL = 'BTC/USDT'  # ট্র্যাকিং পেয়ার
CHECK_INTERVAL = 60  # প্রতি ৬০ সেকেন্ড পর পর মার্কেট চেক করবে

def run_bot():
    print(f"--- Crypto Trading Bot Started for {SYMBOL} ---")
    while True:
        try:
            # বর্তমান মার্কেট প্রাইস ফেচ করা
            ticker = exchange.fetch_ticker(SYMBOL)
            current_price = ticker['last']
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {SYMBOL} Current Price: {current_price} USDT")
            
            # এখানে আপনার ট্রেইলিং প্রফিট রাইডার এবং ২০% ক্যাপিটাল ম্যানেজমেন্ট লজিক যুক্ত হবে
            
        except Exception as e:
            print(f"Error occurred: {e}")
            
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    run_bot()