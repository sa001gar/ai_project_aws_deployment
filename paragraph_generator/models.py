# paragraph_generator/models.py
from django.db import models
from django.contrib.auth.models import User

# GeneratedContent Model : Here the GeneratedContent model is created with the following fields:
class GeneratedContent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # user field is a ForeignKey to the User model
    prompt = models.TextField() # prompt field is a TextField
    content = models.TextField() # content field is a TextField
    word_count = models.IntegerField() # word_count field is an IntegerField
    topic = models.CharField(max_length=200) # topic field is a CharField
    grade_level = models.CharField(max_length=50) # grade_level field is a CharField
    tone = models.CharField(max_length=50) # tone field is a CharField
    style = models.CharField(max_length=50) # style field is a CharField
    created_at = models.DateTimeField(auto_now_add=True) # created_at field is a DateTimeField
    
    # Meta Class : The Meta class is used to define the ordering of the GeneratedContent objects based on the created_at field in descending order.
    class Meta:
        ordering = ['-created_at']

    # __str__ Method : The __str__ method is used to return a string representation of the GeneratedContent object.
    def __str__(self):
        return f"Content by {self.user.username} at {self.created_at}"


# UserApiUsage Model : Here the UserApiUsage model is created with the following fields:
class UserApiUsage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # user field is a OneToOneField to the User model
    daily_usage = models.IntegerField(default=0) # daily_usage field is an IntegerField with a default value of 0
    last_reset = models.DateField(auto_now_add=True) # last_reset field is a DateField with auto_now_add set to True
    
    # __str__ Method : The __str__ method is used to return a string representation of the UserApiUsage object.
    def __str__(self):
        return f"API usage for {self.user.username}" 

# Feedback Model : Here the Feedback model is created with the following fields:
class Feedback(models.Model):
    name = models.CharField(max_length=100) # name field is a CharField
    feedback = models.TextField() # feedback field is a TextField
    RATING_CHOICES = [
        (1, '1 - Very Poor'),
        (2, '2 - Poor'),
        (3, '3 - Average'),
        (4, '4 - Good'),
        (5, '5 - Excellent'),
    ]
    rating = models.IntegerField(choices=RATING_CHOICES) # rating field is an IntegerField with choices defined in RATING_CHOICES
    created_at = models.DateTimeField(auto_now_add=True) # created_at field is a DateTimeField

    # Meta Class : The Meta class is used to define the ordering of the Feedback objects based on the created_at field in descending order.
    class Meta:
        ordering = ['-created_at']

    # __str__ Method : The __str__ method is used to return a string representation of the Feedback object.
    def __str__(self):
        return f"Feedback by {self.name} at {self.created_at}"