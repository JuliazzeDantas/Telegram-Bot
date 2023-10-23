import requests as requests
import json
import function 
import token

def main():
    TOKEN = token.get_token()
    url = f'https://api.telegram.org/bot{TOKEN}'
    offset = 0
    while True:
        function.get_updates(offset)

if __name__ =='__main__':
    print(function.create_menu_button())
    main()