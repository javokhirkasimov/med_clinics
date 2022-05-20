from django.db import models


class Clinic(models.Model):
    WEEK_DAYS = [
        ('Пн', 'Понедельник'),
        ('Вт', 'Вторник'),
        ('Ср', 'Среда'),
        ('Чт', 'Четверг'),
        ('Пт', 'Пятница'),
        ('Сб', 'Суббота'),
        ('Вс', 'Воскресенье'),
    ]
    title = models.CharField(max_length=250, null=True)
    image = models.ImageField(upload_to='clinic_photo', null=True)
    phone_num = models.CharField(max_length=15, null=True)
    region = models.CharField(max_length=250, null=True)
    district = models.CharField(max_length=250, null=True)
    street = models.CharField(max_length=250, null=True)
    home_num = models.CharField(max_length=15, null=True)
    lat_long = models.CharField(max_length=255, null=True)
    open_time = models.TimeField()
    close_time = models.TimeField()
    start_day = models.CharField(null=True, max_length=25, choices=WEEK_DAYS)
    end_day = models.CharField(null=True, max_length=25, choices=WEEK_DAYS)

    def __str__(self):
        return self.title

    @property
    def address(self):
        return f"{self.region}, {self.district}, {self.street} {self.home_num}"
