from django.shortcuts import render, redirect
from .forms import UsersForm  # GroupsForm
from .models import Users


# Create your views here.
def index(request):
    users = Users.objects.all()
    return render(request, 'show.html', {'users': users})


def addnew(request):
    if request.method == "POST":
        form = UsersForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = UsersForm()
    return render(request, 'index.html', {'form': form})


def edit(request, id):
    users = Users.objects.get(id=id)
    return render(request, 'edit.html', {'users': users})


def update(request, id):
    users = Users.objects.get(id=id)
    form = UsersForm(request.POST, instance=users)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'edit.html', {'users': users})


def destroy(request, id):
    users = Users.objects.get(id=id)
    users.delete()
    return redirect("/")

