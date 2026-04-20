
from django.urls import path
from api.views import LeadListCreateView

urlpatterns=[

    path("leads/",LeadListCreateView.as_view()),

]