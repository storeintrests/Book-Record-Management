from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def indexView(request):
    return render(request, 'accounts/index.html')

def dashboardView(request):
    return render(request, 'accounts/dashboard.html')


def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/registration/register.html', {'form':form})
