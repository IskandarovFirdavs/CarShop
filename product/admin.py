from django.contrib import admin

from product.models import CarModel, CommentModel


class CommentInline(admin.TabularInline):
    model = CommentModel
    extra = 1


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_price', 'color']
    search_fields = ['name', ' color']
    list_filter = ['color', 'price']
    ordering = ['color', 'location']
    inlines = [CommentInline]
    readonly_fields = ['likes']


@admin.register(CommentModel)
class CommentModel(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']
