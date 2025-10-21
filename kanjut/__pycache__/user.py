import os
import requests
import random
from bs4 import BeautifulSoup

def generate_and_save_user_agents():
    BASE_URL = "https://whatmyuseragent.com"
    BRAND_LIST = ['xi/xiaomi', 'if/infinix', 'tb/tecno-mobile', 'sa/samsung', 'op/oppo']
    print('sedang create user agent')
    def get_random_device_user_agent(session, brand):
        BRAND_URL = f"{BASE_URL}/brand/{brand}"
        try:
            response = session.get(BRAND_URL)
            response.raise_for_status()
        except requests.RequestException as e:
            print("Gagal mengakses halaman:", e)
            return None

        soup = BeautifulSoup(response.text, "html.parser")
        devices = []
        device_links = []

        for link in soup.find_all("a"):
            href = link.get("href", "")
            if "/device/" in href:
                device_name = link.get_text(strip=True)
                if device_name and device_name not in devices:
                    devices.append(device_name)
                    device_links.append(href)

        if not devices:
            print("Tidak ditemukan daftar device pada halaman tersebut untuk brand", brand)
            return None

        random_index = random.randint(0, len(devices) - 1)
        device_url = BASE_URL + device_links[random_index]

        try:
            response_device = session.get(device_url)
            response_device.raise_for_status()
        except requests.RequestException as e:
            print("Gagal mengakses halaman device:", e)
            return None

        soup_device = BeautifulSoup(response_device.text, "html.parser")
        user_agents = [tag.get_text(strip=True) for tag in soup_device.find_all("td", class_="useragent")]

        if user_agents:
            return random.choice(user_agents)
        else:
            print("Tidak ditemukan user agent pada halaman device tersebut.")
            return None

    user_agents_list = []
    with requests.Session() as session:
        for i in range(5):
            brand = random.choice(BRAND_LIST)
            ua = get_random_device_user_agent(session, brand)
            if ua:
                print(ua)
                user_agents_list.append(ua)
            else:
                fallback = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Mobile Safari/537.36"
                print(fallback)
                user_agents_list.append(fallback)
    
    with open("user.txt", "w", encoding="utf-8") as file:
        for ua in user_agents_list:
            file.write(ua + "\n")
