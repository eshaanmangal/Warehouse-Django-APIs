from http.client import OK
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Category, Product, ProductTransaction
from .forms import CategoryForm, ProductForm, ProductTranscationForm


def healthcheck(request):
    return JsonResponse({'status': OK})


def get_all_products(request):
    return JsonResponse({'products': list(Product.objects.values())})


def get_all_categories(request):
    return JsonResponse({'categories': list(Category.objects.values())})


def get_product(request, product_id):
    product = Product.objects.get(id=product_id)
    data = {'id': product.id, 'category': product.category.name, 'name': product.name, 'measurement_units': product.measurement_units}
    return JsonResponse(data)


def get_category(request, category_id):
    category = Category.objects.get(id=category_id)
    data = {'id': category.id, 'name': category.name}
    return JsonResponse(data)


@csrf_exempt
def create_product(request):
    if request.method == "POST":
        post_data = dict(json.loads(request.body.decode("utf-8")))
        form = ProductForm(post_data or None)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': {'name': form.cleaned_data.get('name'), 'category': form.cleaned_data.get('category').name}})
        return JsonResponse({'error': "Don't know can be multiple errors"})
    else:
        return JsonResponse({'error': "Method not allowed, use POST instead"}, status=405)


@csrf_exempt
def create_category(request):
    if request.method == "POST":
        post_data = dict(json.loads(request.body.decode("utf-8")))
        form = CategoryForm(post_data or None)
        if form.is_valid():
            form.save()
            return JsonResponse({'response': form.cleaned_data})
        return JsonResponse({'error': "Category already exists"})
    else:
        return JsonResponse({'error': "Method not allowed, use POST instead"}, status=405)

@csrf_exempt
def make_product_transaction(request):
    if request.method == "POST":
        post_data = dict(json.loads(request.body.decode("utf-8")))
        form = ProductTranscationForm(post_data or None)
        if form.is_valid():
            form.save()
            return JsonResponse({'response': OK})
        return JsonResponse({'error': "There can be multiple errors"})
    else:
        return JsonResponse({'error': "Method not allowed, use POST instead"}, status=405)

def get_report(request):
    timestamp = request.GET.get('timestamp')
    data = list(ProductTransaction.objects.filter(direction="IN").filter(timestamp__lte=timestamp).values())
    print(data)
    # ProductTransaction is not JSON serializable. Why ? We have ProductTransaction type in list no ? but with .values() it works
    return JsonResponse({'response': data})