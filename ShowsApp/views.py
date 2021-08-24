from django.shortcuts import render, HttpResponse, redirect
from .models import Show, Network
from django.contrib import messages

def index(request):
    return redirect("/shows")


def shows(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request,'index.html', context)


def new(request):
    #create show form
    context = {
    }
    return render(request,'create.html', context)


def create(request):
    print(request.POST)

    errorsNetwork = Network.objects.validate(request.POST)
    errorsShow = Show.objects.validate(request.POST)
    errors = errorsNetwork
    errors.update(errorsShow)
    print(errors)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect(f"/shows/new")    
        
    else:
        try:
            network = Network.objects.get(network=request.POST['network'])
        except Network.DoesNotExist:
            network = Network.objects.create(network=request.POST['network'])

        show_obj = Show.objects.create(title = request.POST['title'], description = request.POST['description'], network = network, release = request.POST['release'])
        return redirect(f'/shows/{show_obj.id}')


def show_id(request, id):
    context = {
        'show': Show.objects.get(id=id)
    }
    return render(request,'description.html', context)


def show_edit(request, id):
    context = {
        'show': Show.objects.get(id=id)
    }
    return render(request, 'edit.html', context)


def show_update(request, id):
    print(request.POST)

    errorsNetwork = Network.objects.validate(request.POST)
    errorsShow = Show.objects.validate(request.POST)
    errors = errorsNetwork
    errors.update(errorsShow)
    print(errors)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect(f"/shows/{id}/edit")    
        
    else:
        try:
            network = Network.objects.get(network=request.POST['network'])
        except Network.DoesNotExist:
            network = Network.objects.create(network=request.POST['network'])

        show_to_update = Show.objects.get(id=id)
        show_to_update.title = request.POST['title']
        show_to_update.network = network
        show_to_update.release = request.POST['release']
        show_to_update.save()
        return redirect(f'/shows/{id}')


def show_destroy(request, id):
    show_to_delete = Show.objects.get(id=id)
    show_to_delete.delete()
    return redirect("/shows")
