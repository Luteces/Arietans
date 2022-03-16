from polls.models import Question, Choice
from django.utils import timezone

Question.objects.all()

Question.objects.filter(id=1)

Question.objects.filter(question_text__startswith='What')

current_year = timezone.now().year
Question.objects.filter(pub_date__year=current_year)

Question.objects.get(pk=1)

q.Question.objects.get(pk=1)
q.was_published_recently()