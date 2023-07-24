from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from app.models import TaskList

# Create your views here.
def show(request):
    task_list = TaskList.objects.all()
    context = {'task_list':task_list}

    return render(request,template_name='show.html',context=context)

def complete(request,pk):
    complete_task = TaskList.objects.get(id=pk)
    complete_task.status = True
    complete_task.save()

    return redirect('app:show_page')

def edit(request,pk):
    old_data = get_object_or_404(TaskList, id=pk)

    if request.method == 'POST':
        new_data = request.POST
        old_data.title = new_data['title']
        old_data.body = new_data['body']
        old_data.deadline = new_data['deadline']
        old_data.save()
        return redirect('app:show_page')
    else:
        temp_dict = {
            'title':old_data.title,
            'body':old_data.body,
            'deadline':old_data.deadline,
        }
        
        return render(request,'edit.html',{'data':temp_dict})

def add(request):
    if request.method == 'POST':
        data = request.POST
        new = TaskList.objects.create(
            title = data['title'],
            body = data['body'],
            deadline = data['deadline']
        )
        new.save()
        return redirect('app:show_page')
    else:
        return render(request,'add.html')
    
def delete(request,pk):
    remove_item = TaskList.objects.get(id=pk).delete()
    return redirect('app:show_page')