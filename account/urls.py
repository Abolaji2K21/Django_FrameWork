from django.urls import path

from account import views

urlpatterns = [
    path('accounts/', views.ListAccount.as_view()),
    path('accounts/<str:pk>/', views.account_details),
    path('deposit', views.deposit),
    path('withdraw', views.withdraw)

]
