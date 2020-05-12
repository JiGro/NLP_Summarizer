import wikipedia
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize

def frequency_table(inputString):
    stemmer = PorterStemmer()
    words = word_tokenize(inputString)
    stopWords = set(stopwords.words("english"))
    filteredWords = [w for w in words if not w in stopWords]
    freqTbl = dict()
    for word in filteredWords:
        word = stemmer.stem(word)
        if word not in freqTbl:
            freqTbl[word] = 1
        else:
            freqTbl[word] += 1
    return freqTbl


def sentences_score(sentences, freqTbl):
    sentenceVal = dict()
    for sentence in sentences:
        wordCount = (len(word_tokenize(sentence)))
        for entry in freqTbl:
            if entry in sentence.lower():
                if sentence[:10] not in sentenceVal:
                    sentenceVal[sentence[:10]] = freqTbl[entry]
                else:
                    sentenceVal[sentence[:10]] += freqTbl[entry]
            #print(entry, sentence.lower(), sentence[:10], sentenceVal)
        sentenceVal[sentence[:10]] = sentenceVal[sentence[:10]] // wordCount
    return sentenceVal


def avg_score(sentenceVal):
    sumValues = 0
    for entry in sentenceVal:
        sumValues += sentenceVal[entry]
    avg = int(sumValues / len(sentenceVal))
    return avg


def summary_generator(sentences, sentenceVal, threshold):
    sentenceCount = 0
    summary = ''
    for sentence in sentences:
        if sentence[:10] in sentenceVal and sentenceVal[sentence[:10]] > (threshold):
            summary += " " + sentence
            sentenceCount += 1
    return summary


input_str = input('What summary from Wiki do you wish to receive?')
input_list = wikipedia.search(input_str)
print(input_list)
print('Which page do you want?')
response = ''
while response not in input_list:
    response = input('Please copy from list above without quotes and paste here: ')

print('*** Summary: ' + str(response) + '***')
wiki_page = wikipedia.page(response)
print(wiki_page.title)
print(wiki_page.url)
wiki_content = wiki_page.content
freqTbl = frequency_table(wiki_content)
sentences = sent_tokenize(wiki_content)
sentenceScore = sentences_score(sentences, freqTbl)
avgScore = avg_score(sentenceScore)
threshold = 1.3
summary = summary_generator(sentences, sentenceScore, threshold * avgScore)
print(summary)
