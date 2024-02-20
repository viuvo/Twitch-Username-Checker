import asyncio
import aiohttp
import random
import string
import threading
import colorama
import json

with open("settings.json") as f:
    jso1 = json.load(f)

async def checkuser():
    async with aiohttp.ClientSession() as session:
        with open('settings.json') as f:
            r = json.load(f)
        r = r["letters"]
        if r == 4:
            username = ''.join(random.choices(string.ascii_lowercase+string.digits,k=4))
        elif r == 5:
            username = ''.join(random.choices(string.ascii_lowercase+string.digits,k=5))
        else:
            username = ''.join(random.choices(string.ascii_lowercase+string.digits,k=r))
        if r> 3 and r <= 5:
            headers = {
                'Accept': '*/*',
                'Accept-Language': 'en-US',
                'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
                'Client-Session-Id': 'cab427f35656d6c4',
                'Client-Version': '121dfb28-b6c3-48e2-8a3b-588128a7fae5',
                'Connection': 'keep-alive',
                'Content-Type': 'text/plain;charset=UTF-8',
                'Origin': 'https://www.youtube.com/@',
                'Referer': 'https://www.youtube.com/@',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

            data = '{"operationName":"UsernameValidator_User","variables":{"username":"'+username+'"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"fd1085cf8350e309b725cf8ca91cd90cac03909a3edeeedbd0872ac912f3d660"}}}'
            async with session.post('https://gql.twitch.tv/gql', headers=headers, data=data) as response:
                r = await response.json()
                r1 = r["data"]["isUsernameAvailable"]
                return r1, username
        else:
            print(f'{colorama.Fore.RED}Invalid setting.{colorama.Fore.RESET}')
            return None

def startniggers():
    r1 = asyncio.run(checkuser())
    if r1 == None:
        None
    elif r1[0] == True:
        re = open('available.txt', 'r').read().splitlines()
        if r1[1] not in re:
            print(f'[{colorama.Fore.CYAN}+{colorama.Fore.RESET}] Got username: {colorama.Fore.CYAN}{r1[1]}{colorama.Fore.RESET}')
            with open('available.txt', 'a') as writer:
                writer.write(f"{r1[1]}\n")
        else:
            print(f'[{colorama.Fore.GREEN}/{colorama.Fore.RESET}] Already generated: {colorama.Fore.GREEN}{r1[1]}{colorama.Fore.RESET}')
    elif r1[0] == False:
        print(f'[{colorama.Fore.RED}-{colorama.Fore.RESET}] Not available.')
    else:
        print(f'[{colorama.Fore.GREEN}/{colorama.Fore.RESET}] Something went wrong.. Try again after few minutes.')

def startniggers1():
    while True:
        startniggers()


for i in range(int(jso1["threads"])):
    startniggers1()