from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from .models import Question, Choice, Comment, Post
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, PostForm
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
import json
#import simplejson
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'

def detail(request, question_id):
    question_name = get_object_or_404(Question, pk=question_id)
    # # for reverse order
    comment_list = Comment.objects.filter(question_id=question_id).order_by('-id')
    # # for reverse order
    # data = reversed(all_posts1)
    paginator  = Paginator(comment_list, 10)
    page = request.GET.get('page', 1)
    try:
        comments = paginator.page(page)
        #comments = page1_list
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        comments = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        comments = paginator.page(paginator.num_pages)
    
    tmpl_vars = {
        'all_posts': comments,
        'form': CommentForm(),
        'question': question_name,
    }
    return render(request, 'polls/detail.html', tmpl_vars, )


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

# @login_required
# def comment1(request, question_id):
#     print "***"*25
#     print "This is in comment view"
#     print "***"*25
#     p = get_object_or_404(Question, pk=question_id)
#     print "***"*25
#     print p
#     print "***"*25
#     if request.method == 'POST':
#         print "***"*25
#         print "inside post or ajax"
#         print "***"*25   
#         print request.user
#         print question_id        
#         print "****************"
#         form = CommentForm(request.POST)
#         if form.is_valid():            
#             print form
#             print "#"*20
#             comment_text = form.cleaned_data['comment']
#             comment_obj = Comment.objects.create(user=request.user,question_id=question_id,comment=comment_text)
#             comment = comment_obj.save()                      

#             print "$$$$"*20
#             content = Comment.objects.filter(question_id=question_id)
#             print type(content)
#             for i in content:
#                 comment = i.comment
#                 users =  i.user
#             print "########"*20  
#             names = request.POST.getlist('comment')
#             print type(names)
#             print names            
#             for name in names:           
#                 print "*******"*10
#                 print name
#                 print "*******"*10                         
            
#             # for all data
#             # print "**"*20
#             # c = Comment.objects.all()
#             # for line in c:
#             #     print line.comment
#             #     print line.user
#             # print "====="*20

#             #json_data = json.dumps(comment, ensure_ascii=False)        
            
#             return render(request, 'polls/detail.html', 
#                 {'question': p, 'data':content})
#             #return HttpResponse(json_data, content_type='application/json')
            
#             # json_data = json.dumps(comment, ensure_ascii=False)
#             # return HttpResponse(json_data, mimetype='application/json')
#             #return HttpResponse(json.dumps({'name': name}), content_type="application/json")
#         #return render_to_response(json.dumps('{{ polls:comment }}', {'comment':comment}, ),context_instance=RequestContext(request), content_type='application/json')

#     else:
#         form = CommentForm()  
#         return render_to_response('polls/detail.html',
#                           {'form': form},
#                           context_instance=RequestContext(request))
#         #return render_to_response('polls/detail.html', locals())
#         #return render_to_response(json.dumps('{{ post.id }}', {'comment':comment} ),context_instance=RequestContext(request), content_type='application/json')

@login_required
def comment(request, question_id):
    if request.method == 'POST':
        # for question
        p = get_object_or_404(Question, pk=question_id)
        form = CommentForm(request.POST)
        print "post comment"        
        post_comment = request.POST.get('the_post')
        print "*****"*20
        print post_comment
        print "*****"*20

        response_data = {}
        comment = Comment(user=request.user,question_id=question_id,comment=post_comment)
        comment_data = comment.save()

        response_data['comment'] = comment.comment            
        response_data['user'] = comment.user.username

        print "stored and response is"
        print "######"*20
        print response_data
        print "######"*20

        
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = RequestContext(request, {
#         'latest_question_list': latest_question_list,
#     })
#     return HttpResponse(template.render(context))

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)

# # def detail(request, question_id):
# #     try:
# #         question = Question.objects.get(pk=question_id)
# #     except Question.DoesNotExist:
# #         raise Http404("Question does not exist")
# #     return render(request, 'polls/detail.html', {'question': question})

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

# # def results(request, question_id):
# #     response = "You're looking at the results of question %s."
# #     return HttpResponse(response % question_id)

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


# from django.http import HttpResponseRedirect
# from django.shortcuts import render_to_response
# from .forms import UploadFileForm

# # Imaginary function to handle an uploaded file.
# from utils import handle_uploaded_file

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadFileForm()
#     return render_to_response('polls/upload.html', {'form': form})


# from django.http import HttpResponseRedirect
# from django.shortcuts import render
# from .forms import UploadFileForm
# from .forms import ModelFormWithFileField

# # def upload_file(request):
# #     if request.method == 'POST':
# #         form = ModelFormWithFileField(request.POST, request.FILES)
# #         if form.is_valid():
# #             # file is saved
# #             form.save()
# #             return HttpResponseRedirect('/success/url/')
# #     else:
# #         form = ModelFormWithFileField()
# #     return render(request, 'upload.html', {'form': form})

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             instance = ModelWithFileField(file_field=request.FILES['file'])
#             instance.save()
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadFileForm()
#     return render(request, 'polls/upload.html', {'form': form})