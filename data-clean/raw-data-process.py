import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize

nltk.download("stopwords")
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt_tab')

def preprocess_text(text):
    stop_words = set(stopwords.words("indonesian"))
    sentences = sent_tokenize(text)
    processed_sentences = [" ".join([word for word in sentence.split() if word.lower() not in stop_words]) for sentence in sentences]
    return processed_sentences

text = "Universitas kami memiliki banyak program studi unggulan. Setiap mahasiswa harus mengikuti ujian masuk."
cleaned_text = preprocess_text(text)
print(cleaned_text)
