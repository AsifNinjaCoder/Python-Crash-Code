directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right']
verbs = ['go', 'stop', 'kill', 'eat']
stop_works = ['the', 'in', 'of', 'from', 'at', 'it']
nouns = ['door', 'bear', 'princess', 'cabinet']

def scan(input):
    words = input.split()
    operation = ''
    sentence = []

    for word in words:
        if word in directions:
            operation = 'direction'
        elif word in verbs:
            operation = 'verb'
        elif word in stop_works:
            operation = 'stop'
        elif word in nouns:
            operation = 'noun'
        elif convert_number(word):
            operation = 'number'
            word = convert_number(word)
        else:
            operation = 'error'

        sentence.append((operation, word))

    return sentence

def convert_number(word):
    try:
        return int(word)
    except ValueError:
        return None