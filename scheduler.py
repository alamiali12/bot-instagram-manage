import time
import random
from instagrapi import Client
from colorama import Fore
from proxy import get_random_proxy
from db import get_accounts
import threading

def schedule_posts(target_username):
    accounts = get_accounts()
    if not accounts:
        print(f"{Fore.RED}No accounts available. Please add an account first.")
        return

    for account in accounts:
        username = account['username']
        password = account['password']

        # ایجاد یک ترد برای هر حساب به منظور مدیریت پست‌های زمان‌بندی شده
        thread = threading.Thread(target=post_randomly, args=(username, password, target_username))
        thread.start()

def post_randomly(username, password, target_username):
    try:
        cl = Client()
        proxy = get_random_proxy()
        if proxy:
            cl.set_proxy(proxy)
        cl.login(username, password)
        user_id = cl.user_id_from_username(target_username)

        while True:
            # دریافت پست‌های کاربر
            medias = cl.user_medias(user_id, 10)  # دریافت 10 پست آخر
            if medias:
                # انتخاب تصادفی یک پست برای ارسال
                media = random.choice(medias)
                caption = f"Scheduled post by {username}"
                cl.photo_upload(media.media_path, caption)
                print(f"{Fore.GREEN}Posted photo using account {username}")

            # زمان‌بندی پست بعدی (هر دو یا سه روز)
            next_post_time = random.randint(2, 3) * 24 * 60 * 60  # تبدیل به ثانیه
            print(f"{Fore.YELLOW}Next post for {username} in {next_post_time // 86400} days.")
            time.sleep(next_post_time)

    except Exception as e:
        print(f"{Fore.RED}Error posting with account {username}: {e}")
