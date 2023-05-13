from .models import *

def facul(reauest):
    fact = Faculty.objects.all()
    return {'fact':fact}