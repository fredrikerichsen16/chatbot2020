# CRUD Offloading

Put CRUD operations into the hands of customer
    - E.g. CB can’t access banks DB so can’t send money etc. (An API can only return data, not manipulate client's db). So in return package for example write todo: transfer(), with data provided by user (amount, currency, recipient etc.)
    - Then company creates all these methods that are used in their own python file with a specific format and parameters etc. defined in the documentation. Make it easy to work with, even auto-generate methods if they’re simple based on for example database name and field etc provided by company.

```
# This is the method for the intent transfers.execute_transfer (in Alfred's codebase)
def transfers_execute_transfer():
    bot_response = {
        offload: {
            'method': 'transfers_execute_transfer',
            'data': {
                'sender': entities['sender'],
                'recipient': entities['recipient'],
                'amount': entities['amount'],
                'currency': entities['currency'],
            }
        }
    }

    return bot_response

...

Now an AJAX request is sent to the bank's backend with the bot response,
The method on their backend looks something like this:
(The parameter)

def transfers_execute_transfer(sender, recipient, amount, currency):
    recipientAccountObj = BankAccount.get(IBAN=recipient)
    transaction = send_money(sender, recipientAccountObj, amount, currency)

    status = transaction.status
    retObj = {
        'status': status
    }

    # Invent some status code numbers, don't use HTTP's. But like 1 = success, 2 = couldn't fetch data, 3 = couldn't connect to database etc., 4 = couldn't find bank account with that IBAN
    if(status == 200):
        retObj['recipient'] = recipientAccountObj

    return retObj

...

Now an AJAX request is sent back to Alfred's codebase into a method that looks something like this:
def transfers_execute_transfer_post(): # Like the method name is the same, but with '_post' added for post-work.
    status = remote_data['status']

    if(status == 200):
        return "You successfully sent {amount} {currency} to {recipient_name}".format(
            amount=remote_data['amount']
            currency=remote_data['currency']
            recipient_name=remote_data['recipient']['name']
        )
    elif(status == 404):
        return "Could not find a bank account with the IBAN provided." (Next prompt to user: Button saying "What is IBAN?" OR they can just insert text. Like a double option. Pure text or button. New prompt type.)
    else:
        return "Unknown error"

```

## Also other ideas:
- Don’t hard code the interaction trees, create an interface to create them based on company data etc, be slightly customizable
- In the chat window have suggestions for messages user can type like Siri has (and transition between list of like 5 sentences so 15 suggestions total)
- Interaction tree shouldn’t be a multi-dimensional array but rather a LinkedList kinda thing. Like a list of dictionaries each with an id and previous_id/next_id kinda thing. So it’s ez to go down the tree and back up etc.
