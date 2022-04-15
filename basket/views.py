from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from store.models import Course

from .basket import Basket


def basket_summary(request):
    basket = Basket(request)
    return render(request, 'basket/summary.html', {'basket': basket})


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        course_id = int(request.POST.get('courseid'))
        course_qty = 1
        course = get_object_or_404(Course, id=course_id)
        basket.add(course=course, qty=course_qty)

        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        return response


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        course_id = int(request.POST.get('courseid'))
        basket.delete(course=course_id)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response


def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        course_id = int(request.POST.get('courseid'))
        course_qty = int(request.POST.get('courseqty'))
        basket.update(course=course_id, qty=course_qty)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response
