from django.contrib import admin
from .models import Person, Positions
from django.urls import reverse
from django.utils.html import format_html


@admin.register(Positions)
class PositionsAdmin(admin.ModelAdmin):
    list_display = ('positions',)


@admin.action(description='Удалить всю  информацию о выплаченной заработной плате')
def zero_salary_total(modeladmin, request, queryset):
    queryset.update(salary_total=0)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'department',
                    'manager_link', 'salary_per_period', 'salary_total')

    def manager_link(self, obj):
        if obj.manager_id:
            url = reverse("admin:Employee_app_person_change", args=[obj.manager_id])
            manager = obj.manager
        else:
            url = reverse("admin:Employee_app_person_change", args=[obj.id])
            manager = 'Босс'

        return format_html('<a href="{}">{}</a>', url, manager)

    manager_link.short_description = "Менеджер"

    list_filter = ('person_rating', 'department')

    actions = [zero_salary_total]
