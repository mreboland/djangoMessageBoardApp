from django.test import TestCase
# Instead of using the view name directly, we can import reverse which wil aloows ur to refer the the named URL of 'home' instead. This is a better way as URL schemes can and do change over the course of a project however generally the named URL (home in this case) will most likely stay the same. It is better future proofing.
from django.urls import reverse
from .models import Post

# In previous example, we used SimpleTestCase as we weren't using a db. Now that we are using a db, we us TestCase.
# TestCase lets us create a 'test' db that we can check against. Which means we don't need to run tests on our actual db, but instead we can make a separate test db, fill it with data, then test against it.

class PostModelTest(TestCase):
    
    # This function creates a new db using our Post model that has just one entry
    def setUp(self):
        Post.objects.create(text="just a test")
        
    def test_text_content(self):
        # Here our variable post is getting the first object (id=1) of our db that was created in setUp
        # post is now a dictionary and text (set in setUp) is one of it's keys
        post = Post.objects.get(id=1)
        # We are saving the value of text (post.text is the key) to a new var to test agains't. We us f strings so we only get the string itself as it'll be given in list format if we don't.
        expected_object_name = f"{post.text}"
        # assertEqual compares our var in expected_object_name to the second argument. They have to be equal to get a pass.
        self.assertEqual(expected_object_name, "just a test")
        

class HomePageViewTestCase(TestCase):
    
    def setUp(self):
        Post.objects.create(text="this is another test")
        
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)
        
    def test_view_url_by_name(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)
        
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "home.html")
