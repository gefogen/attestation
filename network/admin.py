from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from network.models import Link, Products, LinkProducts


class ProductsInline(admin.StackedInline):
    """ Вывод нескольких строк для поля product """

    model = LinkProducts
    extra = 0


class BaseLinkAdmin(admin.ModelAdmin):
    """ Админ-панель для работы с моделями приложения network """

    list_display = ('title', 'level', 'debt', 'supplier_link')
    list_filter = ('city',)
    fieldsets = [
        (None, {'fields': ['level', 'title', 'debt', 'supplier']}),
        ('Contacts', {'fields': ['email', 'country', 'city', 'street', 'home_number']}),
    ]

    def supplier_link(self, obj):
        """ Ссылка на поставщика """

        if obj.supplier:
            url = reverse(
                'admin:supplier_company_change',
                args=(obj.supplier.id, )
            )

            return mark_safe(u'<a href="{0}">{1}</a>'.format(url, obj.supplier))

    actions = ['DebtZero']

    @admin.action(description='Списать задолженность')
    def DebtZero(self, request, queryset):
        """ Обнуление задолженности """

        queryset.update(debt=0)

    inlines = [ProductsInline]


admin.site.register(Link, BaseLinkAdmin)
admin.site.register(Products)
