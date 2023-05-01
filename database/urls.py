from rest_framework import routers
from .views import PokemonViewSet, EvolutionViewSet, BuildsViewSet, HeldItemsViewSet, BattleItemsViewSet, BuildSkillsViewSet, SkillsViewSet, SkillUpgradesViewSet

router = routers.DefaultRouter()
router.register('pokemon', PokemonViewSet, 'pokemon')
router.register('evolution', EvolutionViewSet, 'evolution')
router.register('builds', BuildsViewSet, 'builds')
router.register('held_items', HeldItemsViewSet, 'held_items')
router.register('battle_items', BattleItemsViewSet, 'battle_items')
router.register('build_skills', BuildSkillsViewSet, 'builds_skills')
router.register('skills', SkillsViewSet, 'skills')
router.register('skill_upgrades', SkillUpgradesViewSet, 'skill_upgrades')


urlpatterns = router.urls
