from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

from home.models import Supply, ProductAttribute, Reservation
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from user.models import UserProfile
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse
import stripe
stripe.api_key = "sk_test_51IkV7mJS8r1hMN7QBqVvhz1RFieDcq8HfkYfS2S45agCFCjiNBC1N3mvKnGdJWZyxyw8UBlpWKuwiUMdvPmRuPfD00G8GiJgeu"


# Create your views here.
def signup_form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  # completed sign up
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # Create data in profile table for user
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = "images/users/user.png"
            data.save()
            messages.success(request, 'Your account has been created!')
            return HttpResponseRedirect('/login')
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect('/signup')

    form = SignUpForm()

    context = {
        'form': form,
    }
    return render(request, 'user/signup.html', context)


def login_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_user = request.user
            userprofile = UserProfile.objects.get(user_id=current_user.id)
            request.session['userimage'] = userprofile.image.url

            # Redirect to a success page.
            messages.success(request, 'Wellcome to our website, Please Update your profile')
            return HttpResponseRedirect('/user/profile')
        else:
            messages.warning(request, "Login Error !! Username or Password is incorrect")
            return HttpResponseRedirect('/login')

    return render(request, 'user/login_form.html')


def logout_func(request):
    logout(request)
    # if translation.LANGUAGE_SESSION_KEY in request.session:
    #     del request.session[translation.LANGUAGE_SESSION_KEY]
    #     del request.session['currency']
    return HttpResponseRedirect('/login')


@login_required(login_url='/login')  # Check login
def user_profile(request):
    current_user = request.user  # Access User Session information
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {

        'profile': profile}
    return render(request, 'user/user_profile.html', context)


@login_required(login_url='/login')  # Check login
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)  # request.user is user  data
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return HttpResponseRedirect('/user/update')
    else:

        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(
            instance=request.user.userprofile)  # "userprofile" model -> OneToOneField relatinon with user
        context = {

            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'user/user_update.html', context)


@login_required(login_url='/login')  # Check login
def user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect('/user/profile')
        else:
            messages.error(request, 'Please correct the error below.<br>' + str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:

        form = PasswordChangeForm(request.user)
        return render(request, 'user/user_password.html', {'form': form})

def stripePayment(request, pk):
    supply = Supply.objects.get(id=pk)
    productatr = ProductAttribute.objects.get(supply=supply)
    print(productatr.price)
    context = {
        'price': productatr.price,
        's_id':pk
    }
    return render(request, 'user/stripe_payment.html', context=context)

def charge(request, pk):
    if request.method == 'POST':
        print('Data:', request.POST)
        supply = Supply.objects.get(id=pk)
        reservation = Reservation.objects.get(supply=supply, user=request.user)
        reservation.paid = True
        reservation.save()
        amount = int(request.POST['amount'])

        customer = stripe.Customer.create(
                email=request.POST['email'],
                name=request.POST['nickname'],
                source=request.POST['stripeToken']
            )

        charge = stripe.Charge.create(
                customer=customer,
                amount=amount * 100,
                currency='usd',
                description="Donation"
            )

    return redirect(reverse('payment-success', args=[amount]))

def successPayment(request, args):
    amount = args
    context = {
        'amount': amount
    }
    return render(request, 'user/stripe_payment_success.html', context=context)
