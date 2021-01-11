from django.db import models
from Account.models import custom_user_model
# Create your models here.

status = (
    ('Bought','Bought'),
    ('Pending','Pending'),
    ('Not Available', 'Not Available')
)

class Bag(models.Model):
    username = models.ForeignKey(custom_user_model,on_delete=models.CASCADE)
    item_name = models.CharField(max_length=20)
    item_quantity = models.CharField(max_length=20)
    item_status = models.CharField(max_length=20,choices=status)
    date = models.DateField()

    def __str__(self):
        return str(self.username)
    

