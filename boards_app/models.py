from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Constants:
    Board_Type = (
        ('public', 'Team Board'),
        ('private', 'Personal Board'),
    )


class Board(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='board_owner', on_delete=models.CASCADE)
    type =  models.CharField(max_length=30, choices=Constants.Board_Type, default='public')