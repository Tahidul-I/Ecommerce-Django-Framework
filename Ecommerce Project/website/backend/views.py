from django.shortcuts import render,redirect
from backend.models import User
from backend.models import practice_user
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.forms import PasswordChangeForm


# Create your views here.
def dashboard(request):
    return render(request,'backend/index.html')

def user_registration(request):

    if request.method =='POST' and request.FILES :
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conf_pass = request.POST.get('conf_pass')
        user_image = request.FILES['user_register_image']

        if password == conf_pass :
            pass_1 = make_password(password)
            user = User.objects.create(username = username, password = pass_1,email =email, user_image = user_image)
            user.save()
            return redirect('user_login')

    return render(request, 'backend/user_register.html')

def user_login(request):
    if request.method=='POST':
        u_name   = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=u_name,password=password)
        if user is not None:
            login(request,user)

        return redirect('dashboard')


    return render(request,'backend/login.html')

def user_logout(request):
    logout(request)
    return redirect('user_login')

def change_password(request):
    current_password = request.user.password
    # current_id = request.user.id
    form = PasswordChangeForm(request.POST)
    context={
        # 'current_password':current_password,
        'form' :form
    }
    if request.method =='POST':
        old_pass = request.POST.get('old_password')
        new_pass = request.POST.get('new_password1')
        new_conf_pass = request.POST.get('new_password2')
        get_data = User.objects.get(id = request.user.id)

        if get_data.check_password(old_pass) and new_pass == new_conf_pass :
            get_data.set_password(new_pass)
            get_data.save()
            update_session_auth_hash(request,get_data )
            return redirect('user_logout')
        else :
            return redirect('change_password')

    return render(request, 'backend/change_pass.html',context)


def practice_registration(request):

    if request.method =='POST' and request.FILES :
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conf_pass = request.POST.get('conf_pass')
        user_image = request.FILES['user_register_image']

        if password == conf_pass :
            user_save = practice_user(
                username = username,
                email = email,
                password = make_password(password),
                user_image = user_image


            )
            user_save.save()

            return redirect('user_login')

    return render(request,'backend/practice_user.html')
    


