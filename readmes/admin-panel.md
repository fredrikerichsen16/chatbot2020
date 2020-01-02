# Chatbot Panel
This is the admin panel for Alfred employees to edit company types, default keywords, intents and domains etc.

### Company Types
We can add company types - for example "Airline". Then write a description for this kind of company type Chatbot, add an image etc. Basically this admin panel is a CMS for the admin panel that customers see.

### Domains, intents, and training sentences
We can add domains and intents - for example:
domain: flights
intent: book
training_sentences: "I would like to book a flight", "I need to book a flight" etc.

We can also add training sentences in different languages.

### Keywords and Staticwords
Here keywords and staticwords(?) are defined for two/three(?) levels of specificity:
- company types (Restaurant)
- sub company types (Chinese Restaurant, Italian Restaurant)
- and all company types (global). Examples are keywords like @time, @address, @date, @currency, @
- company-specific: of course. This is the most specific entity you can add keywords to. However, this is controlled in the company's admin panel.

Synonyms are to keywords what training sentences are to intents.
I.e. there are keywords (@country) -> you add a keyword value ("USA") -> then you add a number of synonyms.

Read more about keywords in keywords.md

# Admin Panel
This is the admin panel for customers using our chatbot in their application.

### Company Information
This is where they fill in a long ass form with all kinds of questions about the company: Their hours (on sundays, all public holidays, etc. very detailed), all kinds of stuff you know. This information is stored in a JSON file and used by the chatbot to give that information to the user asking questions.

### General Settings
- Whether to activate voice controlled chatbot
- What languages to offer
- What color/style the chatbot should have

### Domains, intents, and training sentences
Here the customer will see a list of all the domains, intents and training sentences that are in place by default for the company type "Airline". They can add training sentences to the intent 'flights.book' established above. This is an example of a highly general intent so they probably don't need to add many training sentences to it, but there are other intents which are more specific to each airline so they would probably add training sentences to those.

### Keywords
Add values and synonyms to keywords already defined globally and for your company_type.

#### Should you be able to add keywords?
You can definitely add values and synonyms to keywords defined globally and for your company_type.
I.e. a company can add the names of their hotel room types (suite, presidential suite, family room, etc.) to the keyword @hotel-room-type which is defined for the company_type 'hotel' no problem. But should they be able to create a new keyword? It won't be integrated into the code at all because it doesn't exist in any of the training sentences so what do we do with it? Well, if a company creates a keyword and references that keyword in training sentences which they add by themselves then that would be possible.
So yeah.

# TERMINAL ADMIN
In the real app there will be a backend for business owners to add keywords, domains and intents etc. to customize their chatbot. During development, this will be done with a terminal admin system.

## DevelopmentAdmin
### Main page:
Welcome to Development Admin
1. Add company type
2. View company types

## BusinessOwnerAdmin
They they can change the info about their company (hours, menu, etc.). Customize their
chatbot, add new languages support etc.
