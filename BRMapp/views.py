from django.shortcuts import render
from BRMapp.forms import NewBookForm, SearchForm
from BRMapp.models import Applier
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


def view_apply(request):
    results = Applier.objects.filter(passed=0)
    res = render(request, 'BRMapp/temp.html', {'employee': results, 'title': 'Need to process',
                                               'editable': True, 'active': ['active', '']})
    return res


def view_history(request):
    results = Applier.objects.filter(passed__gt=0)
    res = render(request, 'BRMapp/temp.html', {'employee': results, 'title': 'History',
                                               'editable': False, 'active': ['', 'active']})
    return res


def view_passed(request):
    results = Applier.objects.filter(passed=1)
    res = render(request, 'BRMapp/temp.html', {'employee': results, 'title': 'History(passed)',
                                               'editable': False})
    return res


def view_rejected(request):
    results = Applier.objects.filter(passed=2)
    res = render(request, 'BRMapp/temp.html', {'employee': results, 'title': 'History(rejected)',
                                               'editable': False})
    return res


def pass_apply(request):
    Applier.objects.filter(pk=request.GET.get('id')).update(
        passed=1
    )
    return HttpResponseRedirect('/')


def reject_apply(request):
    Applier.objects.filter(pk=request.GET.get('id')).update(
        passed=2
    )
    return HttpResponseRedirect('/')
