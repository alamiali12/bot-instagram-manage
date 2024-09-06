import time
import random
from instagrapi import Client
from colorama import Fore
from utils import animated_text  # از utils وارد کنید
from db import add_account, get_accounts, add_proxy, update_account_token
from proxy import get_random_proxy

def login_and_update_profile(username, password):
    try:
        cl = Client()
        proxy = get_random_proxy()
        if proxy:
            cl.set_proxy(proxy)

        cl.login(username, password)
        token = cl.get_settings()

        # Change profile name and ID
        full_name = generate_full_name()
        cl.account_edit(full_name=full_name)
        cl.username = generate_similar_username(full_name)

        # Set profile picture based on gender
        if is_male_name(full_name):
            cl.account_change_picture('male_profile_pic.jpg')
        else:
            cl.account_change_picture('female_profile_pic.jpg')

        # Save account to JSON
        add_account(username, password, str(token))
        animated_text(f"Account updated and logged in successfully.", color=Fore.GREEN)
    except Exception as e:
        animated_text(f"Error logging in with account {username}: {e}", color=Fore.RED)

def generate_full_name():
    # Generate a full name based on some logic
    return "John Doe"

def generate_similar_username(full_name):
    # Create a username based on the full name
    return full_name.lower().replace(' ', '_') + str(random.randint(100, 999))

def is_male_name(name):
    # Simple gender determination based on name (you can improve this logic)
    return name.split()[0].lower() in ['john', 'michael', 'david']

def report_user():
    accounts = get_accounts()
    if not accounts:
        animated_text(f"No accounts available. Please add an account first.", color=Fore.RED)
        input(f"{Fore.YELLOW}Press any key to return to the menu...")
        return

    animated_text(f"Enter the username of the user to report: ", color=Fore.CYAN)
    user_id = input()
    if not user_id:
        animated_text(f"Username cannot be empty.", color=Fore.RED)
        input(f"{Fore.YELLOW}Press any key to return to the menu...")
        return

    success = False
    for account in accounts:
        username = account['username']
        password = account['password']
        try:
            cl = Client()
            proxy = get_random_proxy()
            if proxy:
                cl.set_proxy(proxy)
            cl.login(username, password)
            user_id_int = cl.user_id_from_username(user_id)
            cl.user_report(user_id_int, 'spam')
            animated_text(f"Reported {user_id} using account {username}.", color=Fore.GREEN)
            success = True
            time.sleep(60)
        except Exception as e:
            animated_text(f"Error reporting with account {username}: {e}", color=Fore.RED)
            success = False

    if success:
        animated_text("Operation successful!", color=Fore.GREEN)
    else:
        animated_text("Operation failed!", color=Fore.RED)

def like_posts():
    accounts = get_accounts()
    if not accounts:
        animated_text(f"No accounts available. Please add an account first.", color=Fore.RED)
        input(f"{Fore.YELLOW}Press any key to return to the menu...")
        return

    animated_text(f"Enter the username of the user whose posts you want to like: ", color=Fore.CYAN)
    target_username = input()
    if not target_username:
        animated_text(f"Username cannot be empty.", color=Fore.RED)
        input(f"{Fore.YELLOW}Press any key to return to the menu...")
        return

    for account in accounts:
        username = account['username']
        password = account['password']
        try:
            cl = Client()
            proxy = get_random_proxy()
            if proxy:
                cl.set_proxy(proxy)
            cl.login(username, password)
            user_id = cl.user_id_from_username(target_username)
            medias = cl.user_medias(user_id, 20)
            for media in medias:
                cl.media_like(media.pk)
                animated_text(f"Liked post {media.pk} using account {username}.", color=Fore.GREEN)
                time.sleep(random.randint(30, 60))
        except Exception as e:
            animated_text(f"Error liking posts with account {username}: {e}", color=Fore.RED)

def schedule_posts():
    animated_text(f"Enter the username of the user to schedule posts for: ", color=Fore.CYAN)
    target_username = input()
    if not target_username:
        animated_text(f"Username cannot be empty.", color=Fore.RED)
        input(f"{Fore.YELLOW}Press any key to return to the menu...")
        return

    # Implement scheduling logic here
