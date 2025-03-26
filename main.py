import requests
import re
import sys
import time
from colorama import Fore, Style, init
from threading import Thread
from datetime import datetime  

init(autoreset=True)

log_file = "GeoTool_log.txt" 

def save_log(message):
    try:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        full_message = f"[{current_time}] {message}"  
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(full_message + "\n")
    except Exception as e:
        print(f"{Fore.RED}Failed to save log: {e}{Style.RESET_ALL}")

def check_network_status():
    try:
        start_time = time.time()  
        print(f"{Fore.YELLOW}Checking network status...{Style.RESET_ALL}")
        response = requests.get("https://www.google.com", timeout=5)
        latency = round((time.time() - start_time) * 1000, 2)  
        
        if response.status_code == 200:
            status = f"Network is up!"
        else:
            status = f"Network is down! Status Code: {response.status_code}"
        
        message = (f"{status}\n"
                   f"Latency: {latency} ms\n"
                   f"Status Code: {response.status_code}")
        save_log(message)
        return message
    except requests.exceptions.RequestException as e:
        error_message = f"Network is down! Error: {e}"
        save_log(error_message)
        return error_message

def get_my_ip():
    try:
        print(f"{Fore.YELLOW}Fetching your IP...{Style.RESET_ALL}")
        response = requests.get("https://api64.ipify.org?format=json").json()
        ip = response["ip"]
        save_log(f"Your IP: {ip}")
        return ip
    except requests.exceptions.RequestException as e:
        error_message = f"Request failed: {e}"
        save_log(error_message)
        return error_message

def get_ip_info(ip):
    try:
        print(f"{Fore.YELLOW}Fetching IP information...{Style.RESET_ALL}")
        response = requests.get(f"http://ip-api.com/json/{ip}")
        
        if response.status_code == 200:
            info = response.json()
            save_log(f"IP Information for {ip}: {info}")
            return info
        else:
            error_message = f"Failed to fetch data! Status code: {response.status_code}"
            save_log(error_message)
            return {"error": error_message}
    except requests.exceptions.RequestException as e:
        error_message = f"Request failed: {e}"
        save_log(error_message)
        return {"error": error_message}

def coords_to_map_link(lat, lon):
    link = f"https://www.google.com/maps?q={lat},{lon}"
    save_log(f"Converted coordinates {lat}, {lon} to link: {link}")
    return link

def map_link_to_coords(link):
    match = re.search(r"q=([-+]?\d*\.\d+|\d+),([-+]?\d*\.\d+|\d+)", link)
    if match:
        coords = match.groups()
        save_log(f"Converted map link to coordinates: {coords}")
        return coords
    error_message = "Invalid link!"
    save_log(error_message)
    return error_message

def loading_message():
    print(f"{Fore.YELLOW}Please wait, fetching data...{Style.RESET_ALL}")
    time.sleep(2) 

def run_option(option):
    if option == "1":
        print(f"\n{check_network_status()}")
    elif option == "2":
        loading_message()
        ip = get_my_ip()
        print(f"\n{Fore.YELLOW}🔹 Your IP: {Fore.GREEN}{ip}")
    elif option == "3":
        ip = input(f"\n{Fore.BLUE}Enter IP: {Style.RESET_ALL}")
        info = get_ip_info(ip)
        print("\n" + Fore.YELLOW + "🔍 IP Information:" + Style.RESET_ALL)
        if "error" in info:
            print(f"{Fore.RED}{info['error']}{Style.RESET_ALL}")
        else:
            for key, value in info.items():
                print(f"{Fore.CYAN}{key}: {Fore.WHITE}{value}")
    elif option == "4":
        lat = input(f"\n{Fore.BLUE}Enter latitude: {Style.RESET_ALL}")
        lon = input(f"{Fore.BLUE}Enter longitude: {Style.RESET_ALL}")
        print(f"\n{Fore.YELLOW}🌍 Google Maps Link: {Fore.GREEN}{coords_to_map_link(lat, lon)}")
    elif option == "5":
        link = input(f"\n{Fore.BLUE}Enter Google Maps link: {Style.RESET_ALL}")
        coords = map_link_to_coords(link)
        print(f"\n{Fore.YELLOW}📍 Coordinates: {Fore.GREEN}{coords}")
    elif option == "6":
        print(f"\n{Fore.RED}Exiting...{Style.RESET_ALL}")
        sys.exit()

while True:
    print(f"\n{Fore.CYAN}╔══════════════════════════════╗")
    print(f"║          {Fore.YELLOW}GeoTool{Fore.CYAN}             ║")
    print(f"╚══════════════════════════════╝{Style.RESET_ALL}")

    print(f"{Fore.GREEN}[1]{Style.RESET_ALL} Check network status")
    print(f"{Fore.GREEN}[2]{Style.RESET_ALL} Get my IP")
    print(f"{Fore.GREEN}[3]{Style.RESET_ALL} Get IP info")
    print(f"{Fore.GREEN}[4]{Style.RESET_ALL} Convert coordinates to map link")
    print(f"{Fore.GREEN}[5]{Style.RESET_ALL} Convert map link to coordinates")
    print(f"{Fore.RED}[6]{Style.RESET_ALL} Exit")

    choice = input(f"\n{Fore.BLUE}Select an option: {Style.RESET_ALL}")

    run_option(choice)
