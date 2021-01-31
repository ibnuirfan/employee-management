from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'employee', views.EmployeeViewSet)
router.register(r'appraisal', views.AppraisalViewSet)
router.register(r'department', views.DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.registerPage , name="register"),
    path('login/', views.loginPage , name="login"),
    path('logout/', views.logoutPage, name="logout"),  
    path('', views.emp, name="home"),  
    path('edit/<int:emp_id>/', views.edit, name='edit'),  
    path('update/<int:emp_id>', views.update, name='update'), 
    path('employee', include(router.urls)), 
]