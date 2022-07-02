import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Category
from .forms import CategoryForm


def healthcheck(request):
    return JsonResponse({"message": "Hello, Products !!!"})


"""
    path('healthcheck/', healthcheck),
    path('categories/<int:category_id>', get_category),
    path('categories/', get_all_categories),
    path('category', create_category)
"""


def get_all_categories(request):
    # [WORKING BUT NOT DESIRED]
    # categories = Category.objects.all()
    # [NOTE] .values() was not serializable
    # data = serializers.serialize('json', categories)
    # return JsonResponse(data, safe=False)
    """
        [RESPONSE]
        "[{\"model\": \"products.category\", \"pk\": 1, \"fields\": {\"name\": \"Fruits\"}}, {\"model\": \"products.category\", \"pk\": 2, \"fields\": {\"name\": \"Drinks\"}}, {\"model\": \"products.category\", \"pk\": 3, \"fields\": {\"name\": \"Medicines\"}}, {\"model\": \"products.category\", \"pk\": 4, \"fields\": {\"name\": \"Beans\"}}]"
    """

    # [DESIRED]
    return JsonResponse({'response': list(Category.objects.values())})


def get_category(request, category_id):
    category = Category.objects.get(id=category_id)
    # [NOT WORKING] This is not JSON Serializable
    # return JsonResponse(category, safe=False)

    # [NOT WORKING] This doesn't work
    # return JsonResponse(dict(category))

    # [NOT WORKING] This object is not iterable
    # data = serializers.serialize('json', category)
    # return JsonResponse(data)

    # [WORKING] Manually fetching data which we need 
    data = {'id': category.id, 'name': category.name}
    return JsonResponse(data)


@csrf_exempt
def create_category(request):
    if request.method == "POST":
        post_data = dict(json.loads(request.body.decode("utf-8")))
        form = CategoryForm(post_data or None)
        if form.is_valid():
            return JsonResponse({'status': post_data})
        return JsonResponse({'error': "Category already exists"})
    else:
        return JsonResponse({'error': "Method not allowed, use POST instead"}, status=405)


