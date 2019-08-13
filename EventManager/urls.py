from django.urls import path, include
from django.conf.urls import url
from EventManager import views, admin
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('secret/', views.secret_page, name='secret'),
    path('secret2/', views.SecretPage.as_view(), name='secret2'),
    path('event_view',views.Event_View.as_view(),name='Event_View'),
    path('event_add',views.Event_Create.as_view(),name='event_add'),
    path('<int:pk>/event_edit/',views.Event_Update.as_view(),name='event_edit'),


    url(r'^getEvent',views.getEvent,name='getEvent'),
    url(r'^Index',views.Index,name='Index'),

    url('^login_view/', views.login_view, name='login_view'),
]

