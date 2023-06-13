from django.shortcuts import render

tasks = ['foo', 'bar']
# Create your views here.

def index(request):
    if request.method == 'POST':
        item = request.POST.get('task')
        tasks.append(item)

    return render(request, 'tasks/index.html', {
        "tasks": tasks
    })
