import random


def simplify_sentence(sentence, word_length, word_count):
    words = sentence.split()
    words = list(filter(lambda word: len(word) <= word_length, words))
    length = len(words)
    while length > word_count:
        i = random.randrange(length)
        words.pop(i)
        length -= 1

    result = ""
    for word in words:
        result += word + " "
    return result


tekst = "Podział peryklinalny inicjałów wrzecionowatych \
        kambium charakteryzuje się ścianą podziałową inicjowaną \
        w płaszczyźnie maksymalnej."

inwokacja = "Litwo! Ojczyzno moja! ty jesteś jak zdrowie.\n \
Ile cię trzeba cenić, ten tylko się dowie,\n\
Kto cię stracił. Dziś piękność twą w całej ozdobie\n\
Widzę i opisuję, bo tęsknię po tobie.\n\
Panno Święta, co Jasnej bronisz \n\
I w Ostrej świecisz Bramie! Ty, co gród zamkowy\n\
Nowogródzki ochraniasz z jego wiernym ludem!\n\
Jak mnie dziecko do zdrowia powróciłaś cudem\n\
(Gdy od płaczącej matki pod Twoję opiekę\n\
Ofiarowany, martwą podniosłem powiekę\n\
I zaraz mogłem pieszo do Twych świątyń progu\n\
Iść za wrócone życie podziękować Bogu),\n\
Tak nas powrócisz cudem na Ojczyzny łono.\n\
Tymczasem przenoś moję duszę utęsknioną\n\
Do tych pagórków leśnych, do tych łąk zielonych,\n\
Szeroko nad błękitnym Niemnem rozciągnionych;\n\
Do tych pól malowanych zbożem rozmaitem,\n\
Wyzłacanych pszenicą, posrebrzanych żytem;\n\
Gdzie bursztynowy świerzop, gryka jak śnieg biała,\n\
Gdzie panieńskim rumieńcem dzięcielina pała,\n\
A wszystko przepasane, jakby wstęgą, miedzą\n\
Zieloną, na niej z rzadka ciche grusze siedzą."
#print(simplify_sentence(inwokacja, 10, 30))


def compress(word):
    prev = word[0]
    num = 1
    result = ""
    for i in range(1, len(word)):
        if word[i] == prev:
            num += 1
        else:
            if num > 1:
                result += str(num) + prev
            else:
                result += prev
            prev = word[i]
            num = 1
    return result


def decompress(word):
    result = ""
    num = ""
    for i in range(0, len(word)):
        if word[i].isdigit():
            num += word[i]
        else:
            if num != "":
                num = int(num)
                while num > 0:
                    result += word[i]
                    num -= 1
                num = ""
            else:
                result += word[i]
    return result


#print(decompress("35asdasda"))
#print(compress("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasdasda"))
