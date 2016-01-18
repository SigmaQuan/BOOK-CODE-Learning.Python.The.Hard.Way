
class ParserError(Exception):
    pass

class Sentence(object):
    def __init__(self, subject, verb, obj):
        # remember we take ('non', 'princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb
        self.obj = obj


def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

