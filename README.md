# Summarizing texts using NLP

![Logo of the project](https://cdn.pixabay.com/photo/2014/02/22/21/25/glasses-272401_960_720.jpg)

### Natural Language Processing (NLP): What Is It and Why Is it Important?
**Natural language processing (NLP)** is a subfield of linguistics, computer science, information engineering, and artificial intelligence concerned with the interactions between computers and human (natural) languages, in particular how to program computers to process and analyze large amounts of natural language data.

NLP can also have significant impact in the business environment. Since the personal performance of each employee is the bedrock of business productivity and success, correctly applied **NLP can** improve staff confidence and morale, **increase team performance and productivity and in turn improve customer satisfaction**.

### Project intention
This .py script is my first approach to text processing. By utilizing the NLTK library in combination with a basic math algorithm, a given input text will be summarized. The threshold variable allows for adjustment of the summary length. The higher the threshold, the fewer words make the cut. I found the threshold of 1.3 to work perfectly.

🛑🛑🛑 **Disclaimer** 🛑🛑🛑

The following sections might include code snippets in order to allow following my thought process. However, steps have been cut out. For detailed code refer to .py file.

***
### 1.) Creating a Frequency Table

Input text from: https://en.wikipedia.org/wiki/Pomodoro_Technique

_**The Pomodoro Technique is a time management method developed by Francesco Cirillo[1] in the late 1980s. The technique uses a timer to break down work into intervals, traditionally 25 minutes in length, separated by short breaks. Each interval is known as a pomodoro, from the Italian word for tomato, after the tomato-shaped kitchen timer that Cirillo used as a university student. The technique has been widely popularized by dozens of apps and websites providing timers and instructions. Closely related to concepts such as timeboxing and iterative and incremental development used in software design, the method has been adopted in pair programming contexts. There are six steps in the original technique: Decide on the task to be done. Set the pomodoro timer (traditionally to 25 minutes). Work on the task. End work when the timer rings and put a checkmark on a piece of paper. If you have fewer than four checkmarks, take a short break (3–5 minutes), then go to step 2. After four pomodoros, take a longer break (15–30 minutes), reset your checkmark count to zero, then go to step 1. The stages of planning, tracking, recording, processing and visualizing are fundamental to the technique. In the planning phase, tasks are prioritized by recording them in a "To Do Today" list. This enables users to estimate the effort tasks require. As pomodoros are completed, they are recorded, adding to a sense of accomplishment and providing raw data for subsequent self-observation and improvement. For the purposes of the technique, a pomodoro is the interval of time spent working. After task completion, any time remaining in the Pomodoro is devoted to overlearning. Regular breaks are taken, aiding assimilation. A short (3–5 minutes) rest separates consecutive pomodoros. Four pomodoros form a set. A longer (15–30 minute) rest is taken between sets. A goal of the technique is to reduce the impact of internal and external interruptions on focus and flow. A pomodoro is indivisible; when interrupted during a pomodoro, either the other activity must be recorded and postponed (using the inform – negotiate – schedule – call back strategy[8]) or the pomodoro must be abandoned. The creator and his proponents encourage a low-tech approach, using a mechanical timer, paper, and pencil. The physical act of winding the timer confirms the users determination to start the task; ticking externalises desire to complete the task; ringing announces a break. Flow and focus become associated with these physical stimuli. The technique has inspired application software for several platforms.**_


First, we dissect the input string / text and create a list of single word snippets, excluding stop words of the English language. 

```
{'the': 7,
 'pomodoro': 12,
 'techniqu': 8,
  ...
 'applic': 1,
 'sever': 1,
 'platform': 1}

```

### 2.) Creating a sentence list
We utilize NLTK's sent_tokenize() function to split the input text into full sentences. This will help us in further calculate the sentence scores.

```shell
['The Pomodoro Technique is a time management method developed by Francesco Cirillo[1] in the late 1980s.',
 'The technique uses a timer to break down work into intervals, traditionally 25 minutes in length, separated by short breaks.',
  ...
 'Flow and focus become associated with these physical stimuli.',
 'The technique has inspired application software for several platforms.']
```

***
### 3.) Output dictionary with scores for each sentence
Next, we loop through the entire sentence list from 2.). We now select the first 10 characters of each sentence and check for matches in the frequency table from 1.). Finally, we generate a final score for each sentence by floor dividing the frequencies by the word count.

```shell
{'The Pomodoro Te': 3,
 'The technique u': 4,
 'Each interval i': 3,
  ...
 'The creator and': 3,
 'The physical ac': 2,
 'Flow and focus ': 4}
 ```
 
***
### 4.) Calculation of average sentence score
We calculate the average sentence score by adding up all individual scores and diving through the length of the sentence list

```shell
avgScore
Out: 4
 ```
 
***
### 5.) Summary
In the last step, we use the defined threshold variable to identify those sentences that make the cut. These will be added to the summary string, which will then be printed out. 

```shell
Set the pomodoro timer (traditionally to 25 minutes). Work on the task. Regular breaks are taken, aiding assimilation. A short (3–5 minutes) rest separates consecutive pomodoros. Four pomodoros form a set.
 ```

