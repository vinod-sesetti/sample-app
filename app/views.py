from django.shortcuts import render
#from .forms import AddressForm,DistanceForm
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
# Create your views here.
from django.template import RequestContext
#from .models import Distance
from django.db.models import Max
from .forms import UserForm,UploadFileForm
from models import User,UploadFile

from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response

def userform(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            fname = request.POST['first_name']
            lname = request.POST['last_name']
            mail = request.POST['email']
            storage = User(first_name = fname,last_name = lname,email = mail)
            storage.save()
            users = User.objects.all()
            image = UploadFile.objects.all()
            for im in image:
                print im
            
            for u in users:
                print u.first_name

            users = User.objects.all()
            for u in users:
                print u.email

            return HttpResponseRedirect('upload')
            #return HttpResponseRedirect('/image/upload')
    else:
        form = UserForm()

    image = UploadFile.objects.all()
    #image_path = image.file 
        
    data = {'form': form}
    return render_to_response('waypoints/page.html', data, context_instance=RequestContext(request))    
def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            users = User.objects.all()
            for u in users:
                print u.email
            new_file = UploadFile(file = request.FILES['file'],email = u.email,first_name = u.first_name)
            new_file.save()
            users = User.objects.all()
            for u in users:
                print u.email
            return HttpResponse("return this string")        
            
    else:
        form = UploadFileForm()

    images =  UploadFile.objects.all()
    img = []
    for im in images:
        img.append(im) 
        

    data = {'form': form ,'img':img}
    return render_to_response('waypoints/index.html', data, context_instance=RequestContext(request))

def images(request):
    
    images =  UploadFile.objects.all()
    img = []
    for im in images:
        img.append(im) 
    
    for im in img:
        print '******************'
        print im.file     
        print '******************'
    data = {'img':img}
    return render_to_response('waypoints/images.html', data, context_instance=RequestContext(request))
    