import time

from api import app, trie


if __name__ == '__main__':
    start = time.perf_counter()
    with open('data/6500titles.csv', 'rb') as csv_file:
        for line in csv_file:
            trie.insert_word(line.decode('utf-8').rstrip('\n'))
    end = time.perf_counter() - start
    print(f'--- Dataset load time in {end} seconds ---')
    app.run()
