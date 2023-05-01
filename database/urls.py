from rest_framework import routers
from .views import PokemonViewSet, EvolutionViewSet, BuildsViewSet, HeldItemsViewSet, BattleItemsViewSet

router = routers.DefaultRouter()
router.register('pokemon', PokemonViewSet, 'pokemon')
router.register('evolution', EvolutionViewSet, 'evolution')
router.register('builds', BuildsViewSet, 'builds')
router.register('held_items', HeldItemsViewSet, 'held_items')
router.register('battle_items', BattleItemsViewSet, 'battle_items')


urlpatterns = router.urls