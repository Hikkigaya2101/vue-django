from django.db import models

class UnitType(models.Model):
    name = models.CharField(max_length=255,verbose_name='Тип подразделения')

    def __str__(self):
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=255,verbose_name='Название')
    parent = models.ForeignKey("self",null=True, on_delete=models.PROTECT,verbose_name='Родитель')
    type = models.ForeignKey(UnitType,null=True, on_delete=models.PROTECT,verbose_name='Тип подразделения')

    def __str__(self):
        return self.name
class Consumer(models.Model):
    name = models.CharField(max_length=255,verbose_name='Имя')
    unit = models.ForeignKey(Unit,on_delete=models.PROTECT,verbose_name='Подразделение')
    data_birthday = models.DateField(verbose_name='День рождения')
    data_workday = models.DateField(verbose_name='День выхода на работу')

    def __str__(self):
        return self.name

