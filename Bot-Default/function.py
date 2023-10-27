import requests as requests
import json

############################# CREATE ITENS ######################################

def create_menu_button(url, menuButton): 
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


def create_inline_keyboard(url, inlineKeyboard, chat_id, text):
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
    
#####################################################################################

############################# GET INFORMATIONS ######################################

def get_type_of_message(function):
    def verify_edited(message):
        if 'edited_message' in message:
            return function(message['edited_message'])
        elif 'message' in message:
            return function(message['message'])
        elif 'callback_query' in message:
            return function(message['callback_query']['message'])
        else:
            print("ERRO - Tipo de mensagem não esperada")
            return function(message)
    return verify_edited

    
@get_type_of_message
def get_text(message_received):
    return message_received['text']
    

@get_type_of_message
def get_sender(message_received):
    return message_received['from']['id']


@get_type_of_message
def is_bot(message_received):
    return message_received['from']['is_bot']
    

@get_type_of_message
def get_user_name(message_received):
    return message_received['from']['first_name']
    

@get_type_of_message
def get_user_last_name(message_received):
    return message_received['from']['last_name']


@get_type_of_message
def get_group_name(message_received):
    return message_received['chat']['title']


@get_type_of_message
def get_chat_id(message_received):
    return message_received['chat']['id']
    
@get_type_of_message
def get_chat_type(message_received):
    return message_received['chat']['type']


@get_type_of_message
def get_message_id(message_received):
    return message_received['message_id']


def get_callback_query(message_received):
    return message_received['callback_query']['data']

@get_type_of_message
def get_photo_id(message_received):
    return message_received['photo'][0]['file_id']

##################################################################################

############################# VERIFIERS ######################################
    
@get_type_of_message
def verify_command(message_received):
    if 'entities' in message_received:
        return True
    else:
        return False

def verify_message(message_received):
    if ('message' in message_received) or ('edited_message' in message_received):
        return True
    else:
        return False
    
def verify_callback_query(message_received):
    if 'callback_query' in message_received:
        return True
    else:
        return False

@get_type_of_message
def verify_photo(message_received):
    if 'photo' in message_received:
        return True
    else:
        return False
    
##################################################################################

############################# SEND MESSAGES ######################################

def send_photo(url,chat_id ,photo_id ,caption):
    data = {
        'chat_id': chat_id, 
        "photo": photo_id,
        'caption': caption
    }

    response = requests.post(url + '/sendPhoto', data)
    return response.status_code


def send_message(url, chat_id, message_sent):
    data = {
        'chat_id': chat_id, 
        'text': message_sent
    }

    response = requests.post(url + '/sendMessage', data)
    return response.status_code


def reply_message(url, message_received, message_sent):
    data = {
        'chat_id': get_chat_id(message_received), 
        "reply_to_message_id" : get_message_id(message_received),
        'text' : message_sent
    }

    response = requests.post(url + '/sendMessage', data)
    return response.status_code

#####################################################################################

############################# FORWARD MESSAGES ######################################

def forward_message(url, chat_id, from_chat_id, message_id, text):
    data = {'chat_id' : chat_id, 
    'from_chat_id' : from_chat_id,
    'message_id' : message_id,
    }
    
    response = requests.post(url + '/forwardMessage', data)
    return response.status_code




data = requests.get('https://api.telegram.org/bot6827779420:AAEDNCElxoBCLdkF8mBC2U5DtO5enpDZd8U' + '/getUpdates')
updates = data.json()
print(updates)
for update in updates['result']:
    print("OK")
    print(get_photo_id(update))