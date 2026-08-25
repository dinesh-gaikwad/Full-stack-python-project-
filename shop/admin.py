from django.contrib import admin
from .models import Category,Product,UserProfile,Order,OrderItem,CartItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name','slug'); prepopulated_fields={'slug':('name',)}; search_fields=('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','category','price','stock','active','created_at')
    list_filter=('category','active'); search_fields=('name','description')
    prepopulated_fields={'slug':('name',)}

class OrderItemInline(admin.TabularInline):
    model=OrderItem; extra=0; readonly_fields=('product_name','price','quantity','subtotal')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('id','user','total','status','created_at')
    list_filter=('status','created_at'); search_fields=('full_name','email')
    inlines=[OrderItemInline]

admin.site.register(UserProfile)
admin.site.register(CartItem)
