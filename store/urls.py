from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.course_all, name='store_home'),
    path('', views.course_all, name='course_all'),
    path('<slug:slug>', views.course_detail, name='course_detail'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
]
