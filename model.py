import glob
import pickle
import codecs

def save_obj(obj, name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, 2)

def load_obj(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

def train():
    path = 'data/*.txt'
    files=glob.glob(path)
    WORDS = load_obj('data')
    for file in files:
        with codecs.open(file, "r",encoding='utf-8', errors='ignore') as f:
            text = f.read()
            from nltk.tokenize import word_tokenize
            tokens = word_tokenize(text)
            words = [word for word in tokens if word.isalpha()]
            for word in words:  
                WORDS[word.lower()] += 1
    save_obj(WORDS, 'data')

