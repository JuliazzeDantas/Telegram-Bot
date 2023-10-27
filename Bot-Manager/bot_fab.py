import requests as requests
import json
import datetime
import re
import function 
import token_telegram

message_template_regex_I = r'^\d+ \d+\,\d{2}$'
message_template_regex_II = r'^\d+ \d+\,\d{1}$'
message_template_regex_III = r'^\d+ \d+$'

product = ''
price = ''
quantity = ''

flag_register = False

def select_product(url, update):
    global flag_register, product, price, quantity
    if function.verify_message(update): # Verifica se a mensagem é um comando ou um callback_query
        if function.verify_command(update) == True:
            function.use_commands(url, update)
        else:
            print("Comando não identificado ou Texto comum")

    elif function.verify_callback_query(update):
        flag_register = True
        product = function.get_callback_query(update)
        function.send_message(url, function.get_chat_id(update), 'Digite a quantidade de produtos comprados e o valor unitário dele. O formato de escrita é assim:\n XXX XX,XX\n\nPrimeiro coloque a quantidade e depois coloque o preço')
    else:
        print("Tipo de mensagem inválido")


def save_product(url, update):
    global flag_register
    if function.verify_message(update):
        message = function.get_text(update)
        print(message)
        if re.match(message_template_regex_I, message) or re.match(message_template_regex_II, message) or re.match(message_template_regex_III, message):
            message = message.split(' ')
            quantity = int(message[0])
            price = float(message[1].replace(',', '.'))
            flag_register = False
            function.send_message(url, function.get_chat_id(update), f'Produto Salvo: {quantity} unidades de {product} por {price:.2f}')
            print("Produto salvo")
        else:
            function.send_message(url, function.get_chat_id(update), 'Formato invalido! Digite o texto na forma: Quantidade Preço')    
    else:
        function.send_message(url, function.get_chat_id(update), 'Envie uma mesnagem comum com o formato requisitado anteriormente')


def get_updates(url, offset):
    global flag_register, product, price, quantity
    data = requests.get(url + '/getUpdates', params={'offset': offset + 1})
    updates = data.json()
    for update in updates['result']:
        print(f"FLAG - {flag_register}")
        print("---------Novo update---------")
        if flag_register == False:
            select_product(url, update)
        else:
            save_product(url, update)
        offset = update['update_id'] #Apaga os updates consumidos
    return offset

def main():
    offset = 0
    while True:
        offset = get_updates(url, offset=offset)

if __name__ =='__main__':
    TOKEN = token_telegram.get_token()
    url = f'https://api.telegram.org/bot{TOKEN}'
    print(function.create_menu_button(url))
    main()