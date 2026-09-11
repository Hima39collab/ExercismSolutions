def rotate(text, key):

    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    new_text = ""

    for item in text:

        if item in lowercase:
            position = lowercase.index(item)
            new_position = (position + key) % 26
            new_text += lowercase[new_position]

        elif item in uppercase:
            position = uppercase.index(item)
            new_position = (position + key) % 26
            new_text += uppercase[new_position]

        else:
            new_text += item

    return new_text





 
        
