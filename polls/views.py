from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader
from django.shortcuts import render


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    template = loader.get_template('polls/index.html')
    context = {
        'question_list': latest_question_list
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("question does not exist")

    return render(request, 'polls/detail.html', {
        'question': question
    })


def vote(request, question_id):
    return HttpResponse('vote function in views.py')

