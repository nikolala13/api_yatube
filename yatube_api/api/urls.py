from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter
from .views import CommentViewSet, GroupViewSet, PostViewSet

router_v1 = SimpleRouter()
router_v1.register(r'posts', PostViewSet)
router_v1.register(r'groups', GroupViewSet)
router_v1.register(
    r'posts/(?P<post_id>[^/.]+)/comments',
    CommentViewSet,
    basename='Comment'
)

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('', include(router_v1.urls)),
]
