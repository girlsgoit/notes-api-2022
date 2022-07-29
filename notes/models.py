from django.contrib.auth.models import AbstractUser
from django.db import models


# Create User model
class GGITUser(AbstractUser):
    pass

# Create Note model
class Note(models.Model):
    user = models.ForeignKey(GGITUser, on_delete = models.CASCADE, related_name = 'notes')
    created_at = models.DateField(auto_now = True)

# Create Note Element model
class NoteElement(models.Model):
    note = models.ForeignKey(Note, on_delete = models.CASCADE, related_name = 'note_elements')
    tag = models.TextField()
    content = models.TextField()



