# Zadanie 1
def vat_faktura(lista):
    vat = 0.23
    sum_of_items_value = 0.0
    for e in lista:
        sum_of_items_value += e
    return sum_of_items_value * vat


def vat_paragon(lista):
    vat = 0.23
    sum_of_items_value_vat_included = 0.0
    for e in lista:
        sum_of_items_value_vat_included += e * vat
    return sum_of_items_value_vat_included


def test_zad1():
    zakupy = [0.2, 0.5, 4.59, 6]
    print(vat_faktura(zakupy))
    print(vat_paragon(zakupy))
    print(vat_faktura(zakupy) == vat_paragon(zakupy))


# Zadanie 2
denominations = [1, 2, 5, 10, 20, 50, 100, 200]


def give_the_change(amount):
    pairs = []
    while amount > 0:
        biggest = find_biggest(amount)
        denomination_occurrences = amount // biggest
        amount %= biggest
        pairs.append((biggest, denomination_occurrences))
    print_result(pairs)


def print_result(pairs):

    print("Your rest is: ")
    for (denomination, occurrences) in pairs:
        print(str(occurrences) + (" bank notes of value " if denomination >= 10 else (" coins of value " if occurrences > 1 else " coin of value ")) + str(denomination))


def find_biggest(amount):
    max_denomination = 0
    for e in denominations:
        if max_denomination < e <= amount:
            max_denomination = e
    return max_denomination


def test_zad2():
    give_the_change(54694765437604935789)


#Zadanie 4

key = 28


def encode(key, message):
    secret_message = ""
    for c in message:
        secret_message += chr(ord(c) ^ key)
    return secret_message


def decode(key, message):
    return encode(key, message)




