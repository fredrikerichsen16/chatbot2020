import json
from mongo.collections.agents import Agent

class Endpoint():

    def __init__(self, bottle, api_key, convo_id = None, message = None):
        self.bottle = bottle
        self.api_key = api_key
        self.convo_id = convo_id

    def validate_api_key(self):
        agent = Agent.objects(id=self.api_key)

        if len(agent) == 0:
            raise self.bottle.HTTPResponse(
                body = json.dumps({ 'error': 'API key is invalid', 'tiss': agent.to_json() }),
                status = 400,
                headers = { 'Content-Type': 'application/json' },
            )

        self.agent_info = agent.as_pymongo()[0]

    def get_log(self):
        client = pymongo.MongoClient()
        db = client.chatbot2020

    def run(self):
        self.validate_api_key()

        generate_response = GenerateResponseHQ(self.bottle, self.api_key, self.convo_id, )

        if not self.convo_id:
            # start convo
            pass

        # self.get_log()

    def initiate_conversation(self):
        pass
