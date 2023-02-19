from django.db import models


class Link(models.Model):
    class Meta:
        verbose_name = "Звено сети"
        verbose_name_plural = "Звенья сети"

    class Level(models.IntegerChoices):
        Factory = 1, 'Завод'
        NetworkRetailer = 2, 'Розничная сеть'
        IP = 3, 'Индивидуальный предприниматель'

    title = models.CharField(verbose_name="Название", max_length=30)
    level = models.PositiveSmallIntegerField(verbose_name='Вид звена', choices=Level.choices)
    debt = models.DecimalField(verbose_name="Задолженность", max_digits=10, decimal_places=2, default=0)
    created = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    email = models.EmailField(verbose_name="Email", max_length=50)
    country = models.CharField(verbose_name="Страна", max_length=30)
    city = models.CharField(verbose_name="Город", max_length=30)
    street = models.CharField(verbose_name="Улица", max_length=30)
    home_number = models.IntegerField(verbose_name="Номер дома")
    supplier = models.ForeignKey('self', verbose_name="Поставщик", null=True, blank=True, on_delete=models.SET_NULL)
    products = models.ForeignKey("Products", on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.title


class Products(models.Model):
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    name = models.CharField(verbose_name="Название", max_length=100)
    type = models.CharField(verbose_name="Модель", max_length=50)
    date_issue = models.DateTimeField(verbose_name="Дата выхода продукта на рынок")

    def __str__(self):
        return f'{self.name} {self.type}'


class LinkProducts(models.Model):
    """ Вывод товара в несколько строк """

    products = models.ForeignKey('Products', on_delete=models.CASCADE)
    link = models.ForeignKey('Link', on_delete=models.CASCADE)


# class Contacts(models.Model):
#     class Meta:
#         verbose_name = "Контакт"
#         verbose_name_plural = "Контакты"
#
#     email = models.EmailField(verbose_name="Email", max_length=50)
#     country = models.CharField(verbose_name="Страна", max_length=30)
#     city = models.CharField(verbose_name="Город", max_length=30)
#     street = models.CharField(verbose_name="Улица", max_length=30)
#     home_number = models.IntegerField(verbose_name="Номер дома")


# class Factory(BaseSupplier):
#     class Meta:
#         verbose_name = "Завод"
#
#
# class RetailNetwork(BaseSupplier):
#     class Meta:
#         verbose_name = "Розничная сеть"
#
#     supplier = models.ForeignKey(Factory, on_delete=models.DO_NOTHING, blank=True, null=True)
#
#
# class IP(BaseSupplier):
#     class Meta:
#         verbose_name = "Предприниматель"
#
#     supplier = models.ForeignKey(RetailNetwork, on_delete=models.DO_NOTHING, blank=True, null=True)
