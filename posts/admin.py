from django.contrib import admin
# Importing our Post class from models.py
from .models import Post

# Registering our model with the admin site
admin.site.register(Post)
