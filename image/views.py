from django.shortcuts import render, redirect, reverse
from django.views import View
from .models import Image


# Create your views here.

class ImageView(View):

    def get(self, request):

        image = Image.objects.get(id=2)

        return render(request, 'index.html', context={'image':image})

    def post(self, request):

        return redirect(reverse('index'), kwargs={'message': 'Upload successful'})

