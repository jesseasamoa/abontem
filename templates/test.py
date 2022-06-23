import json
import urllib

from farm.models import Forecast, DashboardLand, DashboardCrop
from django.views.generic import ListView
import requests
import json


class DashboardHome(ListView):
    template_name = 'dashboard.html'
    queryset = DashboardCrop.objects.all()
    city = requests.POST['city']
    ''' api key might be expired use your own api_key
        place api_key in place of appid ="your_api_key_here "  '''

    # source contain JSON data from API

    source = urllib.request.urlopen(
        'http://api.openweathermap.org/data/2.5/weather?q ='
        + city + '&appid = your_api_key_here').read()

    # converting JSON data to a dictionary
    list_of_data = json.loads(source)

    # data for variable list_of_data
    data = {
        "country_code": str(list_of_data['sys']['country']),
        "coordinate": str(list_of_data['coord']['lon']) + ' '
                      + str(list_of_data['coord']['lat']),
        "temp": str(list_of_data['main']['temp']) + 'k',
        "pressure": str(list_of_data['main']['pressure']),
        "humidity": str(list_of_data['main']['humidity']),
    }
    print(data)


