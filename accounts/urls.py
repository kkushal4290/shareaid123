from knox import views as knox_views
from .views import RegisterAPI ,ChangePasswordView,user_notification
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import LoginAPI , RegisterAPI , getuser , getprofile,updateprofile
urlpatterns = [
    path('register', RegisterAPI.as_view(), name='register'),
    path('login', LoginAPI.as_view(), name='login'),
    path('logout', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('change-password', ChangePasswordView.as_view(), name='change-password'),
    path('notifications', user_notification, name='user_notification'),
    path('user/<int:id>', getuser, name='getuser'),
    path('profile', getprofile, name='getprofile'),
    path('profile/update', updateprofile, name='updateprofile'),

]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)