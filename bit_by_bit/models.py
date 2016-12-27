# Import field types to use in our class
from django.db import models


# Create a class representing an article
class Article:
    # Use statically typed fields now
    # Set primary_key to True to ensure all articles have different identifiers
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=2048)

    # Constructor has been using to create a new instance of the class
    def __init__(self, title, content, id):
        # Add article identifier, we'll use it in our html template
        self.id = id
        self.title = title
        self.content = content
