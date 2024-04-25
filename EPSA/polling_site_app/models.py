from django.db import models

class State(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=2)  # e.g., "CA", "NY"

    def __str__(self):
        return self.name

class County(models.Model):
    name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class CityOrTown(models.Model):
    name = models.CharField(max_length=255)
    county = models.ForeignKey(County, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class PollingSite(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city_or_town = models.ForeignKey(CityOrTown, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE) 
    zip_code = models.CharField(max_length=10)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name
