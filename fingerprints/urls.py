from django.urls import path, include
from .views import CourseViewset, UserViewset, SendMessageView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewset, basename='user')
router.register(r'courses', CourseViewset, basename='course')

urlpatterns = [
    path('api/', include(router.urls)),
    path('fingerprints/detect/', SendMessageView.as_view(), name="send"),
]