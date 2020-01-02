# MongoDB DB structure

## company_types
```
{
    id: 1,
    type: "hotel",
},
{
    id: 2,
    type: "motel",
    subtypeof: 1,
}
```

## keywords
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
    id: 2,
    name: "hotel-room",
    language: "en",
    synonyms: ["room", "hotel room"],
    scope: {global: false, company_types: [1, 2], company: null},
    values: []
},
```

Notice in this one that the synonym: "motel room" has been added to refer to the keyword "hotel-room", and this applies to
the company type with the id 2 only (motel). Whereas the synonyms "room" and "hotel room" apply to the company type "hotel",
which motel is a subtype of. So the user can ask the motel chatbot for a room, hotel room, or a motel room and the chatbot
will know what they mean.

```
{
    id: 3,
    name: "hotel-room",
    synonyms: ["motel room"],
    scope: {
        global: false,
        company_types: [2],
        company: null,
    }
},
```

Notice with this one that the scope is a specific company (the company with id 1) rather than a global or company-type-specific
keyword. The synonym "mo-residence" only refers to @hotel-room in this specific company's chatbot, and "two-bed room" only
refers to the keyword value "double room".

```
{
    id: 4,
    name: "hotel-room",
    synonyms: ["mo-residence"],
    scope: {
        company: 1,
    }
    values: [
        {
            value: "double room",
            synonyms: ["double room", "two-bed room"]
        },
        {
            value: "family room",
            synonyms: ["family room", "room for families"]
        },
    ]
},
# This one uses subkeywords.
{
    id: 1,
    name: "venue-facility",
    synonyms: ["facility", "venue facility"],
    scope: {
        company: 2,
    }
    values: [],
    subkeywords: [
        {
            name: "casino",
            synonyms: ["casino", "gambling room", "gambling house"],
            values: [
                {
                    "value": "Red Dragon Casino",
                    "synonyms": ["red dragon casino", "chinese casino", "casino of the red dragon", "ching chong casino"]
                },
                {
                    "value": " Casino",
                    "synonyms": ["chinese casino", "china casino", "casino de china", "ching chong casino"]
                }
            ]
        }
    ]
}
```
