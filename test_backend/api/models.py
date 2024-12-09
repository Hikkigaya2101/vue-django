from django.db import models
from treebeard.mp_tree import MP_Node

class UnitType(models.Model):
    name = models.CharField(max_length=255,verbose_name='Тип подразделения')

    def __str__(self):
        return self.name


# class Unit(models.Model):
#     name = models.CharField(max_length=255, verbose_name='Название')
#     parent = models.ForeignKey("self",null=True,on_delete=models.PROTECT,verbose_name="Родитель",related_name="children")
#     type = models.ForeignKey(UnitType,
#                              null=True,
#                              on_delete=models.PROTECT,
#                              verbose_name='Тип подразделения')
#     def __str__(self):
#         return self.name


class Unit(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    type = models.ForeignKey(UnitType,on_delete=models.PROTECT,verbose_name='Тип подразделения')

    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                                        null= True,
                                        related_name='children',
                                        verbose_name="Родитель")
    #node_order_by = ['name']
    #def __str__(self):
    #    return 'Category: {}'.format(self.name)

class Consumer(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    unit = models.ForeignKey(Unit, null=True, on_delete=models.PROTECT, verbose_name='Подразделение')
    data_birthday = models.DateField(verbose_name='День рождения')
    data_workday = models.DateField(verbose_name='День выхода на работу')
    consumer_avatar = models.ImageField(upload_to='uploads')

    def __str__(self):
        return self.name

