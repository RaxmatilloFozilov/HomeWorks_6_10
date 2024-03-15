from django.shortcuts import render
from .models import Topic

def ThemesView(request):
    return render(request, 'themes/list.html')

def mavzu_1(request):
    return render(request, 'themes/mavzu_1.html')

def mavzu_2(request):
    return render(request, 'themes/mavzu_2.html')

def mavzu_3(request):
    return render(request, 'themes/mavzu_3.html')


def topic_list(request):
    topics = Topic.objects.all()
    return render(request, 'themes/topic_list.html', {'topics': topics})

def topic_plans(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    return render(request, 'themes/topic_plans.html', {'topic': topic})
