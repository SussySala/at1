from django.shortcuts import render
from .models import Question
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    questions = Question.objects.all()
    return render(request, 'eduprod/index.html', {'questions': questions})

def quiz_view(request):
    # Retrieve questions from the database
    questions = Question.objects.all()

    # Render the quiz template with the questions
    return render(request, 'quiz.html', {'questions': questions})
