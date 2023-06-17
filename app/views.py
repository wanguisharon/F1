from app.models import Driver, Race, Team
from django.shortcuts import render

# Create your views here.


def index(request):
    print(">>>>>>>>>", request.POST)
    if request.method == 'POST':
        team = Team.objects.create(
            name=request.POST.get('team'),
            country = request.POST.get('team_country')
        )
        team.save()

        driver = Driver.objects.create(
            name=request.POST.get('driver'),
            country = request.POST.get('driver_country'),
            team = team
        )
        driver.save()

        race = Race.objects.create(
            country = request.POST.get('race_country'),
            driver = driver,
            weight_before = request.POST.get('weight_before'),
        )
        race.save()

    return render(request, 'index.html')


def CheckWeight(request):
    if request.method == 'POST':
        weight = request.POST.get('weight')
        race = Race.objects.get(country = request.POST.get('country'))
        race.weight_before = weight
        race.save()
    else:
        races = Race.objects.all()
        drivers = Driver.objects.all()
        print("Driver", drivers)
        return render(request, 'index.html', {'races': races, 'drivers': drivers})

    return render(request, 'CheckWeight.html')