from dashboards.dashboard import Dashboard
from dashboards.component import Text, Chart
from dashboards.registry import registry

from demo.mydashboard.data import DashboardData


class FirstDashboard(Dashboard):
    welcome = Text(value="Welcome to Django Dashboards!")
    animals = Chart(defer=DashboardData.fetch_animals)

    class Meta:
        name = "First Dashboard"


registry.register(FirstDashboard)