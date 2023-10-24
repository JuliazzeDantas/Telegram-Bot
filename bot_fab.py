import requests as requests
import json
import function 
import token_telegram

TOKEN = token_telegram.get_token()
url = f'https://api.telegram.org/bot{TOKEN}'

def main():
    offset = 0
    while True:
        offset = function.get_updates(url, offset=offset)

if __name__ =='__main__':
    print(function.create_menu_button(url))
    main()