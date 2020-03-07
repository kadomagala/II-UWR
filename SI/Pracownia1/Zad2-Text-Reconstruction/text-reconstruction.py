import queue

pan_tadeusz = "księgapierwsza \
gospodarstwo \
powrótpaniczaspotkaniesiępierwszewpokoikudrugieustołuważnasędziegonaukaogrzecznościpodkomorzegouwagipolitycznenadmodamipocząteksporuokusegoisokołażalewojskiegoostatniwoźnytrybunałurzutokanaówczesnystanpolitycznylitwyieuropy \
litwoojczyznomojatyjesteśjakzdrowie \
ileciętrzebacenićtentylkosiędowie \
ktocięstraciłdziśpięknośćtwąwcałejozdobie \
widzęiopisujębotęskniępotobie \
pannoświętacojasnejbroniszczęstochowy \
iwostrejświeciszbramietycogródzamkowy \
nowogródzkiochraniaszzjegowiernymludem \
jakmniedzieckodozdrowiapowróciłaścudem \
gdyodpłaczącejmatkipodtwojąopiekę \
ofiarowanymartwąpodniosłempowiekę \
izarazmogłempieszodotwychświątyńprogu \
iśćzawróconeżyciepodziękowaćbogu"


def sum_of_squares(words):
    s = 0
    for w in words:
        s += len(w) * len(w)
    return s


def load_words_set():
    words_set = set()
    with open('words_for_ai1.txt') as f:
        for line in f:
            words_set.add(line.rstrip('\n'))

    return words_set


POLISH_WORDS = load_words_set()


# Generate all possible pairs (my_word, rest) from string word such that my_word exists in POLISH_WORDS
# and my_word + rest = word
def gen_word_and_rest(word):
    my_word = ""
    for i in range(0, len(word)):
        if my_word + word[i] in POLISH_WORDS:
            yield my_word + word[i], word[i+1:]
        my_word += word[i]


def find_max(word):
    current_max = []
    current_max_sum = 0
    pending = queue.Queue()

    for i in gen_word_and_rest(word):
        pending.put(([i[0]], i[1]))
    while not pending.empty():
        state = pending.get()
        if state[1] == "":
            print(state[0])
            candidate_sum = sum_of_squares(state[0])
            if candidate_sum > current_max_sum:
                current_max = state[0]
                current_max_sum = candidate_sum
        else:
            for i in gen_word_and_rest(state[1]):
                new_ls_words = state[0].copy()
                new_ls_words.append(i[0])
                new_state = (new_ls_words, i[1])
                pending.put(new_state)

    result = ""
    for i in range(0, len(current_max) - 1):
        result += current_max[i] + ' '
    result += current_max[len(current_max)-1]
    return result


print(find_max("powrótpaniczaspotkaniesiępierwszewpokoikudrugieustołuważnasędziegonaukaogrzecznościpodkomorzego"))
