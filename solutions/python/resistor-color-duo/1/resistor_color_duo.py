COLORS = ["black",
"brown",
"red",
"orange",
"yellow",
"green",
"blue",
"violet",
"grey",
"white"]

def value(colors):
    result = ""
    for color in colors[:2]:
        result += str(COLORS.index(color))
    return int(result)  
