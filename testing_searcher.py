from gensim.models import Word2Vec

gmodel=Word2Vec.load_word2vec_format(fname)
ms=gmodel.most_similar('good',10)
for x in ms:
    print x[0],x[1]