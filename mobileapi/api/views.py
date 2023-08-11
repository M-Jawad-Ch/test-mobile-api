from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.request import Request

from .models import Unit, Worker, Visit
import json


@api_view(['GET'])
def get_units(req: Request, ph: str):
    try:
        worker = Worker.objects.get(phone_number=ph)
    except Worker.DoesNotExist:
        return Response(status=404)

    units: list[Unit] = Unit.objects.filter(worker=worker).all()
    return Response([{
        'pk': unit.pk,
        'name': unit.name
    } for unit in units])


@api_view(['POST'])
def make_visit(req: Request, ph: str):
    try:
        worker = Worker.objects.get(phone_number=ph)
    except Worker.DoesNotExist:
        return Response(status=404)

    data = json.loads(req.body.decode('utf-8'))

    pk = data.get('pk')
    coordinates = data.get('coordinates')
    latitude = coordinates.get('latitude') if coordinates else None
    longitude = coordinates.get('longitude') if coordinates else None

    if pk == None or coordinates == None or latitude == None or longitude == None:
        print(pk, coordinates, latitude, longitude)
        return Response(status=400)

    try:
        unit = Unit.objects.get(pk=pk)
    except Unit.DoesNotExist:
        return Response(status=404)

    if worker != unit.worker:
        return Response(status=400)

    visit = Visit.objects.create(
        unit=unit,
        latitude=float(latitude),
        longitude=float(longitude)
    )

    return Response({
        'pk': visit.pk,
        'date_time': visit.datetime
    })
