from django.contrib import admin
from gestionpedidos.models import Clientes
from gestionpedidos.models import Articulos
from gestionpedidos.models import pedidos

class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre", "telefono", "email", "direccion")
    search_fields=("nombre", "telefono")
    list_filter=("nombre",)
    #ponemos solo lo que queremos que se vea en el orden que queramos
    #esto se visualiza dentro de edmin
class ArticulosAdmin(admin.ModelAdmin):
    list_display=("nombre", "seccion", "precio")
    search_fields=("nombre", "precio")
    list_filter=("nombre",)
class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero", "fecha", "entregado")
    search_fields=("numero", "fecha")
    list_filter=("fecha",)
    date_hierarchy="fecha"
# Register your models here.

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(pedidos, PedidosAdmin)


