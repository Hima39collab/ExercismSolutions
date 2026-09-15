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

tolerance_values = {'grey' : 0.05,
'violet' : 0.1,
'blue' : 0.25,
'green' : 0.5,
'brown' : 1,
'red' : 2,
'gold' : 5,
'silver' : 10}


def resistor_label(colors):
    if len(colors) == 1:
        first = COLORS.index(colors[0])
        value = 0
        
    if len(colors) == 4:
        first = COLORS.index(colors[0])
        second = COLORS.index(colors[1])
        zeros = COLORS.index(colors[2])
        key = colors[3]
        tolerance = tolerance_values[key]
        value = (first * 10 + second) * (10 ** zeros)
        
    elif len(colors) == 5:
        first = COLORS.index(colors[0])
        second = COLORS.index(colors[1])
        third = COLORS.index(colors[2])
        zeros = COLORS.index(colors[3])
        key = colors[4]
        tolerance = tolerance_values[key]
        value = (first * 100 + second * 10 + third) * (10 ** zeros)

    if value >= 1_000_000_000:
        return f"{value / 1_000_000_000:g} gigaohms ±{tolerance}%"
    elif value >= 1_000_000:
        return f"{value / 1_000_000:g} megaohms ±{tolerance}%"
    elif value >= 1_000:
        return f"{value / 1_000:g} kiloohms ±{tolerance}%"
    elif value == 0:
        return f"{value} ohms"
    else:
        return f"{value} ohms ±{tolerance}%"
