from django.shortcuts import render, redirect
from cods.CartoonImg import cartoonimg
from .models import cartoonImg
from .forms import ImageFileUploadForm
from django.http import JsonResponse, HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
image_dir = os.path.join(BASE_DIR, 'media')

# Create your views here.

def cartoon(request):
    return render(request, 'cartoon.html')

def home(request):
    new = cartoonImg.objects.all()
    return JsonResponse({"img":list(new.values())})


@staff_member_required(login_url='/admin/')
def delete_all_img(request):
    Img = []
    class Procurar_Img:
        def __init__(self):
            pass

        def func(self,Img):
            Img.clear()
            for file in os.listdir(image_dir+"\photo"):
                if file.endswith(".jpg"):
                    Img.append(file)
                elif file.endswith(".jpeg"):
                    Img.append(file)
                elif file.endswith(".png"):
                    Img.append(file)

    Procurar = Procurar_Img()
    Procurar.func(Img=Img)
    quantidade = len(Img)
    return render (request,'deleteallimg.html',{'quantidade':quantidade})


@staff_member_required(login_url='/admin/')
def delete_all_img_Submit(request):
    Img = []
    class Procurar_Img:
        def __init__(self):
            pass

        def func(self,Img):
            Img.clear()
            for file in os.listdir(image_dir+"\photo"):
                if file.endswith(".jpg"):
                    Img.append(file)
                elif file.endswith(".jpeg"):
                    Img.append(file)
                elif file.endswith(".png"):
                    Img.append(file)

    Procurar = Procurar_Img()
    Procurar.func(Img=Img)


    class delete_Img:
        def __init__(self):
            pass

        def delete(self,Img):
            local = image_dir + "\photo"
            for file in Img:
                os.remove(local+"\\"+file)


    Apagar_Tudo = delete_Img()
    Apagar_Tudo.delete(Img=Img)


    return redirect('delete_all_img')


def cartoon_submit(request):
    if request.method == 'POST':
        img = request.FILES.get('photo')
        img = cartoonImg.objects.create(photo=img)

        back = cartoonimg(img.photo.url)

        back1 = back[0] #edges
        back2 = back[1] #cartoon

        back1 = back1.replace('/media', '')
        back2 = back2.replace('/media', '')

        img = cartoonImg.objects.get(id=img.id)
        img.p_edge = back1
        img.p_cart = back2
        img.save()

        form = ImageFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return HttpResponse('Imagem Cartoonizada com sucesso!')
        else:
            return HttpResponse('erro ao Cartoonizada a imagem!')