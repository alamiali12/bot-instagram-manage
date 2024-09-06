import random
from db import get_proxies

def get_random_proxy():
    proxies = get_proxies()
    if proxies:
        return random.choice(proxies)
    return None
