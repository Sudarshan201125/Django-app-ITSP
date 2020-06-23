from django.contrib import admin
from .models import Teams
from django.db import models


class TeamsAdmin(admin.ModelAdmin):
	fields = ["Team_name" ,
	 "Team_id" ,
	  "Team_members"] 

admin.site.register(Teams , TeamsAdmin)

# Register your models here.
