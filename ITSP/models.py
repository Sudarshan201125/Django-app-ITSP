from django.db import models


class Teams(models.Model):
    Team_name= models.CharField(max_length=200)
    Team_id = models.SlugField()
    Team_members = models.TextField()
    
    def _str_(self):
    	return self.tutorial_title
