from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_no = models.PositiveIntegerField()
    CHOICES = [
        ('Guitar', 'Guitar'),
        ('Piano', 'Piano'),
        ('Drums', 'Drums'),
        ('Violin', 'Violin'),
        ('Flute', 'Flute'),
    ]
    instrument_type = models.CharField(choices=CHOICES, max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
