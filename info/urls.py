from django.urls import path
from .views import *
from .scripts import *


app_name = "info"

urlpatterns = [
    path('abcd/',createusers),
    path('', home,name="home"),
    path('profile/<slug:username>/',profile,name="profile"),

    path('sets/', setsPage,name="setsPage"),
    path('donut/', donut,name="donut"),

    path('setReason/<slug:username>/<slug:reason>/',setReason,name="set"),
    path('setReason/',setReasonPage,name="setpage"),
    path('setReason/<slug:reason>/',setReasonlist,name="setlist"),

    path('setCity/<slug:username>/<slug:cityName>/',setCity,name="setCity"),
    path('setCity/',setCityPage,name="setCityPage"),
    path('setCity/<slug:cityName>/',setCitylist,name="setCitylist"),

    # path('setFriendPage/',setFriendPage,name="setFriendPage"),
    # path('setFriendByCityPage/',setFriendByCityPage,name="setFriendByCityPage"),

    path('setRate/',setRatePage,name="setRatePage"),
    path('setRate/<slug:username>/<int:Rate>',setRate,name="setRate"),
    path('setRateByCityPage/',setRateByCityPage,name="setRateByCityPage"),
    path('setRateByCityList/<slug:cityName>/',setRateByCityList,name="setRateByCityList"),
    # path('setRate/<slug:username>/<slug:cityName>/',setCity,name="setCity"),

    path('charts/', charts,name="charts"),
    path('charts/DonutChart/', DonutChart,name="DonutChart"),
    path('charts/lineChart/', lineChart,name="lineChart"),
    path('charts/lineChart/Percentage/', lineChartPercentage,name="lineChartPercentage"),
    path('charts/lineChartCity/Percentage/', lineChartPercentageCity,name="lineChartPercentageCity"),
    path('charts/radarChart/', radarChart,name="radarChart"),


    path('orders/',ordersPage,name="ordersPage"),
    path('orders/orderingByReason/', orderingByReason,name="orderingByReason"),
    path('orders/orderingByCity/', orderingByCity,name="orderingByCity"),
    path('orders/orderingByRate/', orderingByRate,name="orderingByRate"),
    path('orders/userOrdering/', orderingByUser,name="userOrdering"),

    path('exports/excel/', Export_Excel,name="Export_Excel"),
]
