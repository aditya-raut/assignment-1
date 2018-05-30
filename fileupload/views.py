from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.http import JsonResponse
from fileupload.models import FileUpload
from django.views.generic import View
from fileupload.forms import ImageForm

def upload_image(request):
	if request.method=='POST':
		files = request.FILES.getlist('myfiles')
		for i in files:
			file_obj = FileUpload.objects.create(name=i.name,attachment_file=i)
	return render(request,'file_upload.html',locals())

class ImageUploadView(View):
	def get(self, request):
		photos_list = FileUpload.objects.all()
		return render(self.request, 'index.html', {'photos': photos_list})

	def post(self, request):
		form = ImageForm(self.request.POST, self.request.FILES)
		if form.is_valid():
			photo = form.save()
			data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
		else:
			data = {'is_valid': False}
		return JsonResponse(data)