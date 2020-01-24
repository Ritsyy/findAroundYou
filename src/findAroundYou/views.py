from django.shortcuts import render
from googleplaces import GooglePlaces, types, lang
from keys_config import conf


API_KEY = conf['gmaps_key']
google_places = GooglePlaces(API_KEY)


def search(request):
	return render(request, "search.html", locals())


def atm_map(request):
	atms_name = []
	atms_address = []
	atms = {}
	loc = ""

	if request.method == 'POST':
		loc = request.POST.get('location', '')
		# autocomplete = google_places.autocomplete(input
		# 	=loc)
		# print autocomplete

	query_result = google_places.nearby_search(
		location='Jaipur', keyword='atm',
		radius=200)

	for place in query_result.places:
		place.get_details()
		atms[place.name] = [place.formatted_address, place.local_phone_number, place.international_phone_number, place.website]
	return render(request, 'atm_result.html', {'location':loc, 'atms':atms})
