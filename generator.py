import os
import random

class InstanceGenerator:
    def __init__(self, split, n, alphabet, min_size, max_size):
        self.split = split
        self.n = n
        self.alphabet = alphabet
        self.min_size = min_size
        self.max_size = max_size

    def generate_instances(self, output_dir):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Gera palavras aleatórias e as divide em arquivos
        words = self.generate_random_words()
        chunk_size = len(words) // self.split

        for i in range(self.split):
            chunk_words = words[i*chunk_size : (i+1)*chunk_size]
            file_name = f'instance_{i+1}.txt'
            with open(os.path.join(output_dir, file_name), 'w') as writer:
                writer.write(' '.join(chunk_words))

    def generate_random_words(self):
        words = []
        for _ in range(self.n):
            size = random.randint(self.min_size, self.max_size)
            word = ''.join(random.choice(self.alphabet) for _ in range(size))
            words.append(word)
        return words

if __name__ == "__main__":
    instance_generator = InstanceGenerator(
        split = 3,
        n = 10,
        alphabet = ['a', 'b', 'c', 'd', 'e'],
        min_size = 3,
        max_size = 6
    )

    # diretório onde as instancias serão gerados
    dir = './'
    instance_generator.generate_instances(dir)