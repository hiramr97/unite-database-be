from rest_framework import routers
from .views import PokemonViewSet, EvolutionViewSet

router = routers.DefaultRouter()
router.register('pokemon', PokemonViewSet, 'pokemon')
router.register('evolution', EvolutionViewSet, 'evolution')

urlpatterns = router.urls