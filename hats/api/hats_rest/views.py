from itertools import count
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from common.json import ModelEncoder
from .models import LocationVO, Hat

# Create your views here.
class LocationVODetailEncoder(ModelEncoder):
    model = LocationVO
    properties = ["href", "closet_name", "section_number", "shelf_number"]

class HatListEncoder(ModelEncoder):
    model = Hat
    properties = ["fabric", "style", "color", "picture_url"]

class HatDetailEncoder(ModelEncoder):
    model = Hat
    properties = [
        "fabric",
        "style",
        "color",
        "picture_url",
        "location"
    ]
    encoders = {
        "location": LocationVODetailEncoder(),
    }

@require_http_methods(["GET", "POST"])
def api_list_hats(request):
    if request.method == "GET":
        hats = Hat.objects.all()
        return JsonResponse(
            {"hats": hats},
            encoder = HatListEncoder
        )
    else:
        content = json.loads(request.body)
        try:
            location_href = content['location']
            location = LocationVO.objects.get(href=location_href)
            content['location'] = location
        except LocationVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid location id"},
                status=400,
            )
        hats = Hat.objects.create(**content)
        return JsonResponse(
            {"hats": hats},
            encoder = HatListEncoder
        )

@require_http_methods(["DELETE", "GET"])
def api_show_hats(request, id):
    if request.method == "GET":
        hat = Hat.objects.get(id=id)
        return JsonResponse(
            hat,
            encoder=HatDetailEncoder,
            safe=False,
        )
    else:
        count, _ = Hat.objects.filter(id=id).delete()
        return JsonResponse( {
            "deleted": count > 0
        }
    )
