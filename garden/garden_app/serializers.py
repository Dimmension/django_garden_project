"""Module that provides serializers."""
from garden_app import models
from rest_framework.serializers import HyperlinkedModelSerializer

ALL = '__all__'


class CollectPlaceSerializer(HyperlinkedModelSerializer):
    """Serializer for the CollectPlace model."""

    class Meta:
        model = models.CollectPlace
        fields = ALL


class CommentSerializer(HyperlinkedModelSerializer):
    """Serializer for the Comment model."""

    class Meta:
        model = models.Comment
        fields = ALL


class CoordSerializer(HyperlinkedModelSerializer):
    """Serializer for the Coord model."""

    class Meta:
        model = models.Coord
        fields = ALL


class FloraSerializer(HyperlinkedModelSerializer):
    """Serializer for the Flora model."""

    class Meta:
        model = models.Flora
        fields = ALL


class HerbariumSerializer(HyperlinkedModelSerializer):
    """Serializer for the Herbarium model."""

    class Meta:
        model = models.Herbarium
        fields = ALL


class LabelSerializer(HyperlinkedModelSerializer):
    """Serializer for the Label model."""

    class Meta:
        model = models.Label
        fields = ALL


class TaxonSerializer(HyperlinkedModelSerializer):
    """Serializer for the Taxon model."""

    class Meta:
        model = models.Taxon
        fields = ALL
