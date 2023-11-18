n = int(input("Please enter number of translate: "))
dict_en = {}
dict_fr = {}
dict_gr = {}
dictionary = [dict_en, dict_fr, dict_gr]
for i in range(n):
    lst = input(f"Please enter {i+1}'st word and it's translates: ").split()
    dict_en.update({lst[1]: lst[0]})
    dict_fr.update({lst[2]: lst[0]})
    dict_gr.update({lst[3]: lst[0]})

print(dictionary)
sen = input("Please enter your sentence: ")


def lang_detector(sentence, dict_en, dict_fr, dict_gr):
    for word in sentence.split():
        if word in dict_en:
            return 0
        elif word in dict_fr:
            return 1
        elif word in dict_gr:
            return 2


def translator(dict, str):
    translated_str = ""
    for word in str.split():
        translated_str += dict.get(word, word) + ' '
    return translated_str.strip()


lang = lang_detector(sen, dict_en, dict_fr, dict_gr)
print(translator(dictionary[lang], sen))
