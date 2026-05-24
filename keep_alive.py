import requests
import time
from datetime import datetime

# Target URL to visit
URL = "https://nine626-topical-questions.onrender.com/"

# Interval in minutes
INTERVAL_MINUTES = 5
INTERVAL_SECONDS = INTERVAL_MINUTES * 60

def visit_url():
    """Performs a GET request to the target URL."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] Attempting to visit {URL}...")
    
    try:
        # requests handles proxies and SSL/TLS more robustly than urllib
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        
        response = requests.get(URL, headers=headers, timeout=30)
        print(f"[{now}] Success! Status code: {response.status_code}")
    except Exception as e:
        print(f"[{now}] Error occurred: {e}")

def main():
    """Executes a single URL visit."""
    print("Executing URL Pinger...")
    visit_url()

if __name__ == "__main__":
    main()
