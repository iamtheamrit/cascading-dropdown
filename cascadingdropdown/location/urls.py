from django.urls import path, include

from . import views

app_name = 'location'

urlpatterns = [
    path('', views.IndexPageView.as_view(),name="index"),
    path('state/', views.DistrictListByState.as_view(), name="district_list"),
    path('api/district/<int:pk>', views.village_list_by_district, name="village_list_by_district"),
]
