from django.urls import path
from chat import views

urlpatterns = [
    path('signup/', views.signuppage, name='signup'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),

    path('', views.index, name='home'),
    path('chat/<str:username>/', views.chat_page, name='chat_page'),
]
