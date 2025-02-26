from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from todo.models import Todo

def start_page(request: HttpRequest):
    objects = Todo.objects.all()
    return render(request ,'index.html', {'todo' : objects})

def add(request: HttpRequest):
    if request.method == 'POST':
        title = request.POST.get('title')
        Todo.objects.create(title=title)
    else:
        return HttpResponse("<h1>Error! Method is not POST!</h1>")
    return redirect('main')
def completed(request: HttpRequest, id):
    # object = Todo.objects.get(id=id)
    # object = get_object_or_404(Todo, id=id)
    if Todo.objects.filter(id=id).exists():
        object = Todo.objects.get(id=id)
        Todo.objects.filter(id=id).update(is_completed=not object.is_completed)
    else:
        return render(request, "404.html")         
    return redirect('main')
def delete(request: HttpRequest, id):
    # object = Todo.objects.get(id=id)
    # object = get_object_or_404(Todo, id=id)
    if Todo.objects.filter(id=id).exists():
        object = Todo.objects.get(id=id)
        object.delete()
    else:
        return render(request, "404.html")
    return redirect('main')
def edit(request: HttpRequest, id):
    # object = Todo.objects.get(id=id)
    # object = get_object_or_404(Todo, id=id)
    if Todo.objects.filter(id=id).exists():
        object = Todo.objects.get(id=id)
        return render(request ,'edit.html', {'todo' : object})
    else:
        return render(request, "404.html")
def update_todo(request: HttpRequest, id):
    if request.method == 'POST':
        if Todo.objects.filter(id=id).exists():
            title = request.POST.get("title")
            Todo.objects.filter(id=id).update(title=title) 
        else:
            return render(request, "404.html")
    else:
        return HttpResponse("<h1>Error! Method is not POST!</h1>")
    return redirect('main')
