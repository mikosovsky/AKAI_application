# coding=utf-8

# input: array with multiple strings
# expected output: rank of the 3 most often repeated words in given set of strings and number of times they occured, case insensitive

sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]

# Example result:
# 1. "mam" - 12
# 2. "tak" - 5
# 3. "z" - 2


# Good luck! You can write all the code in this file.
words = {}


def clear_sentence(sentence):
    sentence_without_dots = sentence.replace(".", "")
    sentence_without_commas_and_dots = sentence_without_dots.replace(",", "")
    sentence_without_punctuation = sentence_without_commas_and_dots.replace("?", "")
    sentence_lower_signs = sentence_without_punctuation.lower()
    return sentence_lower_signs


for sentence in sentences:
    cleared_sentence = clear_sentence(sentence)
    split_sentence = cleared_sentence.split()
    for word in split_sentence:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

sorted_words = sorted(words.items(), key=lambda x: x[1])
sorted_words.reverse()

for i in range(3):
    print(f"{i + 1}. \"{sorted_words[i][0]}\" - {sorted_words[i][1]}")