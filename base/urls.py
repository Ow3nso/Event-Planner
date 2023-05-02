from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("Event/", views.EventList.as_view()),
    path("Event/<int:pk>", views.EventDetail.as_view()),
    path("yeargroup/", views.YearGroupList.as_view()),
    path("yeargroup/<int:pk>", views.YearGroupDetail.as_view()),
    path("Ministry/", views.MinistryList.as_view()),
    path("Ministry/<int:pk>", views.MinistryDetail.as_view()),
    path("Registration/", views.RegistrationList.as_view()),
    path("Registration/<int:pk>", views.RegistrationDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
