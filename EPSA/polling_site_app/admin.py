from django.contrib import admin
from .models import State, County, CityOrTown, PollingSite

admin.site.register(State)
admin.site.register(County)
admin.site.register(CityOrTown)
admin.site.register(PollingSite)
