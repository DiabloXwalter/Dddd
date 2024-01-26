import threading
import tls_client
import requests
import json
import time
import random
import string
import ctypes
from colorama import Fore, init

init()

session = tls_client.Session(
    client_identifier="chrome112",
    random_tls_extension_order=True
)

count = 0

red = '\x1b[31m❌\x1b[0m'
blue = '\x1b[34m[INF]\x1b[0m'
green = '\x1b[32m✅\x1b[0m'
yellow = '\x1b[33m[INF]\x1b[0m'
G = '\x1b[32m'
yell = '\x1b[33m'
reset = '\x1b[0m'


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))


def set_cmd_window_title(count):
    title = f"Generated : {count} N | Free by Discord Station | Made at : 2023/12/23"
    ctypes.windll.kernel32.SetConsoleTitleW(title)


def worker():
    global count
    url = 'https://api.discord.gx.games/v1/direct-fulfillment'
    headers = {
        'authority': 'api.discord.gx.games',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://www.opera.com',
        'referer': 'https://www.opera.com/',
        'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0'
    }

    data = {
        'partnerUserId': generate_random_string(64)
    }

    def get_timestamp():
        time_idk = time.strftime('%H:%M:%S')
        timestamp = f'[\x1b[90m{time_idk}\x1b[0m]'
        return timestamp

    try:
        while True:
            response = session.post(url, headers=headers, json=data)

            if response.status_code == 200:
                count += 1
                set_cmd_window_title(count)
                token = response.json()['token']
                with open('n.txt', 'a') as file:
                    file.write(f"https://discord.com/billing/partner-promotions/1180231712274387115/{token}\n")
                promo = f'https://discord.com/billing/partner-promotions/1180231712274387115/{token}'
                print(f"{get_timestamp()} {green} New Promo -> {Fore.LIGHTMAGENTA_EX}discord.com/billing/partn.../{promo[67:120]}{reset} -> Genned : {yell}{count}{reset}")            
            else:
                print(f"Error : {response.text}")

            time.sleep(1)

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    num_threads = int(input(blue+" Enter how many threads do you want -> "))

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=worker)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
