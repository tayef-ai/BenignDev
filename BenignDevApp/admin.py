from django.contrib import admin
from .models import Service, PageView, Portfolio, Member, Contact, IctResource
# Register your models here.
@admin.register(Service)
class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'sname', 'slogo')

@admin.register(Portfolio)
class PortfolioModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'pname', 'pimage')

@admin.register(Member)
class MemberModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'mname', 'designation', 'email', 'phone', 'mimage')

@admin.register(PageView)
class PageviewModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'page_view', 'ip', 'date')

@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'cname', 'phone', 'email', 'message', 'date')

@admin.register(IctResource)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'rname', 'file')