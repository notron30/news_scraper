import gensim
import sqlite3
import pandas as pd

def model_loader():
    modelo = gensim.models.doc2vec.Doc2Vec.load("trained\current.model")
    return modelo

def corpus_loader():
    con = sqlite3.connect("trained\corpus.sqlite")
    corp = pd.read_sql_query("SELECT * FROM corpus",con)
    con.close()
    return corp

def correlate(start_model, start_corpus, prompt):
    with open("refresh.txt", mode='r+') as f:
        check = f.read()
    if check == 'yes':
        model = model_loader()
        corpus = corpus_loader()
        with open("refresh.txt", mode='w+') as f:
            f.write('no')
    else:
        model = start_model
        corpus = start_corpus
    
    prompt_fixd = gensim.utils.simple_preprocess(prompt)
    inferred_vector = model.infer_vector(prompt_fixd)
    sims = model.dv.most_similar([inferred_vector], topn=len(model.dv))
    food = {}
    for i in list(range(10)):
        sim = sims[i][0]
        food[str(i+1)] = corpus[corpus.index == sim].to_dict(orient='index')[sim]
    return food