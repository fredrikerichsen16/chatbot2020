"""
Here's an explanation of all the components during a chatbot conversation and how the various processes relate to each other.

BOT: Hello, welcome to SR-Bank. What can I help you with?
USER: I would like to send money overseas
    Here you can see the user typed a quite complicated request. How does the bot understand this message?
      0. First of all, the chatbot window has auto-correct to minimize typos which make the following steps more difficult.
      1. The user presses enter, and sends the message. The chatbot window is front-end, the JavaScript etc. is on the company's website.
         But the message is sent API-style to Alfred's server with the object MSG_LOG and all the backend shit is done, and the MSG_LOG is returned
         What is MSG_LOG? It contains all the information about the chat (bot's messages, user's messages, memory, etc.) It get's sent back and forth between the
         company's website and the Alfred served because what's going on backend is done on our served and is secret so it has to be done with an API.
         MSG_LOG will be discussed more later.
      2. The sentence is decomposed with NLTK and run through a keyword classification algorithm.
            - In this case the algorithm would return something like this:
                - ['i', 'will', 'like', 'to', 'send', 'money', '@destination']
                    -> @destination = 'overseas'
                    - NB: this is simplified, there needs to be a way to represent keywords other than '@keyword'
                          Also, verbs like (will, like, send) are chopped like (wi, lik, sen) so tense doesn't matter.
                          Also, I might remove stopwords like a, an, to, etc. so intent classification might be easier (must be experimented with when I start doing neural net)
                          Also, I might classify parts of speech like verb, noun, adjective, proposition etc. because it might be useful in intent classification neural net (TBD)
                          Also, typos will be automatically corrected
            - A better example would be this sentence (more keywords):
                "I would like to book a flight from AMS to Stavanger, Norway on November 12th and return in the morning on the 15th of November
                This would be keyword classified as:
                "I would like to book a flight from @airport to @city on @date and return @timeofday on @date"
                - Keywords like @date (and @country, @city, @time, @language) etc. are GLOBAL keywords. They are functions created by the Alfred team specifically to capture
                  the various ways you can for example write a date and capture it in a default format "YYYY-MM-DD"
                - Keywords like @airport are company_type specific. In this case specific to the company_type 'airline'. These keywords are also created by the Alfred team
                  but only apply to airlines, not all company type chatbots. Contrary to the keyword @date, the keyword @airport is synonym-based, not function-based.
                  So the @airport keyword has a list of values "AMS", "LAX" etc. and synonyms for those airports "Amsterdam Int. Airport", "LA Airport", "LAX Airport",
                  "LA International Airport" etc.
                - Finally, there are company-specific keywords. For example if a hotel creates a chatbot, when they fill out the information on their hotel (so this
                  information can be used in the chatbot) they are asked to list their room types and various ways the user might refer to that room.
                  For example: "family-suite" can be referred to by customers as "family suite", "family sweet", "family luxury room" etc.
            - There are also FIXED KEYWORDS. There don't have a value like @airport -> 'AMS'. Instead consider the fixed keyword @wifi. There are multiple ways for a
              customer to ask for wifi: "Do you have wifi/wi-fi/internet connection/internet/free wifi" etc. all these are captured into the fixed keyword @wifi.
            - Go to company-types.md to see an example of keywords database structure in MongoDB!!!
      2. Intent classification
           Basically, there are domains and intents. For example the message above would probably be in the domain 'transfers' and intent 'beginTransfer' for example.
           That intent would have a lot of training sentences with various ways to write that message.
           All the training sentences go through the same NLTK and keyword classification treatment which the user input will be put through. This list of words is then
           converted to a list of integers (vector) where each integer represents a word in a BagOfWords list (which is created based on every single word in the corpus of
           training sentences.) Finally you have a trained neural network (which will be quite complicated, more so than described here) and you take the user input,
           run it through step 2, turn it into a vector and put it through the neural network. There might be 3 intents with a high score, so these are possible intents.

           To decide which one is correct the following additional factors will be considered:
             - whether the intent is active or not:
                  for example, the intent casino.hours is not active
                  for a hotel that doesn't have a casino  (this is a bad example because someone could still ask this question not knowing, but I can't think of a better example rn)
             - how common the intent is
                  all chatbot chats are logged and analyzed, including intent frequency etc.
             - how commonly the intent is marked as "appropriate":
                  green checkmark/red X next to message
             - the domain of the previous few messages
                  obvious context reasons
      3. Process intent:
            Now the domain, intent, and keywords are known. The method "domain_intent" is called and all the shit is done here.
            A simple example would be if the user asked a restaurant:
            "What are your hours today?" The method could look something like this:
            basicinfo_hours():
                day = get_day() # 'monday'
                hours = company_info['basicinfo']['hours'][day]
                msg = 'We open at {} and close at {}'.format(hours['open'], hours['close']}
                return {'bot_message': msg}
      4. Start interaction:
            The method "transfers_beginTransfer" will be a bit complicated than the example in step 3.
            We would have to start an interaction.
            LinkedList.
      5. Access Bank's backend:
            Next step would be for the bot to say:
            BOT: Ok, select which of your bank accounts you want to transfer from.
            But Alfred doesn't have access to the SR-Bank's database so this can't be done on our backend. So we would put the following in MSG_LOG:
            {
                action_required: {
                    'action': 'get_user_bank_accounts',
                    'data': {
                        'user_id': 1,
                    }
                }
            }
            Now, MSG_LOG would be returned with that data.
            Then the function get_user_bank_accounts(user_id) would be called on SR-Bank's backend, and return a list of bank accounts.
            On Alfred's website where SR-Bank customizes/administers their chatbot etc. there would be a list of functions which they have to create, what parameters to incldue
            and the expected return value format. They create all the methods and Alfred takes care of the rest.
            Now, with the list of the user's bank accounts, we go back into Alfred's API and go to the method transfers_beginTransfer() and prepare the bot's output
            etc. and put it into MSG_LOG and do what we gotta do. This way we take care of everything on the backend, and whenever we need something we aren't allowed to
            access for security reasons etc. we just go get that quickly and go back with the data we're allowed to see and prepare the bot response.

"""


"""

Interaction:
- Have an interaction design feature on Alfred's website, don't hard code it, that's way too much work.

{
    id: 1,
    bot_message: "What country do you live in?"
    input: {
        textOptions: [
            {
                option: "UK",
                goto: 2,
            }.
            {
                option: "USA",
                goto: 3,
            }
        ]
    }
}
{
    id: 2,
    from: 1, # do I need this or do I only need "goto"? Like if I'm going from A->B do I need A's ID in B or only B's ID in A? Probably the latter. Because multiple letters can go to B.
    bot_message: "Do you agree to EU's data privacy laws?"
    input: {
        textOptions: [
            {
                option: "Yes",
                goto: 3,
            }.
            {
                option: "No",
                goto: "HELL BITCH, YOU GOTTA ACCEPT IT MOTHA FUCKAAAAA:,
            }
        ]
    }
}
{
    id: 3,
    bot_message: "What is your address?"
    input: {
        text: {
            "expectsKeyword": "@address",
            "else": {
                "insist": True,
                "message": "Couldn't detect an address, please try again."
            }
        }
    }
}








"""




"""
{
    user_message: "What time does the Green Lantern casino close on @day",
    meaning: {
        domain: "casino",
        intent: "hours",
        entities: {
            day: "saturday"
        }
    }
},
{
    user_message: "What time does the Green Lantern casino close on @day",
    meaning: {
        domain: "casino",
        intent: "hours",
        entities: {
            day: "saturday"
        }
    }
},
{
    id: 1,
    bot_message: "What country do you live in?"
    input: {
        textOptions: [
            {
                option: "UK",
                goto: 2,
            }.
            {
                option: "USA",
                goto: 3,
            }
        ]
    }
}
{
    id: 2,
    from: 1, # do I need this or do I only need "goto"? Like if I'm going from A->B do I need A's ID in B or only B's ID in A? Probably the latter. Because multiple letters can go to B.
    bot_message: "Do you agree to EU's data privacy laws?"
    input: {
        textOptions: [
            {
                option: "Yes",
                goto: 3,
            }.
            {
                option: "No",
                goto: "HELL BITCH, YOU GOTTA ACCEPT IT MOTHA FUCKAAAAA:,
            }
        ]
    }
}
{
    id: 3,
    bot_message: "What is your address?"
    input: {
        text: {
            "expectsKeyword": "@address",
            "else": {
                "insist": True,
                "message": "Couldn't detect an address, please try again."
            }
        }
    }
}



"""





