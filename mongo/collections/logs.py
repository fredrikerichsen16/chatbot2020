from mongoengine import *
import env

connect(env.mongodb_dbname, host=env.mongodb_host, port=env.mongodb_port)

class Interaction(EmbeddedDocument):
    name = StringField(required = True, maxlength = 100)
    span = ListField(maxlength = 2, default = [None, None])
    entities = DictField(default = {})

class Log(Document):

    messages = ListField()
    memory = DictField()
    interactions = EmbeddedDocumentListField(Interaction)

# -------------
# TRASH
# -------------
# """
# The below are messages that go in the 'messages' embedded document list field in Log
# There are different types of messages so we need to define different types that all inherit
# from Message
#
# """
#
# # USER FREE TEXT INPUT
# class UserFreeTextInputMessage(EmbeddedDocument):
#     sender = StringField(choices=('bot', 'user'))
#     message = EmbeddedDocumentField(UserFreeTextInputMessageMSG)
#
# class UserFreeTextInputMessageMSG(EmbeddedDocument):
#     text = StringField(maxlength = 255)
#     type = StringField(maxlength = 50, default = 'free-text')
#     d = EmbeddedDocumentField(D)
#
# class D(EmbeddedDocument):
#     domain = StringField(maxlength = 100)
#     intent = StringField(maxlength = 100)
#     entities = DictField()
#
# class UserSelectOptionMessage(EmbeddedDocument):
#     sender = StringField(choices=('bot', 'user'))
#     message = EmbeddedDocumentField(UserFreeTextInputMessageMSG)
#
# class UserFreeTextInputMessageMSG(EmbeddedDocument):
#     text = StringField(maxlength = 255)
#     type = StringField(maxlength = 50, default = 'free-text')
#     d = EmbeddedDocumentField(D)
#
# class UserSelectOptionMessage(Message):
#     message = StringField(maxlength = 255)
#     type = StringField(maxlength = 50)
#     d = EmbeddedDocumentField(D)
#
# ---------------------------------------------------------------------
#
# interaction = Interaction(name='book-flight', span=[0, None], entities={'from-city': 'Amsterdam'})
# log = Log(
#     messages=[{
#         'sender': 'user',
#         'message': {
#             'type': 'text',
#             'text': 'I want a flight from Schipol airport',
#         },
#         'd': {
#             'domain': 'flights',
#             'intent': 'book',
#             'entities': {
#                 'from-city': 'Amsterdam'
#             }
#         }
#     }],
#     interactions=[interaction],
#     memory={'user-location': 'Alkmaar'}
# )
# log.save()
