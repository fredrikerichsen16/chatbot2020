# Intent Classification

## Training
- Define many intents, and make many training sentences for each
- For example: flights.book. Training sentences:
    - I want to book a flight from @airport to @airport on @date with return on @date.
    - and many more similar.. with no keywords, similar keywords, completely different keywords etc.

### 1. Parse Input
Use NLTK to convert it to something like:
['i', 'wan', 'to', 'book', 'a', 'flight', 'from', '@airport', 'to', '@airport', 'on', '@date', 'with', 'ret', 'on', '@date']
Basically the verbs are cut so that tenses don't matter, periods and commas etc. are removed, everything is converted to lower case, maybe stop words are removed (not sure if that's smart, test it), and a few other things.

### 2. Bag-of-words
Basically take all the words in all the training sentences, put them in a list called bag-of-words, then convert each sentence to a vector of integers using that bag-of-words.

#### Keywords
Do something with keywords as well. Separate bag of words? Same bag of words? Also remember to differentiate between a staticword and keyword.
Btw @ goes before keywords and # goes before staticwords. (In training sentences).

#### POS tagging?
With NLTK you can tag parts-of-speech. Like this:
```
"They refuse to permit us to obtain the refuse permit"
=> [('They', 'PRP'), ('refuse', 'VBP'), ('to', 'TO'), ('permit', 'VB'), ('us', 'PRP'),
('to', 'TO'), ('obtain', 'VB'), ('the', 'DT'), ('refuse', 'NN'), ('permit', 'NN')]
```

Maybe I can also have the parts of speech in the vectorization of the sentence. Could be useful for the ML algorithm for intent classification idk, gotta test that.

### 3. Machine learning
Input: vectorized training sentences (with keywords, maybe with parts of speech)
Output: an intent
Label all the training sentences with their intent and train that shit.

### 4. BTW:
BTW, the intent classification algorithm is trained whenever the customer edits the training sentences or keywords etc. in their admin panel. (Probably not every time, because that would be expensive, but regularly.) So each company has their own bag of words file and file with the trained ML algorithm. These two files are stored on our server.

## Real Application
### 1. Parse Input
Parse input

### 2. Bag-of-words
Convert to bag of words (which is specific to the company at the current time, because their specific training sentences are unique and use unique words and their specific ML algorithm expects those numbers from their bag of words.)

### 3. Machine learning
Run it through the machine learning algorithm.

### 4. Other factors
The machine learning algorithm takes the user input and returns a score between 0 and 1 for each intent. High score = likely to be that intent - and vice versa. There might be a few intents with a high score, so the following are factors which are also considered:
- whether the intent is active or not:
    for example, the intent casino.hours is not active
    for a hotel that doesn't have a casino  (this is a bad example because someone could still ask this question not knowing, but I can't think of a better example rn)
- how common the intent is
    all chatbot chats are logged and analyzed, including intent frequency etc.
- how commonly the intent is marked as "appropriate":
    green checkmark/red X next to message
- the domain of the previous few messages
    obvious context reasons

### 5. Multiple sentences tested
If the user asks: "what are the casino's hours" to a hotel
It will be converted to two possible sentences:
"what are the @casino hours"
"what are the @venue-facility hours"
Because @casino is a subkeyword of @venue-facility.
Both variants will run through the neural network. If the @casino one gets a low score and @venue-facility gets a high score then the @venue-facility one is probably the right one.
- Just realized now: This is kind of a bs feature? Why did I think of this? When is this useful? Idk man lmao. Maybe I'll remember later.
