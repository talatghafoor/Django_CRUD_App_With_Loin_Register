from django.contrib import admin
from django.urls import path, include
from accounts import views as user_view
from django.contrib.auth import views as auth


from employee import views
 
urlpatterns = [
 
    path('admin/', admin.site.urls),
 
    ##### user related path########################## 
    path('', include('accounts.urls')),
    path('login/', user_view.Login, name ='login'),
    path('logout/', auth.LogoutView.as_view(template_name ='user/index.html'), name ='logout'),
    path('Register/', user_view.register, name ='Register'),
    path('show/', views.show, name='show'),
    path('emp', views.emp),  
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
 
]