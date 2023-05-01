from rest_framework import routers
from .views import PokemonViewSet, EvolutionViewSet, BuildsViewSet, HeldItemsViewSet

router = routers.DefaultRouter()
router.register('pokemon', PokemonViewSet, 'pokemon')
router.register('evolution', EvolutionViewSet, 'evolution')
router.register('builds', BuildsViewSet, 'builds')
router.register('held_items', HeldItemsViewSet, 'held_items')


urlpatterns = router.urls