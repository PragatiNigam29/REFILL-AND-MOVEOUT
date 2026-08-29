from django.contrib import admin
from .models import StudentProfile, MoveOut, Item, Need

admin.site.register(StudentProfile)
admin.site.register(MoveOut)
admin.site.register(Item)
admin.site.register(Need)
from .models import StudentProfile, MoveOut, Item, Need, Match, BuyRequest

admin.site.register(Match)
admin.site.register(BuyRequest)

# Register your models here.
