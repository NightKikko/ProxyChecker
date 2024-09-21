# -*- coding: utf-8 -*-
import sys
import io
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, Style, init
import os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

init(autoreset=True)

def log(status, message):
    status_colors = {
        "INFO": Fore.BLUE,
        "SUCCESS": Fore.GREEN,
        "ERROR": Fore.RED,
    }
    color = status_colors.get(status, Fore.WHITE)
    print(f"{color}[{status}] {Style.RESET_ALL}{message}\n")

os.system("title Proxy Checker")

def load_proxy_apis():
    try:
        with open("proxy_apis.txt", "r") as file:
            return [line.strip() for line in file if line.strip()]
    except Exception as e:
        log("ERROR", f"Error loading proxy APIs: {e}")
        return []

def fetch_proxies(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        log("INFO", f"Proxies retrieved from {api_url}.")
        return response.text.splitlines()
    except requests.RequestException as e:
        log("ERROR", f"Error retrieving proxies from {api_url}: {e}")
        return []

def test_proxy(proxy):
    try:
        response = requests.get("http://httpbin.org/ip", proxies={"http": proxy}, timeout=5)
        if response.status_code == 200:
            log("SUCCESS", f"Valid proxy: {proxy}")
            save_valid_proxy(proxy)
            return proxy
    except requests.RequestException:
        log("ERROR", f"Invalid proxy (connection error): {proxy}")

    return None

def save_valid_proxy(proxy):
    with open("valid_proxies.txt", "a") as file:
        file.write(f"{proxy}\n")

def main():
    proxies = []
    proxy_apis = load_proxy_apis()
    
    log("INFO", "🌟 If you enjoy this project, please consider starring it on GitHub! 🌟")
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_api = {executor.submit(fetch_proxies, api): api for api in proxy_apis}
        for future in as_completed(future_to_api):
            proxies.extend(future.result())

    log("INFO", f"Proxies retrieved: {len(proxies)}")

    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_proxy = {executor.submit(test_proxy, proxy): proxy for proxy in proxies}
        for future in as_completed(future_to_proxy):
            future.result()

    log("INFO", "✅ Proxy testing completed. Thank you for using Proxy Checker! ✅")

if __name__ == "__main__":
    main()
