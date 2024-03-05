from django.shortcuts import render, redirect
from .models import User
from .forms import UserRegistrationForm

def home(request):
    return render(request, 'crud/home.html')


def user_list(request):
    users = User.objects.all()
    return render(request, 'crud/user_list.html', {'users': users})

def edit_user(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES, instance=user)
        if form:
            form.save()
            return redirect('user_list')
    else:
        form = UserRegistrationForm(instance=user)
        
    return render(request, 'crud/user_form.html', {'form': form})

def create_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Form submitted successfully")
            return redirect('user_list')
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    return render(request, 'crud/user_form.html', {'form': form})


def delete_user(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'crud/user_confirm_delete.html', {'user': user})
