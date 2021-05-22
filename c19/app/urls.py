from django.urls import path
from . import views

# Create your urls here.
urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('archive_news/', views.archive_news, name='archive-news'),
    path('contact/', views.contact, name='contact'),
    path('donation/', views.donation, name='donation'),
    path('faq/', views.faq, name='faq'),
    path('infected/', views.infected, name='infected'),
    path('predictions/', views.predictions, name='predictions'),
    path('protection/', views.protection, name='protection'),
    path('single_news/', views.single_news, name='single_news'),
    path('slogin/', views.slogin, name='slogin'),
]