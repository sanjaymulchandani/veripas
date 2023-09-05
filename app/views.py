from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, UserDetailSerializer
from .forms import RegistrationForm, LoginForm, UserDetailsForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import UserDetails, HomeContent, WebsiteLogo
from django.contrib import messages

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailListCreateView(generics.ListCreateAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class UserDetailsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter the queryset based on the current user's ID
        return UserDetails.objects.filter(user=self.request.user)


def home_view(request):
    home_content = HomeContent.objects.all()
    return render(request, 'index.html', {'home_content': home_content})

def nav_bar(request):
    navbar_content = WebsiteLogo.objects.all()
    return render(request, 'navbar.html', {'navbar_content': navbar_content})

@user_passes_test(lambda user: not user.username, login_url='home', redirect_field_name=None)
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('user-details-create')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form':form})

@user_passes_test(lambda user: not user.username, login_url='home', redirect_field_name=None)
def user_login(request):
    if request.method == "POST":
        form = LoginForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('user-details')
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})

@login_required
def logout_custom(request):
    logout(request)
    return redirect('home')

@login_required
def user_details_list(request):
    user_details = UserDetails.objects.all()
    return render(request, 'user_details.html', {'user_details': user_details})

@login_required
def create_user_details(request):
    if request.method == 'POST':
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            # Create a new UserDetails object and save it
            user_details = form.save(commit=False)
            user_details.user = request.user  # Assign the current user
            user_details.save()
            return redirect('user-details')  # Redirect to the home page or another view
    else:
        form = UserDetailsForm()
    
    return render(request, 'userdetails_create.html', {'form': form})

@login_required

def update_user_details(request, pk):
    user_details = get_object_or_404(UserDetails, pk=pk)
    
    if request.method == 'POST':
        form = UserDetailsForm(request.POST, instance=user_details)
        if form.is_valid():
            form.save()
            return redirect('user-details')  # Redirect to the user details list
    else:
        form = UserDetailsForm(instance=user_details)
    
    return render(request, 'userdetails_update.html', {'form': form, 'userDetails': user_details})

@login_required
def delete_user_details(request, pk):
    user_details = get_object_or_404(UserDetails, pk=pk)
    
    if request.method == 'POST':
        user_details.delete()
        return redirect('user-details')  # Redirect to the user details list
    
    return render(request, 'userdetails_delete.html', {'userDetails': user_details})

