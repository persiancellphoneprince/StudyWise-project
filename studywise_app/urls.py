from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.home_page, name = "home_page"),
    path('offers/', views.offers_page, name="offers_page"),
    path('subjects/', views.subjects_page, name="subjects_page" ),
    path('favourites/', views.favourites_page, name='favourites_page'),
    path('offer/detail/<int:pk>/', views.offer_detail_page, name="offer_detail_page"),
    path('favourite/detail/<int:pk>/', views.favourite_detail_page, name="favourite_detail_page"),
    path('subject/jobs/<slug:slug>/', views.offers_by_subject_page, name = 'offers_by_subject_page'),
    path('sign_up/', views.sign_up_page, name = 'sign_up_page'),
    path('login/', views.login_page, name = 'login_page'),
    path('logout/', views.logout_action, name = 'logout_action')
]