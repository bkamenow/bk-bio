from django.urls import path
from .views import HomeView, AboutMeView, MyJourneyView, SkillsView, WorkView, ContactsView

app_name = 'web'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutMeView.as_view(), name='about_me'),
    path('journey/', MyJourneyView.as_view(), name='my_journey'),
    path('skills/', SkillsView.as_view(), name='skills'),
    path('work/', WorkView.as_view(), name='work'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
]
