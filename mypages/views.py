from django.shortcuts import render
from datetime import datetime
# Create your views here.
def home(request):
    context = {
        "username": "Maryam Elrefaey"
    }
    return render(request, 'home.html', context)


def about(request):
    context = {
        "username": "Maryam Elrefaey",
        "current_time": datetime.now(),
    }
    return render(request, 'about.html', context)

def hobbies(request):
    hobbies_list = [
        "Drawing 🎨",
        "Singing 🎤",
        "Learning new things 📚",
        "Traveling ✈️",
        "Video games 🎮",
        "Badminton 🏸",
        "Swimming 🏊‍♀️",
        "Archery 🏹",
        "Horse riding 🐎",
    ]
    context = {"hobbies": hobbies_list}
    return render(request, 'hobbies.html', context)

