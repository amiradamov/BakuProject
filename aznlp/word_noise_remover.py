import re
from aznlp.letter_map import lower_map


def remove_noise(word):
    # lower the word and remove unnecessary characters from it
    word = re.sub('http[s]?://(?:[a-zÖĞIƏÇŞİÜöğıəçşiüA-Z]|[0-9]|[$-_@.&+#]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                  '', word)
    word = re.sub("(@[öğıəçşiüÖĞIƏÇŞİÜA-Za-z0-9_]+)", '', word)
    word = word.translate(lower_map).strip('<>?:;\'"\\|/.,[]{}+=-_)(*&^%$#@!`~ ')
    return word
