import nltk.corpus
import nltk.tokenize.punkt
import nltk.stem.snowball
from nltk.corpus import wordnet
import string
from nltk import word_tokenize
import pandas as pd
# Get default English stopwords and extend with punctuation

fil = pd.read_csv("questions_data_for_assignment.csv",delimiter=',')

stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(string.punctuation)
stopwords.append('')

def get_wordnet_pos(pos_tag):
    if pos_tag[1].startswith('J'):
        return (pos_tag[0], wordnet.ADJ)
    elif pos_tag[1].startswith('V'):
        return (pos_tag[0], wordnet.VERB)
    elif pos_tag[1].startswith('N'):
        return (pos_tag[0], wordnet.NOUN)
    elif pos_tag[1].startswith('R'):
        return (pos_tag[0], wordnet.ADV)
    else:
        return (pos_tag[0], wordnet.NOUN)

# Create tokenizer and stemmer
lemmatizer = nltk.stem.wordnet.WordNetLemmatizer()
#tokenizer = word_tokenize()


def is_ci_lemma_stopword_set_match(a, b, threshold):
    """Check if a and b are matches."""
    pos_a = map(get_wordnet_pos, nltk.pos_tag(word_tokenize(a)))
    pos_b = map(get_wordnet_pos, nltk.pos_tag(word_tokenize(b)))
    lemmae_a = [lemmatizer.lemmatize(token.lower().strip(string.punctuation), pos) for token, pos in pos_a \
                if pos == wordnet.NOUN and token.lower().strip(string.punctuation) not in stopwords]
    lemmae_b = [lemmatizer.lemmatize(token.lower().strip(string.punctuation), pos) for token, pos in pos_b \
                if pos == wordnet.NOUN and token.lower().strip(string.punctuation) not in stopwords]
    
    # Calculate Jaccard similarity
    if (float(len(set(lemmae_a).union(lemmae_b)))):    
    
        ratio = len(set(lemmae_a).intersection(lemmae_b)) / float(len(set(lemmae_a).union(lemmae_b)))
        if (ratio >= threshold):
            return 1 
        else: 
            return 0 
    else: 

        return 1
         

Listq1 = fil ['question1']
Listq2 = fil ['question2']

Result = fil ['is_duplicate']
#print Result
#a= "How likely is a solar storm that affects Earth? "
#b= "How is Earth affected by a solar storm?"
for i in range(0,10): 
    a = Listq1[i]
    b = Listq2[i]
    
    print is_ci_lemma_stopword_set_match(unicode(a,"utf-8"),unicode(b,"utf-8"),threshold=0.40000000000000004)

