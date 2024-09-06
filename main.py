import time
import random
import os
import sys
from colorama import init, Fore, Style
from db import add_account, get_accounts, add_proxy, init_db
from proxy import get_random_proxy
from utils import animated_text  # مطمئن شوید که از utils وارد می‌کنید
from instagramss import report_user, login_and_update_profile, like_posts, schedule_posts

# Initialize colorama
init(autoreset=True)

def display_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Style.BRIGHT}{Fore.CYAN}{'='*40}")
    print(f"{Style.BRIGHT}{Fore.YELLOW}{'Instagram Bot'.center(40)}")
    print(f"{Style.BRIGHT}{Fore.CYAN}{'='*40}")
    print(f"{Style.BRIGHT}{Fore.GREEN}1. Report a user")
    print(f"{Style.BRIGHT}{Fore.GREEN}2. Add an account and login")
    print(f"{Style.BRIGHT}{Fore.GREEN}3. Add a proxy")
    print(f"{Style.BRIGHT}{Fore.GREEN}4. Like posts")
    print(f"{Style.BRIGHT}{Fore.GREEN}5. Schedule post upload")
    print(f"{Style.BRIGHT}{Fore.RED}0. Exit")
    print(f"{Style.BRIGHT}{Fore.CYAN}{'='*40}")

def add_account_prompt():
    animated_text(f"Enter the account username: ", color=Fore.CYAN)
    username = input()
    animated_text(f"Enter the account password: ", color=Fore.CYAN)
    password = input()
    if not username or not password:
        animated_text(f"Username and password cannot be empty.", color=Fore.RED)
        input(f"{Fore.YELLOW}Press any key to return to the menu...")
        return

    login_and_update_profile(username, password)

def add_proxy_prompt():
    animated_text(f"Enter the proxy (e.g., http://123.123.123.123:8080): ", color=Fore.CYAN)
    proxy = input()
    if not proxy:
        animated_text(f"Proxy cannot be empty.", color=Fore.RED)
        input(f"{Fore.YELLOW}Press any key to return to the menu...")
        return

    add_proxy(proxy)
    animated_text(f"Proxy added successfully.", color=Fore.GREEN)
    input(f"{Fore.YELLOW}Press any key to return to the menu...")

def main():
    init_db()
    while True:
        display_menu()
        choice = input(f"{Fore.CYAN}Choose an option: ")

        if choice == '1':
            report_user()
        elif choice == '2':
            add_account_prompt()
        elif choice == '3':
            add_proxy_prompt()
        elif choice == '4':
            like_posts()
        elif choice == '5':
            schedule_posts()
        elif choice == '0':
            animated_text("Exiting...", color=Fore.RED)
            sys.exit()
        else:
            animated_text("Invalid option. Please try again.", color=Fore.RED)
            input(f"{Fore.YELLOW}Press any key to return to the menu...")

if __name__ == "__main__":
    main()
