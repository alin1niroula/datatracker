from django.shortcuts import render
import requests
import csv
# Create your views here.
def index(request):
    url ='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'

    r = requests.get(url,stream=True)
    f = (line.decode('utf-8') for line in r.iter_lines())
    reader = list(csv.reader(f))
    output = []
    todays_total = 0
    previous_total = 0
    for row in reader[1:]:
        temp = {
            'state':row[0],
            'country':row[1],
            'affected_people':row[-1]
        }
        todays_total += int(row[-1])
        previous_total += int(row[-2])
        output.append(temp)
    r.close()

    context = {
        'coronas':output,
        'todays_total':todays_total,
        'previous_total':previous_total,
    }
    return render(request,'index.html',context)