from mongoengine import *
import env

connect(env.mongodb_dbname, host=env.mongodb_host, port=env.mongodb_port)

class Agent(DynamicDocument):
    pass
