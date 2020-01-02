# Terminology

### MESSAGE TRANSFER
- api_key
- convo_id
- msg_log

### PARSE INPUT
- NLTK
- POS tagging

### INTENT RECOGNITION
- Domain
- Intent
- Entities
- Training sentence

### Keywords
- Keyword
- Staticword/statword
- Two types of keyword/statword:
    - Function-based
    - Text-based
- Value
    - Keyword = @country, values = "USA", "Norway", "China",
- Synonym
    - The keyword value @country.'USA' can have many synonyms: "United States", "US", "U.S.A." etc.
    - The keyword itself can have synonyms. In that case it is a staticword. For example there are many ways to refer to the keyword @wifi, so you define the synonyms: wi-fi, internet, wifi connection, broadband, etc.

### RESPONSE GENERATION
- CRUD offloading (read more in crud.md)
- (???) - The name of the function that corresponds to a specific intent
