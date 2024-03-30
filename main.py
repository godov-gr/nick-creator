import random
import string

def generate_readable_nickname(n):
    nouns = ["sky", "fire", "ice", "wind", "earth", "shadow", "light", "water", "storm", "star", "bolt", "wolf", "rabbit", "wild", "demon", "hunter", "soul", "nut", "light", "darkness", "deep"
             , "rider", "dream", "men", "dog", "cat", "elf", "troll", "baby", "frog", "god", "mrak", "smoke", "drink", "next", "sniper", "dragon", "spirit", "beast", "doctor", "force", 
             "mad", "missle", "ghoul", "dude", "bird", "bro", "eye", "face", "hand", "king", "lion", "life", "person", "piece", "place", "rock", "ship", "sound", "state"]
    adjectives = ["sky", "fire", "ice", "wind", "earth", "shadow", "light", "water", "critical", "star", "agressive", "bad", "additional", "blue", "black", "red", "white", "hard", "light", "cool", "cold", "alive", 
                  "angry", "crazy", "basic", "boring", "central", "clear", "common", "curious", "current", "dark", "deep", "dead", "desperate", "early", "easy", "every", "final", "free", "freedom",
                   "general", "global", "great", "high", "hot", "huge", "impressive", "large", "late", "little", "local", "lucky", "main", "mantal", "military", "old", "hyper"]
    cool_numbers = ["13", "69", "228", "420", "666", "777", "911", ]
    nicknames = []
    for _ in range(n):
        noun = random.choice(nouns)
        cool_number = random.choice(cool_numbers)
        adjective = random.choice(adjectives)
        nickname = adjective + noun + cool_number
        nicknames.append(nickname)
    return nicknames

def save_nicknames_to_file(nicknames, filename):
    with open(filename, 'w') as file:
        for nickname in nicknames:
            file.write(nickname + '\n')

# Генерируем 100 никнеймов
nicknames = generate_readable_nickname(100)
# Сохраняем никнеймы в файл
filename = 'nicknames.txt'
save_nicknames_to_file(nicknames, filename)

print(f"Nicknames saved to {filename}")
