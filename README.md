# SJournal

A Proof-reading software for helping those who write Scientific Journals

## Training 

The model has to be first trained. It can be achieved by the following:

```
python init.py
```

What `init.py` does is, it normalizes the data and trains the model based on the dataset of text files of IEEE papers present in `data` folder.

## Running

Run the UI by running

```
python ui.py
```
## Pre-requisites
1. Python 3+
2. tkinter
3. NLTK (Natural Language Toolkit)
4. `language-check` package.
5. SymSpell (1 million times faster through Symmetric Delete spelling correction algorithm ported to Python)
