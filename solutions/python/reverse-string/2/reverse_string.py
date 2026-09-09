def reverse(text):    
    reverse_text = ""
    for i in range(len(text),0,-1):
        reverse_text += text[i-(len(text)+1)]
    return reverse_text

#simpler way of doing it

# def reverse(text):
#     return text[::-1]