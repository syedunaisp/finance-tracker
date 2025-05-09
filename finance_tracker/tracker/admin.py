from django.contrib import admin
from .models import Category, Transaction

class TransactionInline(admin.TabularInline):
    model = Transaction
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [TransactionInline]
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'category', 'amount', 'type', 'date')
    def formatted_amount(self, obj):
            return f"₹{obj.amount}"
    formatted_amount.short_description = 'Amount'
    list_filter = ('type', 'category', 'date')
    search_fields = ('notes', 'user__username')
    ordering = ('-date',)
    date_hierarchy = 'date'
    fieldsets = (
        ('Transaction Info', {
            'fields': ('user', 'category', 'type', 'amount')
        }),
        ('Metadata', {
            'fields': ('date', 'notes'),
            'classes': ('collapse',),
        }),
    )



