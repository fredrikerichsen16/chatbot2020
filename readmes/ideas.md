### AUTO-CORRECT AND AUTOCOMPLETE
Like on iPhone. Autocorrect and three word options n shit.

### GIVE INTENTS A PROBABILITY SCORE
On top of the score given simply by running the query through a
neural network, give intents a score based on additional factors.
Such as the following:
- whether the intent is active or not:
  for example, the intent massage.price is not active
  for a hotel that doesn't offer massages
- how common the intent is
  log every message and its intent
- how common the intent is marked as "appropriate":
  green checkmark next to message
- the domain of the previous few messages
  obvious context reasons

### CONVERSATION
When the user initiates a conversation with the chatbot, a convo_id is generated and the website providing the chatbot has a secret api_key. The api_key and convo_id are sent to our backend through the API. The api_key is used to verify that the request is coming through an authorized channel (i.e. one of our customers.) The database info is stored with the convo_id.
