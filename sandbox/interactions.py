"""
I'm going to try to figure out the structure of the message log and interactions etc.
using a "book airline tickets" interaction as an example

"""

# User: Hello I want to book a flight from Amsterdam to Berlin
{
    sender: 'user',

    message: {
        text: 'Hello I want to book a flight from Amsterdam to Berlin',
        type: 'text',
    }

    # added later
    d: {
        domain: 'booking',
        intent: 'book_flight',
        entities: {
            from_city: 'Amsterdam',
            to_city: 'Berlin',
        }
    }
}

# The above message gets processed backend and an interaction starts, the interaction object looks like this:
{
    name: 'bookflight',
    entities: {
        from_city: 'Amsterdam',
        from_airport: 'AMS', # since there's only one airport in amsterdam
        to_city: 'Berlin',
    },
    span: [0, None] # this interaction spans from message 0 to None (because it is ongoing)
}

# Then the bot responds with this message:
{
    sender: 'bot',

    message: {
        type: 'select-option',
        text: 'One-way or return?',
        options: [
            { value: 'oneway', label: 'One way', text: ['One way, please'] },
            { value: 'return', label: 'Return', text: ['Return tickets'] },
        ],
        question: 'oneway-or-return',
    },

    interaction: 0,
}

# Then the user clicks on 'one way' and the backend basically creates the user's message
# and the next bot message in one
{
    sender: 'user',

    message: {
        type: 'select-option',
        text: 'One way, please',
    },

    interaction: 0,
}

# bot message
{
    sender: 'bot',

    message: {
        type: 'select-option',
        text: 'Which airport would you like to land in Berlin?',
        options: [
            { value: 'TXL', label: 'Tegel', text: ['Tegel'] },
            { value: 'SXF', label: 'Schonefeld', text: ['Shonefeld'] },
            { value: None, label: 'Any airport', text: ['Any airport'] },
        ],
        question: 'to-airport',
    },

    interaction: 0,
}

# Then the user clicks on 'Tegel' and the backend basically creates the user's message
# and the next bot message in one
{
    sender: 'user',

    message: {
        type: 'select-option',
        text: 'Tegel',
    },

    interaction: 0,
}

# bot message
{
    sender: 'bot',

    message: {
        type: 'select-option',
        text: 'Which airport would you like to land in Berlin?',
        options: [
            { value: 'TXL', label: 'Tegel', text: ['Tegel'] },
            { value: 'SXF', label: 'Schonefeld', text: ['Shonefeld'] },
            { value: None, label: 'Any airport', text: ['Any airport'] },
        ],
        question: 'to-airport',
    },
}
