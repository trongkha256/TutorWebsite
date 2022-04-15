from django.shortcuts import get_object_or_404, render

from .models import Category, Course


def course_all(request):
    courses = Course.courses.all()
    return render(request, 'store/index.html', {'courses': courses})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    courses = Course.objects.filter(category=category)
    return render(request, 'store/category.html', {'category': category, 'courses': courses})


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug, in_stock=True)
    return render(request, 'store/single.html', {'course': course})
