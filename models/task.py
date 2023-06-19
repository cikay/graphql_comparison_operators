from mongoengine import Document, StringField, DateTimeField

class Task(Document):
    content = StringField(required=True)
    created_at = DateTimeField(required=True)
    updated_at = DateTimeField(required=True)
