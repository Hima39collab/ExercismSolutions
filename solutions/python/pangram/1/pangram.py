def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for item in alphabet:
        if item not in sentence.lower():
            return False
    return True
