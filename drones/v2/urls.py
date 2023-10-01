from django.urls import path
from .. import views
from . import views as views_2

app_name = "v2"
urlpatterns = [
    path("vehicle-categories/", views.DroneCategoryList.as_view(), name=views.DroneCategoryList.name),
    path("vehicle-categories/<int:pk>/", views.DroneCategoryDetail.as_view(), name=views.DroneCategoryDetail.name),
    path("vehicles/", views.DroneList.as_view(), name=views.DroneList.name),
    path("vehicles/<int:pk>/", views.DroneDetail.as_view(), name=views.DroneDetail.name),
    path("pilots/", views.PilotList.as_view(), name=views.PilotList.name),
    path("pilots/<int:pk>/", views.PilotDetail.as_view(), name=views.PilotDetail.name),
    path("competitions/", views.CompetitionList.as_view(), name=views.CompetitionList.name),
    path("competitions/<int:pk>/", views.CompetitionDetail.as_view(), name=views.CompetitionDetail.name),
    path("", views_2.ApiRootVersion2.as_view(), name=views_2.ApiRootVersion2.name)
]
