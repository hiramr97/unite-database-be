# from rest_framework import routers
from rest_framework.routers import DefaultRouter
# from .views import PokemonViewSet, EvolutionViewSet, BuildsViewSet, HeldItemsViewSet, BattleItemsViewSet, BuildSkillsViewSet, SkillsViewSet, SkillUpgradesViewSet, PokemonList, PokemonDetail
from . import views
from django.urls import path


# router = routers.DefaultRouter()
# router.register('pokemon', PokemonViewSet, 'pokemon')


urlpatterns = [
    path('', views.PokemonList.as_view(), name='pokemon_list'),
    path('pokemon/<int:pk>/', views.PokemonDetail.as_view(), name='pokemon_detail'),
    path('evolution/', views.EvolutionList.as_view(), name='evolution_list'),
    path('evolution/<int:pk>/', views.EvolutionDetail.as_view(),
         name='evolution_detail'),
    path('builds/', views.BuildsList.as_view(), name='builds_list'),
    path('builds/<int:pk>/', views.BuildsDetail.as_view(), name='build_detail'),
    path('held-items/', views.HeldItemsList.as_view(), name='held_items_list'),
    path('held-items/<int:pk>/', views.HeldItemsDetail.as_view(),
         name='held_items_detail'),
    path('battle-items/', views.BattleItemsList.as_view(),
         name='battle_items_list'),
    path('battle-items/<int:pk>/', views.BattleItemsDetail.as_view(),
         name='battle_items_detail'),
    path('skills/', views.SkillsList.as_view(), name='skills_list'),
    path('skills/<int:pk>/', views.SkillsDetail.as_view(), name='skills_detail'),
    path('skill-upgrades/', views.SkillUpgradesList.as_view(),
         name='skill_upgrades_list'),
    path('skill-upgrades/<int:pk>/', views.SkillUpgradesDetail.as_view(),
         name='skill_upgrades_detail'),
]


# router.register('evolution', EvolutionViewSet, 'evolution')
# router.register('builds', BuildsViewSet, 'builds')
# router.register('held_items', HeldItemsViewSet, 'held_items')
# router.register('battle_items', BattleItemsViewSet, 'battle_items')
# router.register('build_skills', BuildSkillsViewSet, 'builds_skills')
# router.register('skills', SkillsViewSet, 'skills')
# router.register('skill_upgrades', SkillUpgradesViewSet, 'skill_upgrades')


# urlpatterns = router.urls
