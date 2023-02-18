from django.db import models


class BaseSupplier(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(verbose_name="Название", max_length=30)
    debt = models.DecimalField(verbose_name="Задолженность", max_digits=10, decimal_places=2)
    created = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    contacts = models.ForeignKey("Contacts", on_delete=models.DO_NOTHING, blank=True, null=True)
    products = models.ForeignKey("Products", on_delete=models.DO_NOTHING, blank=True, null=True)


class Products(models.Model):
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    name = models.CharField(verbose_name="Название", max_length=20)
    type = models.CharField(verbose_name="Модель", max_length=30)
    date_issue = models.DateTimeField(verbose_name="Дата выхода продукта на рынок")


class Contacts(models.Model):
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    email = models.EmailField(verbose_name="Email", max_length=50)
    country = models.CharField(verbose_name="Страна", max_length=30)
    city = models.CharField(verbose_name="Город", max_length=30)
    street = models.CharField(verbose_name="Улица", max_length=30)
    home_number = models.IntegerField(verbose_name="Номер дома")


class Factory(BaseSupplier):
    class Meta:
        verbose_name = "Завод"


class RetailNetwork(BaseSupplier):
    class Meta:
        verbose_name = "Розничная сеть"

    supplier = models.ForeignKey(Factory, on_delete=models.DO_NOTHING, blank=True, null=True)


class IP(BaseSupplier):
    class Meta:
        verbose_name = "Предприниматель"

    supplier = models.ForeignKey(RetailNetwork, on_delete=models.DO_NOTHING, blank=True, null=True)
