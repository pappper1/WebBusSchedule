from django.shortcuts import render, redirect
from .models import Routes
from .forms import RouteForm
from .bus_parser import Parser


parser = Parser()

def index(request):
    if request.method == 'POST':
        selected_option = request.POST.get('selectedOption')
        if selected_option == "Выберите маршрут":
            pass
        else:
            return redirect('route', route_number=selected_option)
    routes = parser.route_list()
    return render(request, 'index.html', {'routes': routes})


def route(request, route_number):
    if request.method == 'POST':
        selected_option = request.POST.get('selectedOption1')
        if selected_option == "Выберите направление":
            pass
        else:
            return redirect('route_stops', route_number=route_number, direction=int(selected_option))

    directions = enumerate(parser.route_info(route_number))
    return render(request, 'bus_routes.html', {'route_number': route_number, 'directions': directions})


def route_stops(request, route_number, direction: int):
    if request.method == 'POST':
        selected_option = request.POST.get('selectedOption1')
        if selected_option == "Выберите остановку":
            pass
        else:
            return redirect('schedule', route_number=route_number, direction=int(direction), stop_id=int(selected_option))

    directions, names_stops_a, names_stops_b, id_stopsA, id_stopsB = parser.stops(route_number)
    stops_a = zip(id_stopsA, names_stops_a)
    stops_b = zip(id_stopsB, names_stops_b)
    return render(request, 'bus_stops.html', {'route_number': route_number,
                                                                   'direction': directions[int(direction)],
                                                                   'stops': stops_a if int(direction) == 0 else stops_b})

def schedule(request, route_number, direction, stop_id):
    hours_minutes = parser.schedule_for_stop(str(route_number), str(stop_id), str(direction))
    return render(request, 'schedule.html', {'route_number': route_number,
                                                                  'hours_minutes': hours_minutes})