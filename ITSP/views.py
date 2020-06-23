
from django.http import HttpResponse
from .models import Teams
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .serializers import TeamsSerializer

def homepage(request):
    return render(request=request , 
    	          template_name="ITSP/home.html",
    	          context={"teams": Teams.objects.all})
def team_detail_view(request, id):
    obj = get_object_or_404(Teams, Team_id=id)
    context = {
        "object": obj

    }
    print(object)
    return render(request, "ITSP/ITSP_detail.html", context)	



class TeamsViewSet(viewsets.ModelViewSet):
    queryset = Teams.objects.all().order_by('Team_name')
    serializer_class = TeamsSerializer