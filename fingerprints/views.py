from rest_framework.viewsets import ModelViewSet
from .models import CustomUser, Course, Attendance
from .serializers import CustomUserSerializer, CourseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .sendMessage import TeleMessages
import datetime
from rest_framework import permissions, status
from dotenv import dotenv_values
from .tasks import send_message

config = dotenv_values(".env")

# Create your views here.
class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)

class UserViewset(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsSuperUser]

class CourseViewset(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsSuperUser]

    def create(self, request, *args, **kwargs):
        new_course = Course.objects.create(
            name=request.data.get("name"),
            description=request.data.get("description"),
            price=request.data.get("price"),
            start_time=request.data.get("start_time"),
            end_time=request.data.get("end_time"),
            days=request.data.get("days"),
            telegram_group_id=request.data.get("telegram_group_id")
        )
        new_course.save()
        return Response({"details":"success"}, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        course = Course.objects.get(id=self.kwargs.get("pk"))
        course.name = request.data.get("name")
        course.description = request.data.get("description")
        course.price = request.data.get("price")
        course.start_time = request.data.get("start_time")
        course.end_time = request.data.get("end_time")
        course.days = request.data.get("days")
        course.telegram_group_id = request.data.get("telegram_group_id")
        course.save()
        return Response({"details":"success"}, status=status.HTTP_205_RESET_CONTENT)

class SendMessageView(APIView):
    permission_classes = [IsSuperUser]

    def get(self, request, *args, **kwargs):
        return self.send('--default', request.GET.get('id'))

    def post(self, request, *args, **kwargs):
        return self.send(request.data['message'], request.GET.get('id'))

    def send(self, message, pk):
        user = CustomUser.objects.get(id=pk)
        attendances = Attendance.get_todays_attendances(user)

        if len(attendances) <= 0:
            if message == '--default' or not message:
                message = f"{user.username} has entered ({user.type_user})"


            weekday = TeleMessages.get_weekday()
            courses = user.courses.filter(days__contains=weekday)

            for course in courses:
                send_message.delay(
                    message, course.telegram_group_id
                )

            if len(courses) == 0:
                send_message.delay(
                    f"{user.username} has entered ({user.type_user})", config.get("CHAT_ID")
                )

            new_attendance = Attendance.objects.create(person=user, day=datetime.datetime.now().date())
            new_attendance.save()
            Attendance.delete_previous_attendances()
            return Response({"success":True})
        else:
            return Response({"success":False, "details":"This person already entered today"}, status=status.HTTP_400_BAD_REQUEST)