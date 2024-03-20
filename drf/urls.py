 
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Create by Avazbek"
admin.site.index_title = "Women Admin"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('women.urls'))
]
