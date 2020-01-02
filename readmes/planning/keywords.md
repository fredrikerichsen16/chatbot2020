# KEYWORDS AND STATWORDS

## Specificity
Keywords are defined for four levels of specificity
- company types (Restaurant)
- sub company types (Chinese Restaurant, Italian Restaurant)
- and all company types (global). Examples are keywords like @time, @address, @date, @currency, @unit-of-weight - apply to everyone
- company-specific: Keywords defined by companies.

## Keyword types
There are two keyword types: text-based and function based.
- Function based: an example is @time - Time can be written as 7PM, 14:30, 2:30PM, Half past 7, etc. so a function is needed to convert it into a standard format. Other examples: @address, @date
- Text-based: an example is @country (or @currency) - countries can be written in many ways: US, USA, U.S.A., United States etc.
so the keyword @country is defined, the value "USA" is defined, and the synonyms: "US", "USA", "United States of America" etc. are defined.
- Hybrid: Not sure, but maybe something like @city would/should be able to use both. Is that a necessary feature to implement? Maybe. You can't add every city in the world to a text-based keyword, so some of them would have to be captured by a function based on them sounding like a city, starting with a capital letter etc.

## Staticwords
Or statwords? Or something else? Basically exactly the same as keywords, except keywords contain a keyword and a value.
For example if you type "I want to travel to Amsterdam Airport", the keyword is @airport and the value is "AMS". On the other hand, staticwords only have the keyword. It could be useful for a hotel chatbot to have the statword @wifi because the customers could ask if they have free wifi in 20 different ways: "wifi", "wi-fi", "internet", "interweb", "internet connection" etc.
So those are all captured in the statword @wifi, but it doesn't have a value. Everything said above about keywords also applies to statwords (4 levels of specificity and types.)

A keyword can be a statword as well. For example, if a hotel has two casinos, it would look something like this:

```
@casino:
    static: casino, playing room, gambling room, gambling area # <- refers to the statword @casino itself
    values:
        hong kong casino: hong kong casino, chinese casino, ching-chong casino # <- refers to the hong-kong-casino VALUE of the KEYWORD @casino
        strip club casino: strip club casino, strip casino, the casino with a damn strip club
```

## Subkeywords
For example, consider a hotel chatbot.

```
# @venue-facility.@swimming-pool
# @venue-facility.@casino
# @venue-facility.@nightclub
#
# @venue-experience.@activity.@excursion
#
#
# So if user types:
# "What time does the gambling room close?"
# it becomes:
# "what time does the @venue-facility close?" -> {key: '@venue-facility', value: ['gambling room', '@casino']}
# OR
# "what time does the @casino close?"
#
# Run both versions through intent classification algorithm and whichever one gets a stronger result is
# probably the correct one. Also, give some extra weight to the sub keyword. I.e. @casino.
#
# When training neural network, only run through the version of the sentence with the sub keyword
# extracted, NOT both.
```

# MongoDB Database Structure of Keywords/Statwords
```
{
    id: 2,
    name: "address",
    function: "address",
    global: true,
    scope: {
        global: true,
        company_types: [],
        company: null,
    }
},
{
    id: 3,
    name: "hotel-room",
    synonyms: ["room", "hotel room"],
    values: [
        {
            value: "double bedroom suite",
            synonyms: ["double bedroom suite", "double suite", "two-bedroom suite"]
        },
        {
            value: "presidential suite",
            synonyms: ["presidential suite", "presidential"]
        },
    ]
},
{
    id: 1,
    name: "venue-facility",
    synonyms: ["facility", "venue facility"],
    values: [],
    subkeywords: [
        {
            name: "casino",
            synonyms: ["casino", "gambling room", "gambling house"],
            values: [
                {
                    "name": "Red Dragon Casino",
                    "synonyms": ["red dragon casino", "chinese casino", "casino of the red dragon", "ching chong casino"]
                },
                {
                    "name": " Casino",
                    "synonyms": ["chinese casino", "china casino", "casino de china", "ching chong casino"]
                }
            ]
        }
    ]
}
```
