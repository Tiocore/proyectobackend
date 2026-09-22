from datetime import datetime

from django.utils import timezone

from events.models import Event
from polls.models import Poll, Choice


events_data = [
    {
        "name": "Festival de Música Santiago",
        "description": "Festival con diferentes artistas y bandas nacionales.",
        "date": datetime(2026, 10, 10, 20, 0),
        "location": "Movistar Arena",
        "price": 25000,
        "capacity": 500,
    },
    {
        "name": "Campeonato de Fútbol",
        "description": "Encuentro deportivo con equipos invitados.",
        "date": datetime(2026, 10, 18, 16, 0),
        "location": "Estadio Nacional",
        "price": 15000,
        "capacity": 1000,
    },
    {
        "name": "Festival de Rock",
        "description": "Jornada dedicada a bandas de rock.",
        "date": datetime(2026, 10, 25, 19, 0),
        "location": "Teatro Caupolicán",
        "price": 30000,
        "capacity": 800,
    },
    {
        "name": "Feria Tecnológica",
        "description": "Exposición de tecnología, innovación y videojuegos.",
        "date": datetime(2026, 11, 5, 10, 0),
        "location": "Centro Cultural Estación Mapocho",
        "price": 10000,
        "capacity": 300,
    },
    {
        "name": "Concierto Nacional",
        "description": "Presentación de artistas nacionales.",
        "date": datetime(2026, 11, 14, 20, 0),
        "location": "Teatro Municipal",
        "price": 35000,
        "capacity": 700,
    },
    {
        "name": "Festival de Cine",
        "description": "Exhibición de películas y producciones independientes.",
        "date": datetime(2026, 11, 20, 18, 0),
        "location": "Centro Cultural La Moneda",
        "price": 12000,
        "capacity": 400,
    },
    {
        "name": "Evento de Gaming",
        "description": "Competencias y actividades relacionadas con videojuegos.",
        "date": datetime(2026, 11, 28, 11, 0),
        "location": "Espacio Riesco",
        "price": 20000,
        "capacity": 600,
    },
    {
        "name": "Stand Up Comedy",
        "description": "Presentación de comediantes nacionales.",
        "date": datetime(2026, 12, 5, 21, 0),
        "location": "Teatro Oriente",
        "price": 18000,
        "capacity": 250,
    },
]


for data in events_data:

    data["date"] = timezone.make_aware(data["date"])

    event, created = Event.objects.update_or_create(
        name=data["name"],
        defaults=data,
    )

    if created:
        print(f"Evento creado: {event.name}")
    else:
        print(f"Evento actualizado: {event.name}")

    poll, poll_created = Poll.objects.get_or_create(
        event=event,
        defaults={
            "question": "¿Qué te pareció este evento?"
        }
    )

    if poll_created:
        print(f"  Encuesta creada para: {event.name}")

    choices = [
        "Excelente",
        "Bueno",
        "Regular",
        "Malo",
    ]

    for choice_text in choices:
        Choice.objects.get_or_create(
            poll=poll,
            choice_text=choice_text,
        )

print("")
print("====================================")
print("DATOS DE PRUEBA CREADOS CORRECTAMENTE")
print("====================================")