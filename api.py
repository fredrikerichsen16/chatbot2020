"""
API endpoint. User inputs data from front-end to this endpoint through AJAX.

"""
import bottle
from endpoint import Endpoint

def jsonp(dictionary):
    """
    Return response dictionary in JSONP format. Required format for
    cross-origin AJAX get request to work.

    """
    import json

    callback = B.request.query.callback
    dictionary = json.dumps(dictionary)
    return "{}({})".format(callback, dictionary)

@bottle.route('/endpoint/<api_key>')
def endpoint(api_key):
    """
    User clicks "Start Conversation" or enters chat and initiates
    conversation. Bot returns welcome/init message like "Welcome to this bot".

    """
    ep = Endpoint(bottle, api_key)

    result = ep.run()

    return jsonp(result)

@bottle.route('/endpoint/<api_key>/<convo_id>/<message>')
def endpoint(api_key, convo_id, message):
    """
    User clicks "Start Conversation" or enters chat and initiates
    conversation. Bot returns welcome/init message like "Welcome to this bot".

    """
    ep = Endpoint(bottle, api_key, convo_id, message)

    result = ep.run()

    return jsonp(result)

# @B.route('/endpoint/user_input/<api_key>/<convo_id>/<user_input>')
# def send_msg(api_key, convo_id, user_input):
#     from main.chat import Chat
#     chat = Chat(
#         user_input=user_input,
#         api_key=api_key,
#         convo_id=convo_id
#     ).get_response().returnDictionary(
#         containing=['msg_log', 'intent_obj', 'bot_responses']
#     )
#
#     return jsonp(chat)


bottle.run(host='localhost', port=8000)
