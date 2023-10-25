sentence = input()
sentence_stack = []
reverse_sentence = ''

for chr in sentence:
    sentence_stack += chr

while True:
    if len(sentence_stack) <= 0:
        break
    else:
        reverse_sentence += sentence_stack.pop()

print(reverse_sentence)