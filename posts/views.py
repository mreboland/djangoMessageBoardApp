# Importing ListView which is a page representing a list of objects
from django.views.generic import ListView
# Importing our model Post
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = "home.html"
