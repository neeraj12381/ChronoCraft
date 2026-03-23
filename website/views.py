from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Watch, Order, UserActivity, ContactMessage  # Saare models ek saath

# 1. Home Page (Order Logic)
def home(request):
    if request.method == "POST":
        p_name = request.POST.get('product_name')
        c_name = request.POST.get('customer_name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')

        Order.objects.create(
            product_name=p_name, 
            customer_name=c_name, 
            mobile=mobile, 
            email=email
        )
        messages.success(request, f"Order Confirmed Successfully for {p_name}!")
        return redirect('home')

    watches = Watch.objects.all()
    return render(request, 'home.html', {'watches': watches})

# 2. About Page
def about(request):
    return render(request, 'about.html')

# 3. Contact Page (FINAL VERSION - Isi ko use karna hai)
def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and message:
            ContactMessage.objects.create(
                name=name, 
                email=email, 
                subject=subject, 
                message=message
            )
            messages.success(request, "Success! Your message has been sent to our Lucknow Boutique.")
            return redirect('contact') # Wapas isi page par redirect
        else:
            messages.error(request, "Please fill all required fields.")
            
    return render(request, 'contact.html')

# 4. Signup
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# 5. Login
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            UserActivity.objects.create(user=user, action="Logged In")
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# 6. Logout
def logout_view(request):
    if request.user.is_authenticated:
        UserActivity.objects.create(user=request.user, action="Logged Out")
    logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect('home')

# 7. Others
def maintenance(request):
    return render(request, 'maintenance.html')

def privacy(request):
    return render(request, 'privacy.html')