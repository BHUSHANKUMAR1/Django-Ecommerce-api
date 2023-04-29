from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers, serializers, viewsets
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path("home", views.index, name='home'),
    path("contactus", views.contact, name='contact'),
    path("signup", views.user_registration, name='signup'),
    path("login", views.login, name='login'),
    path("logout", views.logout, name='logout'),
    path("cart", views.cart, name='cart'),
    path("checkout", views.Checkout, name='checkout'),
    path('Order_dtls', views.Order_dtls, name='Order_dtls'),
    path('find', views.find, name='find'),
    path('clear_table', views.clear_table, name='clear_table'),
    path('order_history', views.order_history, name='order_history'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
