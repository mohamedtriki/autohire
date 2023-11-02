
from django.contrib import admin
from django.urls import path ,include
from django.conf.urls.static import static
from django.conf import settings
from user import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="landing"),
    path('reports/',views.reports,name="reports"),
    path('plans/',views.plans,name="plans"),
    path('logout_user/', views.logout_user ,name='logout_user'),
    path('chat/', views.chat ,name='chat'),
    path('feedback/', views.feedback ,name='feedback'),
    path('help/', views.help_page ,name='help'),
    path('uQLG4OK1MXogpBljOwIoqlOhn5DxUjwGjydUMfZths8VaNfUSr/', views.thanks, name='thanks'),
    path('mGHaeqG65TIuvUy2Y6RZ37yCAuk7sIaHvcvhcy5ZheFn4sAtM5/', views.thanks2, name='thanks2'),
    path('WgOJyfxMFhcDKDIi7eJv4hYzvJ7QpM2LcEMsDJv79pnD0PwTSE/', views.thanks3, name='thanks3'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout2/', views.checkout2, name='checkout2'),
    path('checkout3/', views.checkout3, name='checkout3'),
    path('reports/<report_image>/', views.report_chat,name='chat'),

]
urlpatterns+= staticfiles_urlpatterns()          
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
