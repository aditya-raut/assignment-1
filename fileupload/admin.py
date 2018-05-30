from django.contrib import admin

# Register your models here.
from fileupload.models import FileUpload

admin.site.register(FileUpload)