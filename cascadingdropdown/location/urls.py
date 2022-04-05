from django.urls import path, include

from . import views

app_name = 'location'

urlpatterns = [
    path('', views.IndexPageView.as_view(),name="index"),
    path('api/', include([
        path('state/', views.DistrictListByState.as_view(), name="district_list"),
        path('district/', views.VillageListByDistrict.as_view(), name="village_list"),
    ])
    )
]
