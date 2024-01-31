
from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(max_length=100, verbose_name='Описание')


    def __str__(self):
        return f'{self.name} ({self.description})'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(max_length=100, verbose_name='Описание')
    image = models.ImageField(upload_to='product/', verbose_name='Картинка', **NULLABLE)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    create_date = models.DateTimeField(db_comment="Дата создания")
    last_modified_date = models.DateTimeField(db_comment='Дата последнего изменения')

    def __str__(self):
        return f'{self.name} {self.description} {self.price} {self.create_date} {self.last_modified_date}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
