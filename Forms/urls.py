from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from myapp.views import contact_view
from myapp.views import contact_list_view,DSO_list_view,RSO_list_view,contact_delete,generate_oath_pdf,WIC_list_view
from myapp.views import contact_edit_view
from myapp.views import login_view
from myapp.views import upload_file
from myapp.views import get_retailer_number,contact_delete,update_BVS_Device
from myapp.views import get_bvs_number, get_Cluster,check_retailer_id,check_BVS_Device
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('delete_contact/<int:contact_id>/', contact_delete, name='delete_contact'),
    path('generate_oath_pdf/<int:contact_id>/', generate_oath_pdf, name='generate_oath_pdf'),

    path('admin/', admin.site.urls),
    path('contact/', contact_view, name='contact'),
    path('', RedirectView.as_view(url='/login/')),  # Redirect root to /contact/
    path('contact/list/', contact_list_view, name='contact_list'),  # List URL
    path('DSO/list/', DSO_list_view, name='DSO_List'),  # List URL
    path('RSO/list/', RSO_list_view, name='RSO_list'),  # List URL
    path('WIC/list/', WIC_list_view, name='WIC_list'),  # List URL
    path('contact/edit/<int:pk>/', contact_edit_view, name='contact_edit'),
    path('login/', login_view, name="login"),
    path('upload/', upload_file, name='upload_file'),
    path('get-retailer-number/', get_retailer_number, name='get_retailer_number'),
    path('get-bvs-number/', get_bvs_number, name='get_bvs_number'),
    path('get_Cluster/', get_Cluster, name='get_Cluster'),
    path('check-retailer-id/', check_retailer_id, name='check_retailer_id'),
    path('check-BVS-Device/', check_BVS_Device, name='check_BVS_Device'),
    path('update-BVS-Device/', update_BVS_Device, name='update_BVS_Device'),
    path('logout/', LogoutView.as_view(), name='logout'),  # Add this line

]
