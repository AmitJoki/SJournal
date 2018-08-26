import nltk
import language_check
tool = language_check.LanguageTool('en-US')

# def check(text):
#     sent_text = nltk.sent_tokenize(text) # this gives us a list of sentences
#     result = []
#     print(sent_text)
#     for sentence in sent_text:
#         matches = tool.check(sentence)
#         print(matches)
#         for i in range(len(matches)):
#             m = matches[i]
#             if(m.locqualityissuetype != 'misspelling'):
#                 result.append((m.fromy, sentence, ", ".join(m.replacements), m.category))
#     return result

def check(text):
    result = []
    matches = tool.check(text)
    print(matches)
    for i in range(len(matches)):
        m = matches[i]
        if(m.category == 'Grammar'):
            result.append((m.fromy, m.context, ", ".join(m.replacements), m.category))
    return result