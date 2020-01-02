# Domains and intents etc. for a hotel chatbot

```
{
    domain: "location",
    intent: "get",
    training_sentences: [
        "where are you located", "what's your location", "what is your location", "give me your location"
    ],
    scope: {
        global: false,
        company_types: [1],
        company: null,
    }
},
{
    domain: "location",
    intent: "directions",
    training_sentences: [
        {
            text: "directions from {} to your hotel",
            keywords: [{
                id: 1 # id of keyword,
                refers_to: "value" # refers to the "keyword" itself, or the keyword "value",
                fill_entity: "directions_from",
            }]
        }
    ],
    scope: {
        global: false,
        company_types: [1],
        company: null,
    }
},
```
