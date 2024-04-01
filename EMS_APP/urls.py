from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('emp_signup/',views.emp_signup,name='emp_signup'), # here name is emp_signup so in link you have to give {url emp_signup}
    path('emp_login/',views.emp_login,name='emp_login'),
    path('emp_home/',views.emp_home,name='emp_home'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.Logout, name='logout'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('my_experience/',views.my_experience,name='my_experience'),
    path('edit_experience/',views.edit_experience,name='edit_experience'),
    path('my_education/',views.my_education,name='my_education'),
    path('edit_education/',views.edit_education,name='edit_education'),
    path('change_password/',views.change_password,name='change_password'),

    
    path('admin_index/',views.admin_index,name='admin_index'),
    path('admin_change_password/',views.admin_change_password,name='admin_change_password'),
    path('admin_all_employee/',views.admin_all_employee,name='admin_all_employee'),
    path('admin_edit_profile/<int:pid>',views.admin_edit_profile,name='admin_edit_profile'),
    path('admin_delete_employee/<int:pid>',views.admin_delete_employee,name='admin_delete_employee'),
    path('admin_edit_education/<int:pid>',views.admin_edit_education,name='admin_edit_education'),
    path('admin_edit_experience/<int:pid>',views.admin_edit_experience,name='admin_edit_experience'),
    
]