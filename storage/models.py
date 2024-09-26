from django.db import models
from accounts.models import NewUser

# Create your models here.
class File(models.Model):
    sent_by = models.ForeignKey(NewUser, on_delete=models.CASCADE, related_name='sender', blank=True, null=True)
    recieved_by = models.ForeignKey(NewUser, on_delete=models.CASCADE, related_name='reciever', blank=True, null=True)
    encrypted_file = models.TextField()
    notified = models.BooleanField(default=False)