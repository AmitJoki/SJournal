import model
from collections import defaultdict
import all

def reset():
    model.save_obj(defaultdict(int, all.all_words), 'data')
    model.save_obj(defaultdict(int, {}), 'errors')
