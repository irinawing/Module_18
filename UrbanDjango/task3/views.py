from django.shortcuts import render

# Create your views here.
def game_platform(request):
    return render(request, 'third_task/platform.html', context=game)

def game(request):
    games = {
        'first': 'WOW',
        'second': 'Mu Dark Epoch',
        'third': 'Raid Shadow Legends',
    }
    return render(request, "third_task/games.html")

def cart(request):
    return render(request, "third_task/cart.html")