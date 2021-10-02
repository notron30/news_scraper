import time
import gensim
import sqlite3
import pandas as pd


i=1
while i>0:
        
    con = sqlite3.connect("headlines.sqlite")
    qry = """
    SELECT DISTINCT * from pulls
        WHERE LENGTH(article)>300
        AND news_source != 'reuters'
    """
    df = pd.read_sql_query(qry, con)
    articles = df['article'].to_list()

    def read_corpus(corp, tokens_only=False):
        for i, line in enumerate(corp):
            tokens = gensim.utils.simple_preprocess(line)
            if tokens_only:
                yield tokens
            else:
                yield gensim.models.doc2vec.TaggedDocument(tokens, [i])

    train_corpus = list(read_corpus(articles))

    model = gensim.models.doc2vec.Doc2Vec(vector_size=150, min_count=2, epochs=25)

    start = time.time()
    model.build_vocab(train_corpus)
    model.train(train_corpus, total_examples=model.corpus_count, epochs=model.epochs)
    model.save('trained/current.model')
    conn = sqlite3.connect('trained/corpus.sqlite')
    df.to_sql('corpus',conn,if_exists="replace")
    conn.close()
    with open('refresh.txt', mode = 'w+') as f:
        f.write('yes')


    end = time.time()
    print('took '+str(round(end-start,2))+' seconds to learn')
    time.sleep(900)

    i=i+1
