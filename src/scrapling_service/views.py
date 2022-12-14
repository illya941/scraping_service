from django.shortcuts import render


def home(request):
    first_name = 'Illya'
    last_name = 'Mazhara'
    data_dict = {'first_name': first_name, 'last_name': last_name}
    return render(request, 'home.html', {'data_dict': data_dict.items(), 'first_name': first_name})


def about(request):
    return render(request, 'about.html')
