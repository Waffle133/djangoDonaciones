"""djangoDonaciones URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import requests
from django.contrib import admin
from django.urls import path

# from django.http import JsonResponse

from apps.products import views as products_views

# def challenge(request, todo_id, lorem):
#     response = requests.get(f'https://jsonplaceholder.typicode.com/todos/{todo_id}')
#     todos = response.json()
#     data = {
#         'status': 'ok',
#         'message': 'sucess',
#         'todos': todos
#     }
#     return JsonResponse(data, safe=False)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('challenge/<int:todo_id>/<str:lorem>', challenge, name='challenge')

    path('products/', products_views.show_products)

]
