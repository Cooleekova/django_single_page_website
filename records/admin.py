from django.contrib import admin

# Register your models here.

from records.models import Record


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'title', 'quantity', 'distance')



