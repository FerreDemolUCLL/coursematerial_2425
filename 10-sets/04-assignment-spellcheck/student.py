def spellcheck(document, valid_words):
    result = set()
    valid_words_set = set(valid_words)
    
    words = document.lower().split()
    for word in words:
        if word not in valid_words_set:
            result.add(word)
    
    return result