from django.db import models

# Create your models here.

# Create a new db model called Post which has a db field of 'text'. We also specified the type of content it will hold with TextField() (self-explanatory name)
class Post(models.Model):
    text = models.TextField()
    
    # The below code will allow us to show what we wrote in the var 'text' in our admin dashboard
    # Instead of "Post object (1)", it'll show what we wrote, "Hello, World!"
    # [:50] is a slice that'll limit what is shown to 50 characters
    def __str__(self):
        return self.text[:50]