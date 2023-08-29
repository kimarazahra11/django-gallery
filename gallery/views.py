from django.shortcuts import render


def gallery_single(request):
    return render(request,'gallery/gallery-single.html')


def gallery(request):
    return render(request,'gallery/gallery.html')
