from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, HttpRequest, HttpResponse

from .models import Unit, Worker, Visit

import json


@require_http_methods(['GET'])
def get_units(req: HttpRequest, ph: str):
    try:
        worker = Worker.objects.get(phone_number=ph)
    except Worker.DoesNotExist:
        return HttpResponse(status=404)

    units: list[Unit] = Unit.objects.filter(worker=worker).all()
    return JsonResponse([{
        'pk': unit.pk,
        'name': unit.name
    } for unit in units], safe=False)


@require_http_methods(['POST'])
def make_visit(req: HttpRequest, ph: str):
    try:
        worker = Worker.objects.get(phone_number=ph)
    except Worker.DoesNotExist:
        return HttpResponse(status=404)

    data = json.loads(req.body.decode('utf-8'))

    pk = data.get('pk')
    coordinates = data.get('coordinates')
    latitude = coordinates.get('latitude') if coordinates else None
    longitude = coordinates.get('longitude') if coordinates else None

    if pk == None or coordinates == None or latitude == None or longitude == None:
        print(pk, coordinates, latitude, longitude)
        return HttpResponse(status=400)

    try:
        unit = Unit.objects.get(pk=pk)
    except Unit.DoesNotExist:
        return HttpResponse(status=404)

    if worker != unit.worker:
        return HttpResponse(status=400)

    visit = Visit.objects.create(
        unit=unit,
        latitude=float(latitude),
        longitude=float(longitude)
    )

    return JsonResponse({
        'pk': visit.pk,
        'date_time': visit.datetime
    }, safe=False)
