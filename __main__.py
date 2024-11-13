from pathlib import Path
from re import search
import threading

def count_lines():
    hashmap = {}
    with open('temp.txt', 'r') as reader:
        for line in reader:
            if line not in hashmap: hashmap[line] = []
            hashmap[line].append(1)
    hashmapsorted = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
    return hashmapsorted

def map(file):
    if file.name.startswith("instance") == False: return
    with open('temp.txt', 'a') as writer:
        with open(file, 'r') as reader:
            for line in reader:
                ok = False
                for word in line.split():
                    if search(regex, word):
                        ok = True
                if ok == True:
                    writer.write(f'{line}\n')

def reduce(line, occurrences):
    freq = len(occurrences)
    with open('ans.txt', 'a') as writer:
        writer.write(f'{line}')

if __name__ == '__main__':
    regex = input('Informe qual regex deseja usar: ')

    # limpando arquivo temp.txt
    with open('temp.txt', 'w') as writer:
        writer.write('')

    # limpando arquivo ans.txt
    with open('ans.txt', 'w') as writer:
        writer.write('')

    files = Path('./').glob('*')
    for file in files:
        tr = threading.Thread(target=map, args=[file])
        tr.start()
        tr.join()
    
    d = count_lines()
    for word in d:
        tr = threading.Thread(target=reduce, args=[word, d[word]])
        tr.start()
        tr.join()

# [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
