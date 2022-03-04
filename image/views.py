from django.shortcuts import render, redirect, reverse
from django.views import View
from .models import Image
from .forms import *
from .cnn import get_prediction


# Create your views here.

class ImageView(View):

    def get(self, request):

        image = Image.objects.last()
        pl, tl, s_img = get_prediction()
        return render(request, 'index.html', context={'image': image,
                                                      'predicted_label': pl,
                                                      'true_label': tl,
                                                      'sample_img': s_img})

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

