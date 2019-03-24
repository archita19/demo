# from nltk.tokenize import sent_tokenize
# text = "Joel is ugly, Tukaram is an idiot. They are students of TYBSc"
# print(sent_tokenize(text))

# from nltk import pos_tag
# from nltk import RegexpParser
# text = "Joel is ugly, Tukaram is an idiot. They are students of TYBSc".split()
# print("After Split:",text)
# tokens_tag = pos_tag(text)
# print("After Token:",tokens_tag)
# patterns= """mychunk:{<NN.?>*<VBD.?>*<JJ.?>*<CC>?}"""
# chunker = RegexpParser(patterns)
# print("After Regex:",chunker)
# output = chunker.parse(tokens_tag)
# print("After Chunking",output)

import nltk
text = "ugly Joel, idiotic Tukaram. They are students of TYBSc"
tokens = nltk.word_tokenize(text)
print(tokens)
tag = nltk.pos_tag(tokens)
print(tag)
grammar = "NP: {<DT>?<JJ>*<NNP>}"
cp  =nltk.RegexpParser(grammar)
result = cp.parse(tag)
print(result)
result.draw()    # It will draw the pattern graphically which can be seen in Noun Phrase chunking 