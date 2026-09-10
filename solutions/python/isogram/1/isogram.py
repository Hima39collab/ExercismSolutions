def is_isogram(phrase):
    phrase_words = []
    for item in phrase.lower():
        if item == " " or item == "-":
            continue
        if item in phrase_words:
            return False
        else:
            phrase_words.append(item)
        
    return True