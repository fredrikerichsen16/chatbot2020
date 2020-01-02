# Design

## Message types
There are many different types of ways the bot can send data and ask for data from the user, instead of only using text.
The reasons for this are the following:
- it's faster, easier, and more pleasant for the user
- it's easier to develop a chatbot where the bot asks the user to select "Yes" or "No" and other options like that than just pure free text.

### Default Message Types

#### Text
Just text.

#### Select Options
Bot asks user to select one or more of a list of options.
User selects one or more and hits send.

For example:
```
{
   'sender': 'bot',
   'message': {
       'type': 'select_options',
       'text': 'May I access your location?',
       'options': [
           {'name': 'Yes', value=True},
           {'name': 'No', value=False}
       ],
       'settings': {
           'max_select': 1
       },
       'parameters': {
           'fill_entity': 'access-location',
       }
   }
},
{
   'sender': 'user',
   'message': {
       'type': 'select_options',
       'text': 'Yes',
       'value': True,
       'response_to': 0
   }
}
```
#### Prompt
Bot asks a user a direct question, user answers with text.
For example:
What is your address? What is your phone number? Do you have any other questions?

The msg_log dictionary might look something like this:
```
{
    'sender': 'bot',
    'message': {
        'type': 'prompt',
        'text': 'What is your address?',
        'settings': {
            'capture': {
                'keyword': '@address',                                  // <-
                'error': {                                              // <-
                    'notfound': {                                       // <-
                        'text': "Couldn't find an address, try again",  // <-
                        'tryagain': true,                               // <-
                    }
                }
            }
        }
    }
}
```

The highlighted code basically makes it so that if the user types "Not an address", bot will say: "Couldn't find address, try again", user will type in: "My address is Fjellfruebakken 5, 4072 Randaberg" and the bot will capture only the address part of that message.

#### Carousel
Carousel of items containing an image, some text and optionally some buttons.
For example:
```
{
    "sender": "bot",
    "message": {
        "type": "carousel",
        "text": "Select a hotel room you'd like to book:"
    },
    "settings": {
        "carousel_type": "sometype"
    },
    "slides": [
        {
            "image": "hotel-room-1.jpg",
            "header": "Deluxe Double Bedroom",
            "description": "This is a lovely room and it's $120 a night",
            "buttons": {
                "book-room": {
                    "intent_obj": {
                        "entities": {
                            "room": "deluxe-double-bedroom"
                        }
                    }
                },
            }
        }
    ],
    "buttons_templates": [
        {
            "name": "book-room",
            "label": "Book Room",
            "intent_obj": {
                "domain": "rooms",
                "intent": "book"
            }
        },
        {
            "name": "more-info",
            "label": "More Info",
            "intent_obj": {}
        }
    ]
}
{
    "sender": "user",
    "message": {
        "type": "carousel",
        "response_to": 3,
        "slide": 0,
        "button": 0
    }
}
```

#### Widget Message Types
Widgets are a bot message type.

They're custom message variations to use for better UX instead of just simple message types such as 'text', and 'select_options' etc.

Some (most) widgets are designed to get a response from a user (calendar, payment form, range slider, etc.)
Other widgets are designed to display some kind of data, not get a response from the user (flight data, google maps)

##### Examples
- order food (very complicated widget to browse menu, and add food to order)
- calendar (select dates for a hotel booking or flight)
- login (login to your bank for a banking chatbot)
- select number
- payment form
- range slider (for example price range)
- google maps
- flight data (departure and arrival airport time price etc.)
- specialized selects, for example "male or female" with male or female icons etc. - to spice shit up and make chat less boring and predictable

Designs:
- [Vertical multi select with icons](https://dribbble.com/shots/3459490-Working-on-a-chatbot-flow-design-for-LaunchOrb-app)
- [Range slider, order confirmation](https://dribbble.com/shots/2822930-Messenger-Bots-Augmented-Video-Call-Concept-2)
- Specialized select
	- [Example 1](https://dribbble.com/shots/3082618-Lily-App-Redesign-WIP)
	- [Example 2](https://dribbble.com/shots/3443059-On-boarding)
- [Sick flight info widget](https://dribbble.com/shots/3326602-Daily-UI-Challenge-13-Direct-messaging)
