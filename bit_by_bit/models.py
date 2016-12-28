# Import field types to use in our class
from django.db import models


# Create a class representing an article
# To use real database you have to inherit your class from models.Model
class Article(models.Model):
    # Use statically typed fields now
    # Set primary_key to True to ensure all articles have different identifiers
    # Django adds primary key automatically, so we don't need to set up id manually
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=2048)

    # We don't need custom cunstructor anymore, it's built it by default
