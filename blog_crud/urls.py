from django.urls import include, path
from rest_framework import routers
from blog_crud.views import UserViewSet
from posts.views import PostViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
