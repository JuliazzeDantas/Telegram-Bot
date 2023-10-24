import requests as requests
import json
from where_is_my_lists import MenuButton, InlineKeyboard

menuButton = MenuButton()
inlineKeyboard = InlineKeyboard()

def create_menu_button(url): 
    menu = menuButton.menu_button
    data = {
        "commands" : json.dumps(menu)
    }
    response = requests.post(url + '/setMyCommands', data = data)
    
    if response.status_code == 200:
        print("MenuButton criado com sucesso")
        return True
    else:
        print("Erro na criação do MenuButton")
        return False


def create_inline_keyboard(url, buttons, chat_id, text):
    keyboard = json.dumps(
        {
            "inline_keyboard": buttons
        }
    )

    params = {
        'chat_id': chat_id,
        'text' : text,
        'reply_markup': keyboard
    }

    response = requests.post(url + '/sendMessage', params)

    if response.status_code == 200:
        print("InlineKeyboard criado com sucesso")
        return True
    else:
        print("Erro na criação do InlineKeyboard")
        return False


def get_message(message_received):
    try:
        return message_received['message']['text']
    except KeyError:
        return message_received['edited_message']['text']


def get_chat_id(message_received):
    if ('message' in message_received):
        return message_received['message']['chat']['id']
    elif ('edited_message' in message_received):
        return message_received['edited_message']['chat']['id']


def get_message_id(message_received):
    try:
        return message_received['message']['message_id']
    except KeyError:
        return message_received['edited_message']['message_id']


def get_callback_query(message_received):
    print("Callback query enviado")
    return message_received['callback_query']['data']


def send_message(url, message_received, message_sent):
    data = {
        'chat_id': get_chat_id(message_received), 
        'text': message_sent
    }

    requests.post(url + '/sendMessage', data)


def reply_message(url, message_received, message_sent):

    print("/////////////////////////////////////////")
    print(message_received)
    data = {
        'chat_id': get_chat_id(message_received), 
        "reply_to_message_id" : get_message_id(message_received),
        'text' : message_sent
    }

    requests.post(url + '/sendMessage', data)


def verify_message(message_received):
    if ('message' in message_received) or ('edited_message' in message_received):
        return True
    else:
        return False


def verify_command(message_received):
    if ('message' in message_received):
        if 'entities' in message_received['message']:
            return True
        else:
            return False
    elif ('edited_message' in message_received):
        if 'entities' in message_received['edited_message']:
            return True
        else:
            return False

    
def verify_callback_query(message_received):
    if 'callback_query' in message_received:
        return True
    else:
        return False


def use_commands(url, command):
    print("Comando detectado")
    list_command = menuButton.list_of_command

    if get_message(command) == list_command[0]:
        send_message(url, command, "Esse Bot irá auxiliá-lo a gerir as contas da empresa. Farei isso salvando todas as mercadorias que você compra!\n\n\
                     Ao escolher um dos grupos de produtos, aparecerá em sua tela várias opções de produtos. Escolha um deles e depois digite o preço e a quantidade comprada.")
        
    if get_message(command) == list_command[1]:
        comun_list = inlineKeyboard.comun_product
        chat_id= get_chat_id(command)
        print(create_inline_keyboard(url, comun_list, chat_id, 'Escolha uma das opções de produto para cadastrar'))

    if get_message(command) == list_command[2]:
        gourmet_list = inlineKeyboard.gourmet_product
        chat_id= get_chat_id(command)
        print(create_inline_keyboard(url, gourmet_list, chat_id, 'Escolha uma das opções de produto para cadastrar'))

    if get_message(command) == list_command[3]:
        drinks_list = inlineKeyboard.drink_product
        chat_id= get_chat_id(command)
        print(create_inline_keyboard(url, drinks_list, chat_id, 'Escolha uma das opções de produto para cadastrar'))

    if get_message(command) == list_command[4]:
        pizza_dough_list = inlineKeyboard.pizza_dough_list
        chat_id= get_chat_id(command)
        print(create_inline_keyboard(url, pizza_dough_list, chat_id, 'Escolha uma das opções de produto para cadastrar'))
        
    if get_message(command) == list_command[5]:
        structure_list = inlineKeyboard.structure_list
        chat_id= get_chat_id(command)
        print(create_inline_keyboard(url, structure_list, chat_id, 'Escolha uma das opções de produto para cadastrar'))

    if get_message(command) == list_command[6]:
        print("função não implementada")
        chat_id= get_chat_id(command)
        #print(create_inline_keyboard('', chat_id, 'Escolha uma das opções de produto para cadastrar'))
