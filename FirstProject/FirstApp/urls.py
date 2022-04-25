from django.urls import path
from . import views

urlpatterns = [
    path('addemp/',views.addEmployeeModelForm,name='add_emp'),
    path('showemp/',views.showEmployee,name='show_emp'),
    path('delete/<int:i>/',views.deleteEmployee,name="delete_emp"),
    path('update/<int:i>/',views.updateView,name="update_emp"),
]