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

# from: https://en.wikipedia.org/wiki/Pomodoro_Technique
text = 'The Pomodoro Technique is a time management method developed by Francesco Cirillo[1] in the late 1980s. The technique uses a timer to break down work into intervals, traditionally 25 minutes in length, separated by short breaks. Each interval is known as a pomodoro, from the Italian word for tomato, after the tomato-shaped kitchen timer that Cirillo used as a university student. The technique has been widely popularized by dozens of apps and websites providing timers and instructions. Closely related to concepts such as timeboxing and iterative and incremental development used in software design, the method has been adopted in pair programming contexts. There are six steps in the original technique: Decide on the task to be done. Set the pomodoro timer (traditionally to 25 minutes). Work on the task. End work when the timer rings and put a checkmark on a piece of paper. If you have fewer than four checkmarks, take a short break (3–5 minutes), then go to step 2. After four pomodoros, take a longer break (15–30 minutes), reset your checkmark count to zero, then go to step 1. The stages of planning, tracking, recording, processing and visualizing are fundamental to the technique. In the planning phase, tasks are prioritized by recording them in a "To Do Today" list. This enables users to estimate the effort tasks require. As pomodoros are completed, they are recorded, adding to a sense of accomplishment and providing raw data for subsequent self-observation and improvement. For the purposes of the technique, a pomodoro is the interval of time spent working. After task completion, any time remaining in the Pomodoro is devoted to overlearning. Regular breaks are taken, aiding assimilation. A short (3–5 minutes) rest separates consecutive pomodoros. Four pomodoros form a set. A longer (15–30 minute) rest is taken between sets. A goal of the technique is to reduce the impact of internal and external interruptions on focus and flow. A pomodoro is indivisible; when interrupted during a pomodoro, either the other activity must be recorded and postponed (using the inform – negotiate – schedule – call back strategy[8]) or the pomodoro must be abandoned. The creator and his proponents encourage a low-tech approach, using a mechanical timer, paper, and pencil. The physical act of winding the timer confirms the users determination to start the task; ticking externalises desire to complete the task; ringing announces a break. Flow and focus become associated with these physical stimuli. The technique has inspired application software for several platforms.'
freqTbl = frequency_table(text)
sentences = sent_tokenize(text)
sentenceScore = sentences_score(sentences, freqTbl)
avgScore = avg_score(sentenceScore)
threshold = 1.3
summary = summary_generator(sentences, sentenceScore, threshold * avgScore)
print(summary)
