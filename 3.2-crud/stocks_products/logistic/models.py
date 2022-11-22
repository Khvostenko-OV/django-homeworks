from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    title = models.CharField('Наименование', max_length=60, unique=True)
    description = models.TextField('Описание', null=True, blank=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


class Stock(models.Model):
    address = models.CharField('Адрес', max_length=200, unique=True)
    products = models.ManyToManyField(
        Product,
        through='StockProduct',
        related_name='stocks',
        verbose_name='Продукт',
    )

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'

    def __str__(self):
        return self.address


class StockProduct(models.Model):
    stock = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE,
        related_name='positions',
        verbose_name='Склад',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='positions',
        verbose_name='Продукт',
    )
    quantity = models.PositiveIntegerField('Количество', default=1)
    price = models.DecimalField('Цена',
        max_digits=18,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )

    class Meta:
        unique_together = ['stock', 'product']
        verbose_name = 'Продукт на складе'
        verbose_name_plural = 'Продукты на складе'

    def __str__(self):
        return f'{self.stock} - {self.product}'
