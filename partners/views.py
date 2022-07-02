from django.http import HttpResponse, JsonResponse

from .models import Partner


def healthcheck(request):
    return JsonResponse({"message": "Hello, Partners !!!"})


def fetch_all_partners(request):
    print("Hererererererererererre")
    # data = list(Partner.objects.values())
    # return JsonResponse(data)

    # data = Partner.objects.all()
    # jsonData = serializers.serialize('json', data)
    # return HttpResponse(jsonData, content_type='application/json')
    print("Datatattatatata: ", list(Partner.objects.values()))
    return JsonResponse({'response': list(Partner.objects.values())})


def fetch_partner(request, partner_id):
    partner = Partner.objects.get(id=partner_id)
    # [NOT WORKING] This is not JSON Serializable
    # return JsonResponse(category, safe=False)

    # [NOT WORKING] This doesn't work
    # return JsonResponse(dict(category))

    # [NOT WORKING] This object is not iterable
    # data = serializers.serialize('json', category)
    # return JsonResponse(data)

    # [WORKING] Manually fetching data which we need
    print("Datatatattatatatatat:", partner)
    data = {'id': partner.id, 'name': partner.name}
    return JsonResponse(data)


# @csrf_exempt
# def create_category(request):
#     if request.method == "POST":
#         post_data = dict(json.loads(request.body.decode("utf-8")))
#         form = CategoryForm(post_data or None)
#         if form.is_valid():
#             return JsonResponse({'status': post_data})
#         return JsonResponse({'error': "Category already exists"})
#     else:
#         return JsonResponse({'error': "Method not allowed, use POST instead"}, status=405)


