import json


def strip_request(message):
    return message.text.lower() \
        .replace('!', '') \
        .replace('.', '') \
        .replace(',', '') \
        .replace('?', '') \
        .strip()

def is_hello_request(message):
    print(f"User: {message.from_user.full_name}({message.from_user.id}). Message: {message.text}" )

    return strip_request(message) in [
        'start', 
        'hi', 
        'hello', 
        'привет', 'приветик', 'приветище', 
        'здрасте', 'здравствуй', 'здравствуйте', 'здарова', 'здароф', 'здаров',
        'дратуте', 
        'салют',
        'хай','хаюшки',
        'как дела', 'как твои дела',
        'куку'
        ]


def is_order_callback(call):
    callback_data = json.loads(call.data)
    if callback_data.get('op', None) == 'order':
        return True
    
    return False
