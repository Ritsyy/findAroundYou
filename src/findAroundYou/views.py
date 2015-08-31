from django.shortcuts import render, render_to_response, RequestContext
from googleplaces import GooglePlaces, types, lang

API_KEY = 'AIzaSyAi4SKFgjnR9uODbJI3s5Op2pF3HBRJKCU'

google_places = GooglePlaces(API_KEY)

# Create your views here.
def search(request):
	return render_to_response("search.html", locals(), 
		context_instance=RequestContext(request))

def atm_map(request):
	atms_name = []
	atms_address = []
	atms = {}
	loc = ""

	if request.method == 'POST':
		loc = request.POST.get('location', '')
		autocomplete = google_places.autocomplete(input
			=loc)
		print autocomplete

	query_result = google_places.nearby_search(
		location=loc, keyword='atm',
		radius=200000)

	for place in query_result.places:
		place.get_details()
		atms[place.name] = [place.formatted_address, place.local_phone_number, place.international_phone_number, place.website]
	return render_to_response('atm_result.html', {'location':loc, 'atms':atms}, context_instance=RequestContext(request))