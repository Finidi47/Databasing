from django.contrib import admin

from sacco.models import Deposit, Customer

# Register your models here.
admin.site.register(Customer)
admin.site.register(Deposit)

#customise header
admin.site.site_header = 'Umoja Sacco Administration'

#title
admin.site.site_title = 'Sacco Admin'

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'gender', 'dob']
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['gender']
    list_per_page = 25












#python manage.py --help
#python mange.py createsuperuser
#admin@gmail.com
#123456