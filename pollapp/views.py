from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, Choice

# Get questions and display them

#home page / Welcome page

from pollapp.models import users
from pollapp.forms import userform


def register(request):
    form=userform()
    if request.method=="POST":
        form=userform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"login/login.html")
        else:
            HttpResponse("invalid data")
    return render(request,"registrationuser.html",{'form':form})





def login(request):
 if request.method=="POST":
    m=users.objects.get(name=request.POST['username'])
    print(m.password)
    if m.password==int(request.POST['passw']):
        request.session['users_name']=m.email



        return render(request,'pages/index.html',{'name':m.email})
    else:
        return HttpResponse("invalid")
 else:
    return render(request,'login/login.html')

def logout(request):
     try:
         del request.session['users_name']
     except KeyError:
         pass
     return render(request, 'login/login.html')
def main(request):
    return render(request, 'pages/index.html')

def main(request):
    return render(request, 'pages/index.html')



def homepage(request):
    return render(request, 'pages/index.html')

def userpage(request):
    return render(request, 'homepage.html')
def uspg(request):
    return render(request, 'homepage.html')
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# Show specific question and choices


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

# Get question and display results


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

# Vote for a question choice


def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def log(request):
    return render(request, 'login/login.html')
def home(request):
    return render(request, 'registration/login.html')

