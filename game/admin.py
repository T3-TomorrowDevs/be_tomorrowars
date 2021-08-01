from django.contrib import admin

from game.models import PlanetArmy, GameAccount, UserTroop

admin.site.register(PlanetArmy)
admin.site.register(GameAccount)
admin.site.register(UserTroop)

# Register your models here.
