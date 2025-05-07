from django.shortcuts import render
from .forms import ContactForm
import os
from django.conf import settings
from .models import ContactMessage
from django.template.loader import render_to_string


def home(request):
    gallery_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'gallery')
    gallery_images = []
    if os.path.exists(gallery_path):
        for filename in os.listdir(gallery_path):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                gallery_images.append({
                    'url': f'images/gallery/{filename}',
                    'alt': os.path.splitext(filename)[0]
                })

    return render(request, 'main/index.html', {
        'gallery_images': gallery_images
    })
def about(request):
    return render(request, 'main/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            return render(request, 'main/contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})

