from app1 import views
from django.urls import path,include

urlpatterns = [
    path('',views.add_show,name="addandshow"),
    path('delete/<int:id>/',views.delete_data,name="deletedata"),
    path('<int:id>/',views.update_data,name="updatedata")
]
