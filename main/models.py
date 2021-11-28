from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Customer(models.Model):

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='customer')
    record = models.FloatField(verbose_name='Рекорд без задержки', default=0)
    record_delay = models.FloatField(verbose_name='Рекорд с задержкой', default=0)
    count = models.IntegerField(verbose_name='Количество капчей', default=0)
    all_time = models.FloatField(verbose_name='Всего времени', default=0)
    avg = models.FloatField(verbose_name='Среднее время', default=0)
    delay = models.IntegerField(verbose_name='Задержка', default=0)
    capKey = models.CharField(verbose_name='Клавиша капчи', default='KeyN', max_length=15)

    def __str__(self):
        return f'{self.user.username}'
