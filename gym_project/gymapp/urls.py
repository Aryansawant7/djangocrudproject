from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home),
    path('add',views.add),
    path('view',views.view),
    path('save',views.save),
    path('delete/<rid>',views.deletecustomer),
    path('update/<rid>',views.updatecustomer),

]
