import requests 
from django.shortcuts import render

# Create your views here.

def index(request):
    appid = '0f7368fb6d8073123a090f9b507b6767'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid


    city = None
    city_info = None

    if request.method == 'POST':
        city = request.POST.get('city')
        res = requests.get(url.format(city)).json()

        if res.get('cod') != 200:
            city_info ={
                'city': 'City not found',
                'temp_max': None,
                'temp_min': None,
                'wind': None,
                'description': None,
                'icon': None,
                'country_info': None,
            }
        else:
            city_info = {
                'city': city,
                'temp_max': res["main"].get("temp_max") if "main" in res else "N/A",
                'temp_min': res["main"].get("temp_min") if "main" in res else "N/A",
                'wind': res["wind"].get("speed") if "wind" in res else "N/A",
                'description': res["weather"][0].get("description") if "weather" in res and len(res["weather"]) > 0 else "N/A",
                'icon': res["weather"][0].get("icon") if "weather" in res and len(res["weather"]) > 0 else None,
                'country_info': res["sys"].get("country") if "sys" in res else "N/A",
            }



    context = {'info': city_info}


    return render(request, 'weather/index.html', context)