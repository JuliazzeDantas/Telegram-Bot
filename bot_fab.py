import requests as requests
import json
import datetime
import re
import function 
import token_telegram

TOKEN = token_telegram.get_token()
url = f'https://api.telegram.org/bot{TOKEN}'
message_template_regex = r'^\d+ \d+\.\d{2}$'

product = ''
price = ''
quantity = ''

flag_register = False

def get_updates(url, offset):
    global flag_register, product, price, quantity
    data = requests.get(url + '/getUpdates', params={'offset': offset + 1})
    updates = data.json()
    for update in updates['result']:
        print("---------Novo update---------")
        if flag_register == False:
            if function.verify_message(update): # Verifica se a mensagem é um comando um callback_query
                if function.verify_command(update):
                    function.use_commands(url, update)
                else:
                    print("TEXT: " + function.get_message(update))
                

            elif function.verify_callback_query(update):
                flag_register = True
                product = function.get_callback_query(update)
                function.send_message(url, update, 'Digite a quantidade de produtos comprados e o valor unitário dele. O formato de escrita é assim:\n XXX XX,XX\n\nPrimeiro coloque a quantidade e depois coloque o preço utilizando a vírgula e duas casas decimais sempre')
            else:
                print("Tipo de mensagem inválido")
        else:
            if function.verify_message(update):
                message = function.get_message(update)
                if re.match(message_template_regex, message):
                    message = message.split(' ')
                    quantity = message[0]
                    price = message[1]
                    flag_register = False
                    print("Produto salvo")
                else:
                    function.send_message(url, update, 'Formato invalido! Digite o texto na forma: Quantidade Preço (usando duas casas decimais)')    
            else:
                function.send_message(url, update, 'Envie uma mesnagem comum com o formato requisitado anteriormente')

        print('\n')
        offset = update['update_id'] #Apaga os updates consumidos
    return offset

def main():
    offset = 0
    while True:
        offset = get_updates(url, offset=offset)

if __name__ =='__main__':
    print(function.create_menu_button(url))
    main()