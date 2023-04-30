import random

def handle_response(message):
    p_message = message.lower()
    
    if p_message == 'hello':
        return 'Hello Jeff and Alex! I am MunchLax Bot! Here to Lick, Tackle, and sleep!'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return "`This is a help message!`"

