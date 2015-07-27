from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from demoapp.models import Note
from demoapp.forms import CreateNotesForm

from django.utils.safestring import mark_safe

from django.contrib import messages
from django.template.response import TemplateResponse
# Create your views here.

def index(request):
    #return HttpResponse('demoapp/home.html')
    return TemplateResponse(request, 'demoapp/home.html')

def index1(request):
    latest_notes_list = Note.objects.all().order_by('-timestamp')
    paginator = Paginator(latest_notes_list, 5) # Show 5 notes per page
    page = request.GET.get('page')
    try:
        notes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        notes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        notes = paginator.page(paginator.num_pages)
    template = loader.get_template('demoapp/index.html')
    context = RequestContext(request, {'latest_notes_list': notes, })
    return HttpResponse(template.render(context))


def create_note(request):
    if request.method == "GET":
        form = CreateNotesForm()
    else:
        form = CreateNotesForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            note = Note.objects.create(title=title,body=body)
            note.save()
            messages.success(request, 'Notes saved sucessfully')
            return redirect('/')
        return  render(request,'demoapp/create_note.html',{'form': form},context_instance=RequestContext(request))
    form = CreateNotesForm()
    return  render(request,'demoapp/create_note.html',{'form': form},context_instance=RequestContext(request))


