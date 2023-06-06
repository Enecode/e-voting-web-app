from django.urls import path
from . import views
from .views import polling_unit_result, store_results, lga_result_page

app_name = 'bincom_app'

urlpatterns = [
    path('', views.index, name="index"),
    path('polling_unit/<int:polling_unit_id>/', polling_unit_result, name='polling_unit_result'),
    path('lga_result/', lga_result_page, name='lga_result'),
    path('store_results/', store_results, name='store_results'),
]
