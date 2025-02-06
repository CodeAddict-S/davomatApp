from django.db import models
from multiselectfield import MultiSelectField
from dotenv import dotenv_values
import datetime

config = dotenv_values(".env")

# Create your models here.
class Course(models.Model):
    days_choices = models.TextChoices('days', 'mon tue wed thu fri sat sun')

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.BigIntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    days = MultiSelectField(choices=days_choices)
    telegram_group_id = models.TextField()

    def __str__(self):
        return self.name 
    
class CustomUser(models.Model):
    types = models.TextChoices("Types", "student employee")

    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    type_user = models.CharField(choices=types, max_length=25)
    courses = models.ManyToManyField('fingerprints.Course', related_name='users', blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            ids = []
            for user in CustomUser.objects.all():
                ids.append(user.id)
            ids.sort()
            for i in range(1, int(config.get('MAX_USERS'))):
                if not (i in ids):
                    self.id = i
                    super().save(*args, **kwargs)
                    return
            raise BaseException("No more space")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

class Attendance(models.Model):
    person = models.ForeignKey('fingerprints.CustomUser', on_delete=models.CASCADE)
    day = models.DateField()

    def __str__(self):
        return str(self.day) + " / " + self.person.username
    
    @staticmethod
    def get_todays_attendances(user):
        attendances = Attendance.objects.filter(day=datetime.datetime.now().date()).filter(person=user)
        return attendances
    
    @staticmethod
    def delete_previous_attendances():
        attendances = Attendance.objects.exclude(day=datetime.datetime.now().date())
        attendances.delete()
        return attendances