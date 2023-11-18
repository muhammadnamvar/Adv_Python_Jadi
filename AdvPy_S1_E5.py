sentence = '''The Persian League is the largest sport event dedicated to the deprived areas of Iran.
The Persian League promotes peace and friendship.
This video was captured by one of our heroes who wishes peace.'''

dct = {}
sentence_lst = sentence.split()
print(sentence_lst)

length = len(sentence_lst)
for i in range(1, length):
    if not sentence_lst[i-1].endswith('.'):
        if sentence_lst[i][0].isupper():
            if sentence_lst[i].endswith('.'):
                print(i+1, ': ', sentence_lst[i][0:-1])
            else:
                print(i+1, ': ', sentence_lst[i])


