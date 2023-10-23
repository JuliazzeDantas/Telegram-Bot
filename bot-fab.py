TOKEN = '6827779420:AAEDNCElxoBCLdkF8mBC2U5DtO5enpDZd8U'

import requests as requests
import json
import function 

def main():
    url = f'https://api.telegram.org/bot{TOKEN}'
    offset = 0
    while True:
        function.get_updates(offset)

if __name__ =='__main__':
    print(function.create_menu_button())
    main()