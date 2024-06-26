import json

from django.shortcuts import render


# Create your views here.


def index(request):
    context = {}
    return render(request, "index.html", context)


def query(request):
    zipcode = request.POST['zipcode']
    min = int(zipcode) - 1000
    max = int(zipcode) + 1000
    # rows = Restaurant.objects.filter(zipcode__gt=min, zipcode__lt=max).all()
    rows = []
    with open('data.json', 'r', encoding='utf8') as j:
        ls = json.loads(j.read())
        for i in ls:
            if i['zipcode'] >= min and i['zipcode'] <= max:
                rows.append(i)

    print(rows)
    # return HttpResponse("Hello, world. You're at the polls index.")
    context = {'zipcode': zipcode, "rows": rows}
    return render(request, "list.html", context)
