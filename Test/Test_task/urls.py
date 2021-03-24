# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.Users, name='List of Users'),
#     path('Groups/', views.Groups, name='List of Groups for Users'),
# ]

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('addnew', views.addnew, name='addnew'),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
]
