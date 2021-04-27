from config import ROOT_DIR

dict_file = open(ROOT_DIR + '/text_files/dictionary.txt', 'r', encoding='utf-8').readlines()
stopwords_file = open(ROOT_DIR + '/text_files/stopwords.txt', 'r', encoding='utf-8').readlines()

luget = set()
stopwords = set()

for line in stopwords_file:
    stopwords.add(line.strip('\n'))

for line in dict_file:
    luget.add(line.strip('\n'))
