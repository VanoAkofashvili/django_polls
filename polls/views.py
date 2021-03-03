from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.views import generic


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')
#     template = loader.get_template('polls/index.html')
#     context = {
#         'question_list': latest_question_list
#     }
#     return HttpResponse(template.render(context, request))

class IndexView(generic.ListView):
    template_name = 'polls/index.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("question does not exist")
#
#     return render(request, 'polls/detail.html', {
#         'question': question
#     })
#
#
# def results(request, question_id):
#     question = Question.objects.get(pk=question_id)
#     return render(request, 'polls/results.html', context={
#         'question': question
#     })


def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    try:
        choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    choice.votes += 1
    choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
