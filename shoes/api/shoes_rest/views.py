from .models import Shoe, BinVO
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import json
from common.json import ModelEncoder

# Create your views here.


class BinVODetailEncoder(ModelEncoder):
    model = BinVO
    properties = [
        "closet_name",
        "import_href",
    ]


class ShoesListDetailEncoder(ModelEncoder):
    model = Shoe
    properties = [
        "manufacturer",
        "model_name",
        "color",
        "picture_url",
        "bin",
        "id",
    ]
    encoders = {
        "bin": BinVODetailEncoder(),
    }


class ShoesListEncoder(ModelEncoder):
    model = Shoe
    properties = [
        "manufacturer",
        "model_name",
        "color",
        "picture_url",
        "bin",
        "id",
    ]
    encoders = {
        "bin": BinVODetailEncoder(),
    }

    def get_extra_data(self, o):
        return super().get_extra_data(o)


@require_http_methods(["GET", "POST"])
def shoes_list(request):
    if request.method == "GET":
        shoes = Shoe.objects.all()
        return JsonResponse({"shoes": shoes}, encoder=ShoesListEncoder)
    else:
        content = json.loads(request.body)
        try:
            bin = BinVO.objects.get(
                import_href=content["bin"]
            )
            content["bin"] = bin
        except BinVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid bin href"},
                status=400
            )

        shoes = Shoe.objects.create(
                **content
            )
        return JsonResponse(
            shoes,
            ShoesListDetailEncoder,
            safe=False,
        )


@require_http_methods(["DELETE", "PUT", "GET"])
def show_shoe(request, id):
    if request.method == "GET":
        shoe = Shoe.objects.get(id=id)
        context = {
            "shoes": shoe
        }
        return JsonResponse(
            context
        )
    elif request.method == "DELETE":
        count, _ = Shoe.objects.filter(id=id).delete()
        return JsonResponse({"deleted": count > 0})
    else:
        content = json.loads(request.body)

        try:
            if "bin" in content:
                bin = BinVO.objects.get(import_href=content["bin"])
                content["bin"] = bin
        except BinVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid bin href"},
                status=404,
            )

        Shoe.objects.filter(id=id).update(**content)
        shoe = Shoe.objects.get(id=id)
        return JsonResponse(
            shoe,
            encoder=ShoesListEncoder,
            safe=False,
        )
