# To show custom tables in admin panel use function from `admin` module
from django.contrib import admin
from .models import Article


# Register your model here
admin.site.register(Article)
