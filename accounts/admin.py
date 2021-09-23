from django.contrib import admin
from accounts.models import register_table

admin.site.site_header="My Website"

admin.site.register(register_table)