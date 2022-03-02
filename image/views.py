from django.shortcuts import render, redirect, reverse
from django.views import View
from .models import Image
from .forms import *


# Create your views here.

class ImageView(View):

    def get(self, request):

        image = Image.objects.last()

        return render(request, 'index.html', context={'image': image})

    def post(self, request):

        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            last_image = Image.objects.last()
            # print(last_image.image.url)

            last_image.path = last_image.image.url
            last_image.save()

            return redirect('/image', kwargs={'message': 'Upload successful'})

        return redirect('/image', kwargs={'message': 'Upload failed'})

