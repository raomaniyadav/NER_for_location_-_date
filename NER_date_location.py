import re
from nltk.tokenize import sent_tokenize,SpaceTokenizer
import nltk
from nltk.chunk import ne_chunk
from nltk import pos_tag
from nltk.tree import Tree
def get_location(text):
    t=nltk.tokenize.sent_tokenize(text)
    m=[]
    for i in t:
        c=[]
        if re.search(pattern=r"(\d\d\d\d | \d\d)",string=i):
            a=re.findall(pattern=r"(\d\d\d\d|\d\d)",string=i)
        n = ne_chunk(pos_tag(SpaceTokenizer().tokenize(i)))
        for s in n:
            if type(s) == Tree and s.label() == "GPE":
                c.append(" ".join([token[0] for token in s.leaves()]))
                
        m.append([i,c,a])
    print(m)