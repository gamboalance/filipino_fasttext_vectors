# Download the model files from http://tiny.cc/iknb001

from gensim.models import Word2Vec

fil_model = Word2Vec.load('fil_model')
fil_vectors = fil_model.wv

en_model = Word2Vec.load('en_model')
en_vectors = en_model.wv

# for model usage instructions, see https://radimrehurek.com/gensim/models/word2vec.html
