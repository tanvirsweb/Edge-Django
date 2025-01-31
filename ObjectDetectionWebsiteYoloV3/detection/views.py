from django.shortcuts import render
from .utils import objDetect
import os
from django.core.files.storage import FileSystemStorage
from django.conf import settings

# import os
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.shortcuts import render

def index(request):
    objects = []
    image_url = None

    if request.method == 'POST' and request.FILES.get('image'):
        try:
            file = request.FILES['image']
            extension = os.path.splitext(file.name)[1].lower()

            if extension not in ['.jpg', '.jpeg', '.png', '.gif']:
                return render(request, 'detection/index.html', {'error': 'File type not allowed.'})

            # Define upload directory
            upload_dir = os.path.join(settings.BASE_DIR, 'staticfiles', 'img')
            os.makedirs(upload_dir, exist_ok=True)  # Ensure the directory exists

            file_path = os.path.join(upload_dir, 'img.jpeg')

            # Remove existing file if it exists
            if os.path.exists(file_path):
                os.remove(file_path)

            # Save the new file
            FileSystemStorage(location=upload_dir).save('img.jpeg', file)

            # Run object detection
            objects, processed_image_path = objDetect(file_path)
            image_url = processed_image_path

        except Exception as e:
            return render(request, 'detection/index.html', {'error': str(e)})

    return render(request, 'detection/index.html', {'objects': objects, 'image_url': image_url})
