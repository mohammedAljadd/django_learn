from django.shortcuts import render


rooms = [
    {'id': 1, 'name': 'Learn python'},
    {'id': 2, 'name': 'Design'},
    {'id': 3, 'name': 'Frontend'},
    
]


# Create your views here.
def home(request):
    return render(request, 'base/home.html', {'rooms': rooms})

def room(request, pk):
    room = rooms[int(pk)-1]
    return render(request, 'base/room.html', {'room': room})