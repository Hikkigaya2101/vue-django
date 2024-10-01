from .models import Unit
def gav():
    units = Unit.objects.all()

    return print(units)
