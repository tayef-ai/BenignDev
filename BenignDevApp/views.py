from django.shortcuts import render
from .models import Service, Portfolio, Member, PageView, IctResource
from datetime import date
from .forms import ContactForm
from django.http import HttpResponseRedirect
# Create your views here.
def homeview(request):
    count_view = PageView.objects.last()
    if count_view != None:
        pv = count_view.page_view + 1
    else:
        pv = 0
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip:
        ip = user_ip.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    regip = PageView(ip=ip, page_view=pv)
    regip.save()
    page_view = PageView.objects.last()
    today = date.today()
    page_view_today = PageView.objects.filter(date__year=today.year, date__month=today.month, date__day=today.day)[1:].count()
    service = Service.objects.all().order_by('id')[:3]
    portfolio = Portfolio.objects.all().order_by('-id')[:2]
    member = Member.objects.all().order_by('id')[:4]
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
            HttpResponseRedirect('/')
    else:
        form = ContactForm()
    context = {
        'services': service,
        'portfolios': portfolio,
        'members': member,
        'page_view': page_view,
        'page_view_today': page_view_today,
        'form': form,
    }
    return render(request, 'BenignDevApp/home.html', context)

def ictsubjectview(request):
    ictr = IctResource.objects.all()
    return render(request, 'BenignDevApp/ictresource.html', {'ictr': ictr})
