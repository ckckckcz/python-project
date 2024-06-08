with open("cerita.txt", "r") as f:
    cerita = f.read()

words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(cerita):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = cerita[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

answers = {}

for word in words:
    answer = input("Masukkan sebuah kata " + word + ": ")
    answers[word] = answer

for word in words:
    cerita = cerita.replace(word, answers[word])

print(cerita)