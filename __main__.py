from pathlib import Path
from re import search
import threading

def count_words():
    hashmap = {}
    with open('temp.txt', 'r') as reader:
        for line in reader:
            word, value = line.split()
            if word not in hashmap: hashmap[word] = []
            hashmap[word].append(value)
    hashmapsorted = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
    return hashmapsorted

def map(file):
    if file.name.startswith("aux") == False: return
    with open('temp.txt', 'a') as writer:
        with open(file, 'r') as reader:
            for line in reader:
                for word in line.split():
                    if search(regex, word):
                        writer.write(f'{word} 1\n')

def reduce(word, occurrences):
    freq = len(occurrences)
    print(f'{word} | number of occurrences: {freq}')

if __name__ == '__main__':
    regex = input('Informe qual regex deseja usar: ')

    files = Path('./').glob('*')
    for file in files:
        tr = threading.Thread(target=map, args=[file])
        tr.start()
        tr.join()
    
    d = count_words()
    for word in d:
        tr = threading.Thread(target=reduce, args=[word, d[word]])
        tr.start()
        tr.join()

# [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
