from django.db import models
from django.contrib.auth.models import User
from PIL import  Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self): # This is the method that gets run after our model is saved.
        super().save() # To run the save method 

        # Get the image it saved and resize it
        img = Image.open(self.image.path) # Open the image of the current instance.

        # First, check if the image is more than 300px
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path) # Save the image to the same path to override the oversize image