import random
import string

def generate_readable_nickname(n):
    words = ["Sky", "Fire", "Ice", "Wind", "Earth", "Shadow", "Light", "Water", "Storm", "Star"]
    nicknames = []
    for _ in range(n):
        word = random.choice(words)
        number = str(random.randint(1, 99))
        nickname = word + number
        nicknames.append(nickname)
    return nicknames

def save_nicknames_to_file(nicknames, filename):
    with open(filename, 'w') as file:
        for nickname in nicknames:
            file.write(nickname + '\n')

# Генерируем 100 никнеймов
nicknames = generate_readable_nickname(100)
# Сохраняем никнеймы в файл (пример для локального использования: 'nicknames.txt')
filename = 'nicknames.txt'
save_nicknames_to_file(nicknames, filename)

print(f"Nicknames saved to {filename}")

#сделать так, чтобы числа использовались только 2/4/69 типа 2- ту, 4 - фор игра слов и добавить схему слово-цифра-слово или слово-слово-цифра