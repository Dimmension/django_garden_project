"""Module that provides admin panel config."""
from django.contrib import admin
from django.contrib.gis import admin as gis_admin
from garden_app import models


@admin.register(models.Flora)
class FloraAdmin(admin.ModelAdmin):
    """Admin class for Flora model."""

    model = models.Flora


@gis_admin.register(models.Coord)
class CoordsAdmin(gis_admin.GISModelAdmin):
    """Admin class for Coord model."""

    model = models.Coord


@admin.register(models.Label)
class LabelAdmin(admin.ModelAdmin):
    """Admin class for Label model."""

    model = models.Label


@admin.register(models.CollectPlace)
class CollectPlaceAdmin(admin.ModelAdmin):
    """Admin class for CollectPlace model."""

    model = models.CollectPlace


@admin.register(models.Herbarium)
class HerbariumAdmin(admin.ModelAdmin):
    """Admin class for Herbarium model."""

    model = models.Herbarium


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin class for Comment model."""

    model = models.Comment


@admin.register(models.Taxon)
class TaxonAdmin(admin.ModelAdmin):
    """Admin class for Taxon model."""

    model = models.Taxon
