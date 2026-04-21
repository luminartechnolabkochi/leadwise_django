
from django.urls import path
from api.views import LeadListCreateView,LeadRetrieveUpdateDeleteView

urlpatterns=[

    path("leads/",LeadListCreateView.as_view()),

    path("leads/<int:pk>/",LeadRetrieveUpdateDeleteView.as_view()),
    

]