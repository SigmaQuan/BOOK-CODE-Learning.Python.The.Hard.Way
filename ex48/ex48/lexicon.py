#
direction = {
    'north': '',
    'south': '',
    'west': '',
    'east': '',
    'down': '',
    'up': '',
    'left': '',
    'right': '',
    'back': ''
}

verb = {
    'go': '',
    'stop': '',
    'kill': '',
    'eat': ''
}

stop = {
    'the': '',
    'in': '',
    'of': '',
    'from': '',
    'at': '',
    'it': ''
}

noun = {
    'door': '',
    'bear': '',
    'princess': '',
    'cabinet': ''
}

def is_number(word):
    try:
        number = int(word)
        return True
    except:
        return False


def get_word_type(word):
    if direction.has_key(word):
        return ('direction', word)
    elif verb.has_key(word):
        return ('verb', word)
    elif stop.has_key(word):
        return ('stop', word)
    elif noun.has_key(word):
        return ('noun', word)
    elif is_number(word):
        return ('number', int(word))
    else:
        return ('error', word)


def scan(sentence):
    words = sentence.split()
    results = []
    for word in words:
        results.append(get_word_type(word))

    return results
