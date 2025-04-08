from django.db import models

# Model for storing festival data
class Festival(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    region = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

# Model for storing traditions data
class Tradition(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)  # Ensure this field exists
    description = models.TextField(null=True, blank=True)
    event_day = models.DateField(null=False, blank=False)  # New field to store the event day
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
