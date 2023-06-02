from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from common.json import ModelEncoder
from .models import LocationVO, Hat

# Create your views here.
class LocationVODetailEncoder(ModelEncoder):
    model = LocationVO
    properties = ["href", "closet_name"]

# class HatListEncoder(ModelEncoder):
#     model = Hat
#     properties = ["id", "fabric", "style", "color", "picture_url"]
#     encoders = {"location": LocationVODetailEncoder()}

class HatDetailEncoder(ModelEncoder):
    model = Hat
    properties = [
        "id",
        "fabric",
        "style",
        "color",
        "picture_url",
        "location",
    ]
    encoders = {
        "location": LocationVODetailEncoder(),
    }

@require_http_methods(["GET", "POST"])
def api_list_hats(request, location_vo_id=None):
    if request.method == "GET":
        if location_vo_id is not None:
            hats = Hat.objects.all()
        else:
            hats = Hat.objects.filter(location=location_vo_id)
        return JsonResponse(
            {"hats": hats},
            encoder = HatDetailEncoder,
        )
    else:
        content = json.loads(request.body)
        print(content)

        try:
            print("hello world")
            location_href = content["location"]
            location = LocationVO.objects.get(href=location_href)
            content["location"] = location
        except LocationVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid location id"},
                status=400,
            )
        hats = Hat.objects.create(**content)
        return JsonResponse(
            hats,
            encoder=HatDetailEncoder,
            safe=False,
        )

@require_http_methods(["DELETE", "GET"])
def api_show_hats(request, id):
    if request.method == "GET":
        try:
            hats = Hat.objects.get(id=id)
            return JsonResponse(
                hats,
                encoder=HatDetailEncoder,
                safe=False,
            )
        except Hat.Does.NotExist:
            response = JsonResponse({"message": "Does not exist"}, status = 404)
            return response
    elif request.method == "PUT":
        try:
            content = json.loads(request.body)
            Hat.objects.filter(id=id).update(**content)
            hat = Hat.objects.get(id=id)
            return JsonResponse(
                hat,
                encoder=HatDetailEncoder,
                safe=False,
            )
        except Hat.DoesNotExist:
            response = JsonResponse(
                {"message": "Does not Exist"},
                status=404,
                )
            return response
    else:
        count, _ = Hat.objects.filter(id=id).delete()
        return JsonResponse( {
            "deleted": count > 0
        }
    )
