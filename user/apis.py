from .models import Address
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder


@login_required
def get_user_address(request, id):
    address = Address.objects.filter(user=request.user, id=id).values().first()
    
    if address:
        data = {
            'status': 'success',
            'address': address
        }
        return JsonResponse(data, encoder=DjangoJSONEncoder)
    else:
        data = {
            'status': 'failed',
            'address': None
        }
        return JsonResponse(data, encoder=DjangoJSONEncoder)