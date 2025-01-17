from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import List
from django.shortcuts import redirect


def list(request):
  mytasks = List.objects.all().values()
  template = loader.get_template('test.html')
  delreq='delete-req-'
  context = {
  'mytasks': mytasks,
  }

  if request.method == 'POST':
          action = request.POST.get('action')
          
          if action == 'add': #ajout d'une task
              task = request.POST.get('task')
              desc = request.POST.get('desc', '')  
              List.objects.create(task=task, desc=desc)
          
          elif action.startswith('delete-req-'): #suppression d'une task
              task_id = int(request.POST.get('task_id'))
              List.objects.filter(id=task_id).delete()
          
          return redirect("http://127.0.0.1:8000/list/")  

  return HttpResponse(template.render(context, request))

