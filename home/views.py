from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.http import JsonResponse, Http404, HttpResponseForbidden
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from datetime import datetime as dt

from .forms import SupplyDetailsForm, ComposeForm, MessageForm, ReservationForm, MyAdvertiseForm
from .models import Experience, Supply, Rating, CommentForm, ProductAttribute, Cartypes, Reservation, Message

from user.models import UserProfile
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from listvehicle.models import About,Agents
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from contact.models import Ownerquote
from django.db.models import Max,Min,Count
from django.template.loader import render_to_string
from django.db.models import  Q
from django.views import View
from django.views.generic.list import ListView
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def test(request):
    return render(request,'home/test.html')
@ login_required
def favourite_list(request):
    user = request.user
    favourite_post = user.favourite.all()
    context = {
        'favourite_post' : favourite_post
    }
    return render(request,
                  'home/favourites.html',context)
@ login_required(login_url='/login')
def favourite(request,id):
    supply = get_object_or_404(Supply,id=id)
    if supply.favourite.filter(id=request.user.id).exists():
        supply.favourite.remove(request.user)
    else:
        supply.favourite.add(request.user)
    return HttpResponseRedirect('/favourites')        
def index(request):
    if request.GET:
        adress= request.GET.get('adress', '')
        pickupDate = request.GET.get('pick_up', '')
        dropoffDate = request.GET.get('drop_off', '')
        exp = Experience.objects.all()
        supply=Supply.objects.all()
        if adress!='':
            supply=supply.filter(city=adress)

        if pickupDate!="" and dropoffDate!="":
            pickupDate=dt.strptime(pickupDate, "%m/%d/%Y").strftime("%Y-%m-%d")
            pickupDate=dt.strptime(pickupDate, "%Y-%m-%d")
            dropoffDate=dt.strptime(dropoffDate, "%m/%d/%Y").strftime("%Y-%m-%d")
            dropoffDate=dt.strptime(dropoffDate, "%Y-%m-%d")

            supply = supply.filter(~Q(reservation__start_date__range=(pickupDate, dropoffDate),reservation__end_date__range=(pickupDate, dropoffDate))).order_by('id')
            # another=Supply.objects.filter(reservation__start_date__range=(pickupDate, dropoffDate),reservation__end_date__range=(pickupDate, dropoffDate),reservation__confirm=True).order_by('id')
            # supply=supply.objects.filter()
        user = request.user
        # sup = Supply.objects.all()
        quote = Ownerquote.objects.filter()
        # is_favourite = False
        # if sup.favourite.filter(id=request.user.id).exists():
        #     is_favourite = True

        context = {
            'exp': exp,
            'supply': supply,
            # 'is_favourite':is_favourite,
            'quote': quote
        }

    else:
        exp = Experience.objects.all()
        supply = Supply.objects.all().order_by('id')[:3]
        user = request.user
        # sup = Supply.objects.all()
        quote = Ownerquote.objects.filter()
        # is_favourite = False
        # if sup.favourite.filter(id=request.user.id).exists():
        #     is_favourite = True

        context = {
            'exp': exp,
            'supply': supply,
            # 'is_favourite':is_favourite,
            'quote': quote
        }
    return render(request,'home/home.html',context)


def supply(request):
    supply = Supply.objects.all()
    # sup = Supply.objects.all().order_by('-id').distinct()
    min_price=ProductAttribute.objects.aggregate(Min('price'))
    max_price=ProductAttribute.objects.aggregate(Max('price'))
    # is_favourite = False
    # if sup.favourite.filter(id=request.user.id).exists():
    #     is_favourite = True
    context = {
        'supply' :supply,
        # 'is_favourite':is_favourite,
        'min_price':min_price,
		'max_price':max_price
    }    
    return render(request,'home/supply.html',context)

class ReservationView(View):
    template_name = "user/reservation.html"
    my_form = ReservationForm
    data = None
    total_unreserved = None
    msg = None
    page_obj = None
    page_number = 0
    def get(self, request):
        s = Reservation.objects.filter(supply__user=request.user)
        k = Reservation.objects.filter(user=request.user)
        # ss = Supply.objects.get(user=request.user)
        # print(ss)
        if s.count()>0:
            # print("ss", s)

            self.data = s
            self.total_unreserved = s.count()
            paginator = Paginator(self.data, 5)
            self.page_number = request.GET.get('page')
            self.page_obj = paginator.get_page(self.page_number)
            print(self.page_obj)
        elif k.count()> 0:
            self.data = k
            self.total_unreserved = k.count()
            paginator = Paginator(self.data, 5)
            self.page_number = request.GET.get('page')
            self.page_obj = paginator.get_page(self.page_number)
            print(self.page_obj)
        else:
            self.msg = "No data found"
        context = {
            'page_obj': self.page_obj,
            's': s,
            'k': k,
            'form': self.my_form,
            'total': self.total_unreserved,
            'msg': self.msg
        }
        return render(request, template_name=self.template_name, context=context)

class MyAdvertiseView(View):
    template_name = "user/my_advertise.html"
    form = MyAdvertiseForm
    page_obj = None
    def get(self, request):
        data = Supply.objects.all()
        paginator = Paginator(data, 5)
        self.page_number = request.GET.get('page')
        self.page_obj = paginator.get_page(self.page_number)
        print(self.page_obj)
        context = {
            'page_obj': self.page_obj,
            'form': self.form
        }
        return render(request, template_name=self.template_name, context=context)

class DeleteAdvertiseView(View):
    template_name = "user/delete_advertise.html"
    def get(self, request, pk):
        data = Supply.objects.get(id=pk)
        if request.method == "POST":
            data.delete()
            return redirect('my-advertise')
        context = {
            'item': data
        }
        return render(request, template_name=self.template_name, context=context)
    def post(self, request, pk):
        data = Supply.objects.get(id=pk)
        data.delete()
        return redirect('my-advertise')

class AddAdvertiseView(View):
    template_name = "user/add_advertise.html"
    form = MyAdvertiseForm
    def get(self, request):
        context = {
            'form': self.form
        }
        return render(request, template_name=self.template_name, context=context)

    def post(self, request):
        self.form = MyAdvertiseForm(request.POST, request.FILES)
        supply = Supply.objects.latest('id')
        print(supply)
        if self.form.is_valid():
            user = request.user
            cartypes = self.form.cleaned_data['cartypes']
            title = self.form.cleaned_data['title']
            slug = self.form.cleaned_data['slug']
            cart_title = self.form.cleaned_data['car_title']
            city = self.form.cleaned_data['city']
            price = self.form.cleaned_data['price']
            status = self.form.cleaned_data['status']
            main_photo = self.form.cleaned_data['main_photo']
            image1 = self.form.cleaned_data['image1']
            image2 = self.form.cleaned_data['image2']
            image3 = self.form.cleaned_data['image3']
            seats = self.form.cleaned_data['seats']
            bearth = self.form.cleaned_data['bearth']
            feature = self.form.cleaned_data['features']
            description = self.form.cleaned_data['description']
            facilities = self.form.cleaned_data['description']
            houserules = self.form.cleaned_data['houserules']
            min_reserve_period = self.form.cleaned_data['min_reserver_period']
            pick_up_from = self.form.cleaned_data['pick_up_from']
            drop_of_before = self.form.cleaned_data['drop_of_before']
            favourite = self.form.cleaned_data['favourite']
            is_published = self.form.cleaned_data['is_published']
            # ct = Cartypes.objects.filter(title=cartypes)
            # ur = User.objects.filter(username=favourite)
            supply = Supply.objects.create(user=user, title=title, slug=slug, car_title=cart_title, city=city, price=price, status=status, main_photo=main_photo, image1=image1, image2=image2, image3=image3, seats=seats, bearth=bearth, features=feature, description=description, failities=facilities, houserules=houserules, min_reserver_period=min_reserve_period, pick_up_from=pick_up_from, drop_of_before=drop_of_before, is_published=is_published)
            for u in cartypes:
                supply.cartypes.add(u)
            for u in favourite:
                supply.favourite.add(u)
            ProductAttribute.objects.create(supply=supply, price=self.form.cleaned_data['price'])

        return redirect('my-advertise')

class UpdateReservationView(View):
    template_name = "user/update_reservation.html"
    form = ReservationForm
    def get(self, request, pk):
        reservation = Reservation.objects.get(id=pk)
        self.form = ReservationForm(instance=reservation)
        context = {
            "form": self.form
        }
        return render(request, template_name=self.template_name, context=context)

    def post(self, request, pk):
        reservation = Reservation.objects.get(id=pk)
        self.form = ReservationForm(instance=reservation)
        if request.method == 'POST':
            self.form = ReservationForm(request.POST, instance=reservation)
            if self.form.is_valid():
                self.form.save()
                return redirect('user_reservation')

class UpdateAdvertiseView(View):
    template_name = "user/update_advertise.html"
    form = MyAdvertiseForm
    def get(self, request, pk):
        supply = Supply.objects.get(id=pk)
        self.form = MyAdvertiseForm(instance=supply)
        context = {
            "form": self.form
        }
        return render(request, template_name=self.template_name, context=context)

    def post(self, request, pk):
        supply = Supply.objects.get(id=pk)
        self.form = MyAdvertiseForm(instance=supply)
        if request.method == 'POST':
            self.form = MyAdvertiseForm(request.POST, instance=supply)
            if self.form.is_valid():
                self.form.save()
                return redirect('my-advertise')

class SupplyDetails(View):
    template_name = "home/supply_details.html"
    my_form = SupplyDetailsForm
    message_form = MessageForm
    msg = None


    def get(self, request, slug, id):
        supply = Supply.objects.get(pk=id,slug=slug)
        comments = Rating.objects.filter(supply_id=id,status='True')
        supply_list = Supply.objects.all().order_by('id')[:3]
        is_favourite = False
        if supply.favourite.filter(id=request.user.id).exists():
            is_favourite = True
        if request.GET and request.user.is_authenticated:
            user_name = request.user
            supply_name = supply
            start_date = request.GET['start_date']
            end_date = request.GET['end_date']
            location = request.GET['location']
            traveller = request.GET['traveller']
            phone = request.GET['phone']
            reservation = Reservation.objects.create(user=user_name, supply=supply_name, end_date=end_date, start_date=start_date, location=location, traveller=traveller, phone=phone)
            self.msg = "Reservation submitted"

            message = "We have received your reservation in location: " + location + ". Please wait for supplier confirmation: " + str(supply)

            send_mail('Tombotrip reservation form submitted',
                      message,
                      settings.EMAIL_HOST_USER,
                      ['tanzil.ovi578@gmail.com'],
                      fail_silently=False)

        else:
            self.msg = "Please Login for reservation"
        context ={
            'message': self.msg,
            'supply':supply,
            'comments':comments,
            'is_favourite':is_favourite,
            'supply_list':supply_list,
            'form': self.my_form,
            'form_msg':self.message_form,
            # 'price':ProductAttribute.objects.get(supply=supply).price
        }
        return render(request, template_name=self.template_name, context=context)

    def post(self, request, slug, id):
        supply = Supply.objects.get(pk=id, slug=slug)
        comments = Rating.objects.filter(supply_id=id, status='True')
        supply_list = Supply.objects.all().order_by('id')[:3]
        is_favourite = False
        if supply.favourite.filter(id=request.user.id).exists():
            is_favourite = True
        if request.POST and request.user.is_authenticated:
            toUser = supply.user
            fromUser = request.user
            messages = request.POST['message']
            sendMessage = Message.objects.create(toUser=toUser, fromUser=fromUser,  message=messages)
            self.msg = "Message submitted"
        else:
            toUser = supply.user
            email = request.POST['email']
            messages = request.POST['message']
            sendMessage = Message.objects.create(toUser=toUser, message=messages, email=email)
            self.msg = "Message submitted"
        context = {
            'message': self.msg,
            'supply': supply,
            'comments': comments,
            'is_favourite': is_favourite,
            'supply_list': supply_list,
            'form': self.my_form,
            'form_msg': self.message_form
        }
        return render(request, template_name=self.template_name, context=context)

# class ThreadView(LoginRequiredMixin, FormMixin, DetailView):
#     template_name = 'chat/thread.html'
#     form_class = ComposeForm
#     success_url = './'
#
#     def get_queryset(self):
#         return Thread.objects.by_user(self.request.user)
#
#     def get_object(self):
#         other_username  = self.kwargs.get("username")
#         obj, created    = Thread.objects.get_or_new(self.request.user, other_username)
#         if obj == None:
#             raise Http404
#         return obj
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = self.get_form()
#         return context
#
#     def post(self, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return HttpResponseForbidden()
#         self.object = self.get_object()
#         form = self.get_form()
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)
#
#     def form_valid(self, form):
#         thread = self.get_object()
#         user = self.request.user
#         message = form.cleaned_data.get("message")
#         ChatMessage.objects.create(user=user, thread=thread, message=message)
#         return super().form_valid(form)

# def supply_details(request,slug,id):
#     supply = Supply.objects.get(pk=id,slug=slug)
#     comments = Rating.objects.filter(supply_id=id,status='True')
#     supply_list = Supply.objects.all().order_by('id')[:3]
#     is_favourite = False
#     if supply.favourite.filter(id=request.user.id).exists():
#         is_favourite = True
#     context ={
#         'supply':supply,
#         'comments':comments,
#         'is_favourite':is_favourite,
#         'supply_list':supply_list
#     }
#     return render(request,'home/supply_details.html',context)
def exp_details(request,slug):
    exp = get_object_or_404(Experience,slug=slug) 
    about = About.objects.get()
    agents = Agents.objects.all()  
    context = {
        'exp':exp,
        'about':about,
        'agents':agents,
    }
    return render(request,'home/details.html',context)      
def addcomment(request,id):
   url = request.META.get('HTTP_REFERER')  # get last url
   #return HttpResponse(url)
   if request.method == 'POST':  # check post
      form = CommentForm(request.POST)
      if form.is_valid():
         data = Rating()  # create relation with model
         data.subject = form.cleaned_data['subject']
         data.comment = form.cleaned_data['comment']
         data.rate = form.cleaned_data['rate']
         data.ip = request.META.get('REMOTE_ADDR')
         data.supply_id=id
         current_user= request.user
         data.user_id=current_user.id
         data.save()  # save data to table
         messages.success(request, "Your review has ben sent. Thank you for your interest.")
         return HttpResponseRedirect(url)

   return HttpResponseRedirect(url)  
def supplysearch(request):
    queryset = Supply.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(car_title__icontains=query) |
            Q(city__icontains=query) |
            Q(description__icontains=query)

        ).distinct()
    context = {
        'supply': queryset,
        'query':query
    }
    return render(request, 'home/search_results.html', context)    
   
def filter_data(request):
	
	# cartypes=request.GET.getlist('cartypes[]')
	catagories=request.GET.getlist('catagory[]')
	transmissions=request.GET.getlist('transmission[]')
	minPrice=request.GET['minPrice']
	maxPrice=request.GET['maxPrice']
	cartypes=request.GET.getlist('cartype[]') 
	allProducts=Supply.objects.all().order_by('-id').distinct()
	allProducts=allProducts.filter(productattribute__price__gte=minPrice)
	allProducts=allProducts.filter(productattribute__price__lte=maxPrice)
	
	if len(cartypes)>0:
		allProducts=allProducts.filter(cartypes__id__in=cartypes).distinct()
	if len(catagories)>0:
		allProducts=allProducts.filter(productattribute__category__id__in=catagories).distinct()
	if len(transmissions)>0:
		allProducts=allProducts.filter(productattribute__transmission__id__in=transmissions).distinct()
	t=render_to_string('ajax/supply.html',{'data':allProducts})
	return JsonResponse({'data':t})


class MessageListView(ListView):
    # specify the model for list view
    model = Message

    def get_queryset(self, *args, **kwargs):
        qs = super(MessageListView, self).get_queryset(*args, **kwargs)
        qs = qs.filter(toUser=self.request.user)
        return qs

    def get_context_data(self, **kwargs):
        context = super(MessageListView, self).get_context_data(**kwargs)
        context['form'] = MessageForm()
        return context

def message_create(request,username):
    if request.method == 'POST' and request.user.is_authenticated:
        # create a form instance and populate it with data from the request:
        toUser = User.objects.get(username=username)
        fromUser = request.user
        messages = request.POST['message']
        sendMessage = Message.objects.create(toUser=toUser, fromUser=fromUser, message=messages)
        # context={}
        message='Message send '
        return render(request,"home/message_list.html",{'message':message})

class MessageDetailView(DetailView):
    # specify the model to use
    model = Message