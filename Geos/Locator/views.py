from django.shortcuts import render, redirect
from django.http import HttpResponse
from folium import Map, PolyLine

from .models import Search
from .forms import SearchForm
import folium
import geocoder

# Create your views here.


def index(request):
    # if request.method == 'POST':
    #     form = SearchForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/')
    # else:
    #     form = SearchForm()
    # address = Search.objects.all().last()
    # location = geocoder.osm(address)
    # lat = location.lat
    # lng = location.lng
    # country = location.country
    # if lat == None or lng == None:
    #     address.delete()
    #     return HttpResponse('You address input is invalid')
    #
    # # Create Map Object
    # m = folium.Map(location=[19, -12], zoom_start=2)
    #
    # folium.Marker([lat, lng], tooltip='Click for more',
    #               popup=country).add_to(m)
    # # Get HTML Representation of Map Object
    # m = m._repr_html_()
    # context = {
    #     'm': m,
    #     'form': form,
    # }
    # return render(request, 'index.html', context)
    source_address = request.POST.get('source', '')
    destination_address = request.POST.get('destination', '')

    # Use a geocoding service to convert source and destination addresses to coordinates.
    source_coordinates = (0, 0)  # Replace with actual coordinates
    destination_coordinates = (0, 0)  # Replace with actual coordinates

    m = Map(location=source_coordinates, zoom_start=5)
    PolyLine([source_coordinates, destination_coordinates], color="blue").add_to(m)

    return render(request, 'map.html', {
        'source_address': source_address,
        'destination_address': destination_address,
        'map': m.index.html(),
    })