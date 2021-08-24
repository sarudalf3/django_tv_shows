from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    
    def validate(self, postData):
        errors = {}
        if len(postData['title'])<2:    
            errors['length_title'] = "Check the TV show title, it's too short"
        if len(postData['description'])<10:
            errors['length_desc'] = "Check the TV show description, it's too short"
        if postData['release'] > datetime.now().strftime('%Y-%m-%d'):
            errors['release_date'] = "Check the TV show release, it's more than today"    
        return errors

class NetworkManager(models.Manager):
    
    def validate(self, postData):
        errors = {}
        if len(postData['network'])<2:
            errors['length_network'] = "Check the TV show network, it's too short"
        return errors

class Network(models.Model):
    network = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = NetworkManager() #Validate Data

    def __str__(self):
        return f"{self.network}"
    
    def __repr__(self):
        return f"{self.network}"
        
class Show(models.Model):
    title = models.CharField(max_length=150)
    network = models.ForeignKey(Network, related_name="shows",on_delete = models.CASCADE)
    release = models.DateField()
    description = models.TextField(null=True)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager() #Validate data

    def __str__(self):
        return f"{self.title} ({self.network.network})"
    
    def __repr__(self):
        return f"{self.title} ({self.network.network})"