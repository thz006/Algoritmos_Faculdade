import random
def embaralhar_string(s):
    s = list(s)
    random.shuffle(s)
    return ''.join(s)