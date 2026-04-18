from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    NewsArticleViewSet, MatchViewSet, LeagueStandingViewSet,
    MatchVideoViewSet, PlayerViewSet, CoachingStaffViewSet,
    GalleryViewSet, DocumentViewSet, ContactMessageViewSet,
    NewsletterViewSet
)

router = DefaultRouter()
router.register(r'news', NewsArticleViewSet, basename='news')
router.register(r'matches', MatchViewSet, basename='match')
router.register(r'league-standings', LeagueStandingViewSet, basename='league-standing')
router.register(r'videos', MatchVideoViewSet, basename='video')
router.register(r'players', PlayerViewSet, basename='player')
router.register(r'coaching-staff', CoachingStaffViewSet, basename='coaching-staff')
router.register(r'gallery', GalleryViewSet, basename='gallery')
router.register(r'documents', DocumentViewSet, basename='document')
router.register(r'contact', ContactMessageViewSet, basename='contact')
router.register(r'newsletter', NewsletterViewSet, basename='newsletter')

urlpatterns = [
    path('', include(router.urls)),
]
