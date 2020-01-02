# Context

## CONVO 1:
```
- Hey can I book a room?
* Yes, select a room: [carousel]
- [Selects "More Info"]
* This hotel room has 3 bedrooms and two bathrooms. Any other questions?
   -> what: deluxe double bedroom
- How much does it cost?
   -> how much does deluxe double bedroom cost?
* 150$ a night - would you like to book it?
   -> action: book hotel room deluxe double bedroom
- Yes, let's do that
   -> Yes, lets do book hotel room with double bedroom
* [BOOKS]
- Do you have a casino?
* Yes
   -> what: casino
- How large is it?
   -> how large is casino?
```

## Contextual Information:
- who, what, value, where, when, action, timestamp

Basically find the subject/object of sentences using NLTK and POS tagging and such. Decide what in a sentence is "who" and "what" and "where" etc. Then when the user says "it", "then", "those" etc. refer back to those values.
Don't have a concrete plan on how to implement this. Might be very hard and error prone - better to use more closed prompts instead of free text (like user selects options, "Yes" and "No", etc.)

# Memory
Have a memory class where information can be stored short-term or long term.
For example if a user tells the bot where they live, it makes sense to store it in the memory. That way, the bot can check its memory next time, notice that that information is already in its memory and not have to ask again.
Also store cookies and session memory here (this is considered long-term memory.) Other things are only stored during one conversation or even just x amount of messages back and forth (short-term memory.)
