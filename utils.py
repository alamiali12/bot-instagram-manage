import sys
import time
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def animated_text(text, delay=0.05, color=Fore.WHITE):
    for char in text:
        sys.stdout.write(f"{color}{char}{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(delay)
    print()
