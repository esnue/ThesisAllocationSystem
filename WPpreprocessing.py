from sklearn.feature_extraction.text import CountVectorizer
import string
from nltk.corpus import stopwords 
import warnings

stoplist = ['gov', 'anheier', 'xxx', 'et', 'enrichsource', 'al', 'rgreq', 'al', 'often', 'nin', 'nm', 'nd', 'nw', 'nn', 'ns',
'ng', 'np', 'ne', 'na', 'nat', 'nt', 'nio', 'may', 'net', 'even', 'use', 'publicationcoverpdf', '\\n', '\n', 'researchgate' 
'likely', 'dataset', 'nwe', 'aims', 'throughout', 'nbecause', 'nonly', 'gov', 'ncan', 'ncan', 'even', 'bryson', 'simple', 'reducing',
'net', 'example', 'jankin', 'results', 'first', 'esc', 'shows', 'also', 'utc', 'jstor', 'nu', 'nh', 'nb', 'doi' 
'www', 'tandfonline', 'nhttps', 'nof', 'nthe', 'well', 'new', 'nand', 'paper', 'co', 'however', 'kreyenfeld', '\\xa0See', '\\xa0BIaS?',
'wegrich', 'mena', 'nsource', 'ny', 'el', 'ng', 'nri', 'nio', 'neu', 'nbut', 'nif', 'ets', 'echr', 'used']

class WhiteSpacePreprocessing():

    def __init__(self, documents, stopwords_language="english", vocabulary_size=2000):

        self.documents = documents
        stop_words = stopwords.words(stopwords_language).append(stoplist)
        self.stopwords = set(stop_words)
        self.vocabulary_size = vocabulary_size

    def preprocess(self):

        preprocessed_docs_tmp = self.documents
        preprocessed_docs_tmp = [doc.lower() for doc in preprocessed_docs_tmp]
        preprocessed_docs_tmp = [doc.translate(
            str.maketrans(string.punctuation, ' ' * len(string.punctuation))) for doc in preprocessed_docs_tmp]
        preprocessed_docs_tmp = [' '.join([w for w in doc.split() if len(w) > 0 and w not in self.stopwords])
                             for doc in preprocessed_docs_tmp]

        vectorizer = CountVectorizer(max_features=self.vocabulary_size, token_pattern=r'\b[a-zA-Z]{2,}\b')
        vectorizer.fit_transform(preprocessed_docs_tmp)
        vocabulary = set(vectorizer.get_feature_names())
        preprocessed_docs_tmp = [' '.join([w for w in doc.split() if w in vocabulary])
                                 for doc in preprocessed_docs_tmp]

        preprocessed_docs, unpreprocessed_docs = [], []
        for i, doc in enumerate(preprocessed_docs_tmp):
            if len(doc) > 0:
                preprocessed_docs.append(doc)
                unpreprocessed_docs.append(self.documents[i])

        return preprocessed_docs, unpreprocessed_docs, list(vocabulary)