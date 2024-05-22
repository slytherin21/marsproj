from django.urls import path
from . import views
from .views import profile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('team/', views.team, name='team'),
    path('bmi-calculator.html', views.bmi, name='bmi-calculator'),  # Add this line for the BMI calculator
    path('about-us/', views.about, name='about-us'),
    path('class-details/', views.classdetail, name='class-details'),
    path('services/', views.services, name='services'),
    path('class-timetable/', views.classtimetable, name='class-timetable'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),  # Define 'blog' URL pattern
    path('contact/', views.contact, name='contact'),
    path('blog-details/', views.blogdetails, name='blog-details'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profilenew/', views.profilenew, name='profilenew'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 