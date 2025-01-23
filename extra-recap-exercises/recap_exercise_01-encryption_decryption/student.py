def decode1(word):
    result = ''
    for c in word:
        if c == 'A':
            result += 'o'
        else:
            result += c
    return result

def decode2(word):
    result = ''
    result += word[::2]
        
    return result

def decode3(sentence):
    result = ''
    
    words = sentence.split()
    words[0] = words[0][::-1]

    result = ' '.join(words)

    return result

def decode4(word):
    i = len(word) // 2
    return word[2:i+2]

def decode5(sentence):
    sentence = decode3(sentence)
    words = sentence.split()
    result = []

    for word in words:
        word = decode4(word)
        word = decode2(word)
        word = decode1(word)
        result.append(word)

    return ' '.join(result)

print(decode5("NBFOeWdu XfPAkkagtkzm CaxIkkrGaNprtOGYQszl fhmbdYeI YndYkdrUAVlLlqecnSZJQpxiklmJ"))