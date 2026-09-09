def reverse(text):    
    reverse = ""
    for i in range(len(text),0,-1):
        reverse += text[i-(len(text)+1)]
    return reverse

#simpler way of doing it

def reverse(text):
    return text[::-1]