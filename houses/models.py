from django.db import models

class House(models.Model):
    house_name = models.CharField('Название', max_length=20)
    house_description = models.TextField('Описание',)
    house_area = models.PositiveSmallIntegerField('Площадь дома', default=100)

    class Meta:
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'

    def __str__(self):
        return self.house_name
