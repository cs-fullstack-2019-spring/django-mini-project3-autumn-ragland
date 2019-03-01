from django.shortcuts import render, redirect, get_object_or_404
from .forms import TeacherForm
from .models import TeacherModel
from django.http import HttpResponse


# render html file with all teachers puller from model
def index(request):
    teachers = TeacherModel.objects.all()
    context = {
        'teachers': teachers
    }
    return render(request, 'miniApp/index.html', context)


# render hml file with model bound form
def add(request):
    form = TeacherForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'miniApp/add.html', context)


# render html file listing all entries made by a specific by item ID
def listTeacher(request, id):
    return render(request, 'miniApp/listTeacher.html')


# render html file listing all entries made at a specific school by item ID
def listSchool(request, id):
    return render(request, 'miniApp/listSchool.html')


# edit item with form
def edit(request, id):
    teacher_item = get_object_or_404(TeacherModel, pk=id)
    edit_form = TeacherForm(request.POST or None, instance=teacher_item)
    if edit_form.is_valid():
        edit_form.save()
        return redirect('index')
    context = {
        'form': edit_form
    }
    return render(request, 'miniApp/add.html', context)


# delete item with confirmation
def delete(request, id):
    teacher_item = get_object_or_404(TeacherModel, pk=id)
    if request.method == 'POST':
        teacher_item.delete()
        return redirect('index')
    context = {
        'teacher': teacher_item
    }
    return render(request, 'miniApp/delete.html', context)
