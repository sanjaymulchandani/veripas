from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

# urls start here
router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_custom, name='logout'),
    path('user-details/', views.user_details_list, name='user-details'),
    path('user-details/create/', views.create_user_details, name='user-details-create'),
    path('user-details/update/<int:pk>/', views.update_user_details, name='user-details-update'),
    path('user-details/delete/<int:pk>/', views.delete_user_details, name='user-details-delete'),

    # Include the API URLs under a separate path
    path('api/user-details/', views.UserDetailListCreateView.as_view(), name='user-details-api-list'),
    path('api/', include(router.urls)),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)