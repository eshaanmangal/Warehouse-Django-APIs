import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Partner
from .forms import PartnerForm

def healthcheck(request):
    return JsonResponse({"message": "Hello, Partners !!!"})


def fetch_all_partners(request):
    return JsonResponse({'response': list(Partner.objects.values())})


def fetch_partner(request, partner_id):
    partner = Partner.objects.get(id=partner_id)
    data = {'id': partner.id, 'name': partner.name, 'phone no.': partner.phone}
    return JsonResponse(data)


@csrf_exempt
def create_category(request):
    if request.method == "POST":
        post_data = dict(json.loads(request.body.decode("utf-8")))
        form = PartnerForm(post_data or None)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': post_data})
        return JsonResponse({'error': "Partner already exists"})
    else:
        return JsonResponse({'error': "Method not allowed, use POST instead"}, status=405)
