import model
import corrections
import codecs
WORDS = model.load_obj('data')
ERRORS = model.load_obj('errors')

def proofread(fname):
    mispelt = []
    with codecs.open(fname, "r",encoding='utf-8', errors='ignore') as f:
        for i, line in enumerate(f):
            text = line.rstrip()
            print(text)
            from nltk.tokenize import word_tokenize
            tokens = word_tokenize(text)
            words = [word for word in tokens if word.isalpha()]
            for word in words:
                if(ERRORS[word.lower()] == 0):
                    if (WORDS[word.lower()] == 0):
                        mispelt.append((i, word, [suggestion.term for suggestion in corrections.suggest(word)]))
                        ERRORS[word.lower()] += 1
                else:
                    mispelt.append((i, word, [suggestion.term for suggestion in corrections.suggest(word)]))
            model.save_obj(ERRORS, 'errors')
    return mispelt