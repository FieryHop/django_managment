from django.shortcuts import render, redirect, get_object_or_404
from references.models import Status, Type, Category, SubCategory
from references.forms import StatusForm, TypeForm, CategoryForm, SubCategoryForm

def status_list(request):
    statuses = Status.objects.all()
    return render(request, 'references/status_list.html', {'statuses': statuses})

def status_create(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('references:status_list')
    else:
        form = StatusForm()
    return render(request, 'references/status_form.html', {'form': form})

def status_edit(request, pk):
    status = get_object_or_404(Status, pk=pk)
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return redirect('references:status_list')
    else:
        form = StatusForm(instance=status)
    return render(request, 'references/status_form.html', {'form': form})

def status_delete(request, pk):
    status = get_object_or_404(Status, pk=pk)
    status.delete()
    return redirect('references:status_list')

# Аналогичные функции для Type, Category, SubCategory
def type_list(request):
    types = Type.objects.all()
    return render(request, 'references/type_list.html', {'types': types})

def type_create(request):
    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('references:type_list')
    else:
        form = TypeForm()
    return render(request, 'references/type_form.html', {'form': form})

def type_edit(request, pk):
    type_obj = get_object_or_404(Type, pk=pk)
    if request.method == 'POST':
        form = TypeForm(request.POST, instance=type_obj)
        if form.is_valid():
            form.save()
            return redirect('references:type_list')
    else:
        form = TypeForm(instance=type_obj)
    return render(request, 'references/type_form.html', {'form': form})

def type_delete(request, pk):
    type_obj = get_object_or_404(Type, pk=pk)
    type_obj.delete()
    return redirect('references:type_list')

def category_list(request):
    categories = Category.objects.select_related('type').all()
    return render(request, 'references/category_list.html', {'categories': categories})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('references:category_list')
    else:
        form = CategoryForm()
    return render(request, 'references/category_form.html', {'form': form})

def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('references:category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'references/category_form.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('references:category_list')

def subcategory_list(request):
    subcategories = SubCategory.objects.select_related('category').all()
    return render(request, 'references/subcategory_list.html', {'subcategories': subcategories})

def subcategory_create(request):
    if request.method == 'POST':
        form = SubCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('references:subcategory_list')
    else:
        form = SubCategoryForm()
    return render(request, 'references/subcategory_form.html', {'form': form})

def subcategory_edit(request, pk):
    subcategory = get_object_or_404(SubCategory, pk=pk)
    if request.method == 'POST':
        form = SubCategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            form.save()
            return redirect('references:subcategory_list')
    else:
        form = SubCategoryForm(instance=subcategory)
    return render(request, 'references/subcategory_form.html', {'form': form})

def subcategory_delete(request, pk):
    subcategory = get_object_or_404(SubCategory, pk=pk)
    subcategory.delete()
    return redirect('references:subcategory_list')

def reference_home(request):
    return render(request, 'references/reference_home.html')

# Create your views here.
