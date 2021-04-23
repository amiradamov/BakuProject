import random

def example(word):
    if word.startswith("quba-xaçmaz bölgə") and word.endswith("aralıq azərbaycan təmsil"):
        labels = ['arxitektura', 'din', 'edebiyyat', 'ekologiya', 'elm', 'felsefe', 'herb', 'huquq', 'idman',
          'incesenet', 'jurnalistika', 'kendteserrufati', 'maliyye', 'medeniyyet', 'proqramlaşdırma',
          'psixologiya', 'rabiteveinformatika', 'siyaset', 'sosiologiya', 'tarix', 'tibb', 'turizm']
        randd = random.choice(labels)
        return "Category Name: "+ randd
    return "something went wrong"