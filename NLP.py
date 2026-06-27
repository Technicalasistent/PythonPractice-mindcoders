import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt_tab')

text='Students are learning python for AI and Machine Learning in Bhopal'

#step 1 tokenise-split into words
tokens=word_tokenize(text.lower())
print('Tokens : ',tokens)

#step 2 : remove stepwords (common word that add no meaning)
stop=set(stopwords.words('english'))
filtered=[w for w in tokens if w not in stop and w.isalpha()]
print('After stopward removal : ',filtered)

#step 3 : lemmatise-reduce to root form
lemma=WordNetLemmatizer()
final=[lemma.lemmatize(w) for w in filtered]
print('After lemmatisation : ',final)

#tf-idf : convert text to number into ml
from sklearn.feature_extraction.text import TfidfVectorizer
docs=['Python is great for data science','Machine learning is amazing','AI is the future of technology']
tfidf=TfidfVectorizer()
matrix=tfidf.fit_transform(docs)
print('TF-IDF shape :',matrix.shape)
print('Feature names:',tfidf.get_feature_names_out())