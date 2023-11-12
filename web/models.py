from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class TimeSlotTag(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return self.title


class TimeSlot(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    start_date = models.DateTimeField(verbose_name='Время начала')
    end_date = models.DateTimeField(verbose_name='Время окончания')
    is_realtime = models.BooleanField(default=False, verbose_name='В реальном времени')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    tags = models.ManyToManyField(TimeSlotTag, verbose_name='Теги')
    image = models.ImageField(upload_to='time_slots/', null=True, blank=True, verbose_name='Картинка')


class Holiday(models.Model):
    date = models.DateField(verbose_name='Дата')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')