from django.urls import path, include
from .views import CourseViewset, UserViewset, SendMessageView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewset, basename='user')
router.register(r'courses', CourseViewset, basename='course')

urlpatterns = [
    path('', include(router.urls)),
    path('message/<int:pk>', SendMessageView.as_view(), name="send"),
    path('message/', SendMessageView.as_view(), name="send")
]