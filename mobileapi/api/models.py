from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=255)
    worker = models.ForeignKey(
        Worker,
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self) -> str:
        return self.name


class Visit(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self) -> str:
        return f'{self.datetime} ~ {self.latitude} {self.longitude}'
