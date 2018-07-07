from api import app, trie
from utils import Timer


if __name__ == '__main__':
    timer = Timer()
    with timer:
        with open('data/6500titles.csv', 'rb') as csv_file:
            for line in csv_file:
                trie.insert_word(line.rstrip('\n'))
    print(f'--- Dataset load time in {timer.result:.4f} seconds ---')
    app.run()
