sentences = input()
sentences = sentences.lower()
letter = input()
count = 0

for i in range(len(sentences)):
    if sentences[i] == letter:
        count += 1
print(count)
