from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import Http404
from .models import Question, Choice
from django.contrib.auth.views import LoginView
from .forms import CandidateRegistrationForm
from django.contrib.auth import login
from django.contrib import messages

# Get questions and display those questions
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'voting/index.html', context)

# Show question and choices
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request, 'voting/detail.html', {'question': question})

# Get question and display results
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'voting/results.html', {'question': question})

# Vote for a question choice
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form with an error message
        return render(request, 'voting/detail.html', {
            'question': question,
            'error_message': 'You did not select a choice.'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Redirect to the results page after a successful vote
        return HttpResponseRedirect(reverse('voting:results', args=(question.id,)))

class CandidateLoginView(LoginView):
    template_name = 'candidate_login.html'

candidate_login = CandidateLoginView.as_view()


def register_candidate(request):
    if request.method == 'POST':
        form = CandidateRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('/')
    else:
        form = CandidateRegistrationForm()
    return render(request, 'candidate_register.html', {'form': form})