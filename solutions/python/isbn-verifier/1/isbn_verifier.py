def is_valid(isbn):

    isbn = isbn.replace("-", "")

    if len(isbn) != 10:
        return False

    isbn_formula = 0

    for i in range(10):
        if isbn[i] == "X":
            if i != 9:
                return False
            value = 10

        elif isbn[i].isdigit():
            value = int(isbn[i])

        else:
            return False

        isbn_formula += value * (10-i)
    return isbn_formula % 11 == 0










