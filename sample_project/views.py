from django.shortcuts import render
from django.template.response import TemplateResponse
# from django.contrib.auth import logout
# from django.http import HttpResponseRedirect

# def my_render_callback(response):
#     # Do content-sensitive processing
#     do_post_processing()

# def my_view(request):
#     # Create a response
#     response = TemplateResponse(request, 'mytemplate.html', {})
#     # Register the callback
#     response.add_post_render_callback(my_render_callback)
#     # Return the response
#     return response

# def index(request):
#     response = TemplateResponse(request, 'base_index.html')
#     return response
def index(request):
    response = TemplateResponse(request, 'sample_project/home.html')
    return response

# def logout_page(request):
#     """
#     Log users out and re-direct them to the main page.
#     """
#     logout(request)
#     return HttpResponseRedirect('/')
