import random
import string
import requests

print("\033[34m ____            ______            _      _                  _____ __ __ ___ \n   / __ )____ _____/ / __ \\___  _____(_)____(_)___  ____  _____/ ___// // /|__ \\ \n  / __  / __ `/ __  / / / / _ \\/ ___/ / ___/ / __ \\/ __ \\/ ___/ __ \\/ // /___/ / \n / /_/ / /_/ / /_/ / /_/ /  __/ /__/ (__  ) / /_/ / / / (__  ) /_/ /__  __/ __/ \n/_____/\\__,_/\\__,_/_____/\\___/\\___/_/____/_/\\____/_/ /_/____/\\____/  /_/ /____/ \033[0m")

def check_username_availability(username):
    url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
    r = requests.get(url)
    if r.status_code == 204:
        return True
    return False

def generate_username(length, with_numbers):
    chars = string.ascii_lowercase + string.digits if with_numbers else string.ascii_lowercase
    return ''.join(random.choices(chars, k=length))

def username_checker():
    user_len = int(input("\033[35mEnter the username length: \033[0m"))
    nums = input("\033[35mInclude numbers in usernames? (y/n): \033[0m").lower() == 'y'
    num_to_generate = int(input("\033[35mHow many usernames do you want to generate? \033[0m"))
    stop_input = input("\033[35mPress 'Enter' to begin, Type 'cancel' to exit. \033[0m").lower()
    if stop_input == 'cancel':
        print("\033[31mcanceled.. sad times fr\033[0m")
        return
    available_usernames = []
    try_count = 0
    while try_count < num_to_generate:
        user_name = generate_username(user_len, nums)
        print(f"\033[35mChecking username: {user_name}\033[0m")
        if check_username_availability(user_name):
            print(f"\033[35mUsername {user_name} is untaken.. YIPEE!\033[0m")
            available_usernames.append(user_name)
        try_count += 1
    if available_usernames:
        print("\033[35mAvailable usernames:\033[0m")
        for username in available_usernames:
            print(f"\033[35m{username}\033[0m")
    else:
        print("\033[31mNo available users here.. sorry\033[0m")

username_checker()