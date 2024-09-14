from django.urls import path

from student import views

urlpatterns = [

    # student app urls
    path('',views.home,name='home'),
    path('display',views.display_studs,name='displaystudents'),
    path('add',views.add_studs,name='addstudent'),
    path('edit/<int:id>',views.edit_studs,name='editstudent'),
    path('delete/<int:id>',views.delete_studs,name='deletestudent'),
    # login system urls
    path('login',views.login_fun,name = 'login'),
    path('register',views.register_fun,name = 'register'),
    path('logout',views.logout_fun,name = 'logout')


]