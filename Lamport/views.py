import hashlib
import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from Lamport.models import UserPass


def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        username = data.get('username')
        user = UserPass.objects.get(username=username)
        if data.get('initlog'):
            response_data = {'success': True, 'n': user.n - 1}
            return JsonResponse(response_data, content_type='application/json')
        else:
            password = data.get('password')
            h_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            if h_password == user.password:
                user.n -= 1
                print(user.n)
                user.password = password
                user.save()
                response_data = {'success': True}
                return JsonResponse(response_data, content_type='application/json')

    return render(request, 'Login.html')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        hashed_password = request.POST['password']
        n = 10
        for _ in range(n):
            hashed_password = hashlib.sha256(hashed_password.encode('utf-8')).hexdigest()

        # Create a new UserPass instance and save it to the database
        user = UserPass(username=username, password=hashed_password, n=n)
        user.save()

        # Redirect to a success page or login page
        return redirect('home')
    return render(request, 'Signup.html')


def change_pass_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        hashed_password = request.POST['password']
        n = 10
        for _ in range(n):
            hashed_password = hashlib.sha256(hashed_password.encode('utf-8')).hexdigest()

        user = UserPass.objects.get(username=username)
        user.password = hashed_password
        user.n = n
        user.save()
        return redirect('login')
    return render(request, 'ChangePass.html')


def home_view(request):
    return render(request, 'Home.html')
