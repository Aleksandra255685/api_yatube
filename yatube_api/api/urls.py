from rest_framework import routers
from django.urls import include, path
from rest_framework.authtoken import views
from .views import PostViewSet, GroupViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('groups', GroupViewSet, basename='group')
router.register(r'posts/(?P<post_id>.+)/comments',
                CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
