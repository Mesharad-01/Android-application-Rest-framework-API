from django.urls import path
from .views import myimagedetailsView, myimageView,allmyimagedetailsView


urlpatterns = [
    path('myimage/', myimageView.as_view(),name='myimageView'),
    path('myimage/<int:id>/', myimagedetailsView.as_view(),name='myimagedetailsView'),
    path('myimage/all/<int:my_id>/', allmyimagedetailsView.as_view(),name='allmyimagedetailsView'),   
]




