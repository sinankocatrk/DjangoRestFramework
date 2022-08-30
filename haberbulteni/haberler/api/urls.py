from django.urls import path
from haberler.api import view_ilk as api_views


urlpatterns = [

    path('makaleler/',api_views.makale_list_create_api_view, name='makale-listesi'),

]
