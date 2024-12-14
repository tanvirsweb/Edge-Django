Instructions [by Tanvir Anjom Siddique](https://tanvirsweb.github.io/):

### Dowload Python & Install it:

```
py --version, python --version

pip --version

django-admin --version

pip install django
```

### Project Creation

```
django-admin startproject ProjectName

cd ProjectName
```

```
python manage.py runserver

ctrl+c
```

### App Creation

```
python manage.py startapp appName
```

- projectName/`projectName/urls.py` change [ add path of created app in ProjectName]

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('appName.urls')),
    path('admin/', admin.site.urls),
]
```

- projectName/`appName/urls.py` create

```py
from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/
    path('',views.home, name='home'),
    # http://127.0.0.1:8000/newpage/
    path('newpage',views.newpageh, name='newpageh'),
]
```

- projectName/`appName/views.py` - code write

```py
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'index.html')

def newpageh(request):
    return HttpResponse ("<h1> Hi </h1>")

```

### Cotact route creation - h1 tag response

- homepage route creation - html file send
- templete folder creation - home.html create
- url, views - render

#### Render `ProjectName/template/index.html` (all html files)

- Add below code `ProjectName/ProjectName/setting.py` file

```py
# on TOP of file write
import os
...
TEMPLATES = [
    ...
    'DIRS': [os.path.join(BASE_DIR,'templates')],
    ...
]
```

### Add Static folder for loading CSS, JS, Images

```
python manage.py collectstatic
```

- error occured
- fix this in ProjectName/ProjectName/`settings.py`
- check:

```py
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
```

- add code below (Correct code in settings.py)

```py
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'staticfiles')  # Your additional static files directory
]
```

- note:

```py
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'  # This should already be present
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # Optional for custom static files

```

- run in terminals: `python manage.py collectstatic` again
- ProjectName/`staticfiles/admin/ css/, img/, js/` will be created.

- or to access css,js,img etc files from `ProjectName/static/css,js,img` folders in setting.py at bottom of file write:

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
  ...
  <img
    src="{% static 'admin/img/calendar-icons.svg' %}"
    alt="Calendar Icon loading ..."
  />
</html>
```

### Entends

- ProjectName/templates/base/base.html

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{% block title %} Django base.html {% endblock %}</title>

    {% block linktag %} {% endblock %}
  </head>
  <body>
    {% block blockName %}
    <div>
      After entending this file if This Block is not modified content of
      blockName in extened file base.html will be shown.<br />
      If modified the file that extended current files that's content will be
      shown.
    </div>
    {% endblock %}
  </body>
</html>
```

- ProjectName/templates/

```py
{% extends "base/base.html" %}
{% comment %}
    {% extends "/base/base.html" %}   will generate error emit / at start of url
{% endcomment %}
{% load static %}

```
