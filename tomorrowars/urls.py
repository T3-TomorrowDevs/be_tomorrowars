"""tomorrowars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from game.views import PlanetArmyFormAPIView
from battle.views import BattleSearchAPIView, BattleFightAPIViews
from user_account.views import LoginAPIView
from shop.views import ShopAPIView, UserTroopsAPIViews

urlpatterns = [
    path('admin/', admin.site.urls),

    path("game/planet-army/", PlanetArmyFormAPIView.as_view(), name='planet-army-name'),  # planet army form endpoint

    path('battle-search/', BattleSearchAPIView.as_view(), name='battle-search'),  # search battle fight endpoint
    path('battle-fight/', BattleFightAPIViews.as_view(), name='battle-fight'),    # battle fight endpoint
    path('testlogin/', LoginAPIView.as_view()),  # endpoint test google login

    path('shop/', ShopAPIView.as_view(), name='shop'),                   # to show all available troops to buy
    path('buy-troops/', UserTroopsAPIViews.as_view(), name='troops'),    # to buy troops for the user

]
