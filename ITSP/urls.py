from django.urls import include, path
from rest_framework import routers
from . import views 
#from .views import (team_detail_view , homepage)
app_name="ITSP"

router = routers.DefaultRouter()
router.register(r'Teamss', views.TeamsViewSet)

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('api', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('<slug:id>/' , views.team_detail_view , name='ITSP_detail'),
]


