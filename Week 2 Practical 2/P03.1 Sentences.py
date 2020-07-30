'''Sentence Manipulator'''

sentence = input('Enter Sentence: ')
print(sentence.replace(' ', ''))

lower_sentence = list(sentence.lower())

lower_sentence[0] = lower_sentence[0].upper()
for i in range(len(lower_sentence)):
    if lower_sentence[i] == ' ':
        print('go')
        lower_sentence[i+1] = lower_sentence[i+1].upper()

print(''.join(lower_sentence).replace(' ', ''))


sentence1 = list(input('Enter Camel Case Sentence: '))

for i in range(len(sentence1)-1, -1, -1):
    try:
        if sentence1[i+1].isupper():
            sentence1.insert(i+1, ' ')
    except IndexError:
        pass

print(''.join(sentence1))
