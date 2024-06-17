"""Module that provides models."""
from uuid import uuid4

from django.contrib.gis.db import models as gis_models
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_minio_backend import MinioBackend, iso_date_prefix
from garden_app import consts, validators


class UUIDMixin(models.Model):
    """Mixin for adding UUID field to models."""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    class Meta:
        abstract = True


class CollectPlace(UUIDMixin, models.Model):
    """Model that represents place where flora was collected."""

    country = models.TextField(
        _('Country'),
        blank=False,
        null=False,
        max_length=consts.MAX_LENGTH_COUNTRY,
    )
    region = models.TextField(
        _('Region'),
        blank=False,
        null=False,
        max_length=consts.MAX_LENGTH_REGION,
    )
    city = models.TextField(_('City'), blank=True, null=True, max_length=consts.MAX_LENGTH_CITY)
    coord = models.OneToOneField('Coord', models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = '"garden"."collect_place"'

    def __str__(self) -> str:
        return f'{self.id} {self.country} {self.region}'


class Comment(UUIDMixin, models.Model):
    """Model that represents comment for flora."""

    description = models.TextField(
        _('Description'),
        blank=False,
        null=False,
        max_length=consts.MAX_LENGTH_DESCRIPTION,
    )
    cool_facts = models.TextField(
        _('Cool facts'),
        blank=True,
        null=True,
        max_length=consts.MAX_LENGTH_COOL_FACTS,
    )
    ww_distribution = models.TextField(
        _('Distribution in the world'),
        blank=True,
        null=True,
        max_length=consts.MAX_LENGTH_WW_DISTRIBUTION,
    )
    protect = models.TextField(
        _('Protect'),
        blank=True,
        null=True,
        max_length=consts.MAX_LENGTH_PROTECT,
    )

    class Meta:
        db_table = '"garden"."comment"'

    def __str__(self) -> str:
        return f'{self.id}'


class Coord(UUIDMixin, models.Model):
    """Model that represents coordinates."""

    altitude = models.DecimalField(
        _('Altitude'),
        blank=True,
        null=True,
        decimal_places=consts.CORDS_MAX_DECIMAL,
        max_digits=consts.CORDS_MAX_DIGITS,
        default=0,
        validators=[validators.check_positive_height],
    )
    longitude = models.DecimalField(
        _('Longitude'),
        blank=False,
        null=False,
        decimal_places=consts.CORDS_MAX_DECIMAL,
        max_digits=consts.CORDS_MAX_DIGITS,
        default=0,
        validators=[validators.check_coords],
    )
    latitude = models.DecimalField(
        _('Latitude'),
        blank=False,
        null=False,
        decimal_places=consts.CORDS_MAX_DECIMAL,
        max_digits=consts.CORDS_MAX_DIGITS,
        default=0,
        validators=[validators.check_coords],
    )
    geog_point = gis_models.PointField(
        _('Latitude and Longitude'),
        geography=True,
        blank=True,
        null=True,
    )

    class Meta:
        db_table = '"garden"."coord"'

    def __str__(self) -> str:
        return f'{self.id} {self.latitude} {self.longitude}'


class Flora(UUIDMixin, models.Model):
    """Model that represents flora."""

    author = models.TextField(
        _('Author'),
        blank=False,
        null=False,
        max_length=consts.MAX_LENGTH_AUTHOR,
    )
    alive = models.BooleanField(_('Alive'), blank=False, null=False, default=True)
    taxonomycol = models.TextField(
        _('Taxonomy COL'),
        blank=False,
        null=False,
        max_length=consts.MAX_LENGTH_TAXONOMY_COL,
    )
    geo_author = models.TextField(
        _('Georeferencing author'),
        blank=True,
        null=True,
        max_length=consts.MAX_LENGTH_GEO_AUTHOR,
    )
    rus_name = models.TextField(
        _('Russian Name'),
        blank=True,
        null=True,
        max_length=consts.MAX_LENGTH_RUS_NAME,
    )
    autochthony = models.TextField(
        _('Autochthony'),
        blank=True,
        null=True,
        choices=(
            ('autochthonous', _('autochthonous')),
            ('introduced', _('introduced')),
            ('invasive', _('invasive')),
        ),
    )

    created = models.DateTimeField(
        _('Create date'),
        blank=True,
        null=True,
        default=validators.get_datetime,
        validators=[validators.check_date],
    )
    picture = models.ImageField(
        _('Image'),
        blank=True,
        storage=MinioBackend(bucket_name=consts.BUCKET_NAME),
        upload_to=iso_date_prefix,
    )

    taxon = models.OneToOneField('Taxon', models.CASCADE, blank=True, null=True)
    collect_place = models.OneToOneField('CollectPlace', models.CASCADE, blank=True, null=True)
    herbarium = models.OneToOneField('Herbarium', models.CASCADE, blank=True, null=True)
    comment = models.OneToOneField('Comment', models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = '"garden"."flora"'
        ordering = ['taxonomycol', 'author']

    def __str__(self) -> str:
        return f'{self.id} {self.author} {self.taxonomycol}'


class Herbarium(UUIDMixin, models.Model):
    """Model that represents herbarium."""

    depart = models.TextField(_('Department'), blank=False, null=False)
    region = models.TextField(_('Region'), blank=False, null=False)

    class Meta:
        db_table = '"garden"."herbarium"'

    def __str__(self) -> str:
        return f'{self.depart} {self.region}'


class Label(UUIDMixin, models.Model):
    """Model that represents label for flora."""

    institute = models.TextField(
        _('Institute'),
        blank=False,
        null=False,
        max_length=consts.MAX_LENGTH_INSTITUTE,
    )
    project = models.TextField(
        _('Project'),
        blank=False,
        null=False,
        max_length=consts.MAX_LENGTH_PROJECT,
    )
    name = models.TextField(
        _('Label from Name'),
        blank=False,
        null=False,
        max_length=consts.MAX_LENGTH_LABEL_NAME,
    )
    description = models.TextField(
        _('Description'),
        blank=True,
        null=True,
        max_length=consts.MAX_LENGTH_DESCRIPTION,
    )
    morph_features = models.TextField(
        _('Morph features'),
        blank=True,
        null=True,
        max_length=consts.MAX_LENGTH_MORPH_FEATURES,
    )

    collected = models.DateField(
        _('Collected'),
        blank=True,
        null=True,
        validators=[validators.check_date],
    )

    plant = models.ForeignKey('Flora', models.CASCADE, blank=True, null=True)
    coord = models.OneToOneField('Coord', models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = '"garden"."label"'

    def __str__(self) -> str:
        return f'{self.id} {self.institute} {self.project}'


class Taxon(UUIDMixin, models.Model):
    """Model that represents taxon."""

    genus = models.TextField(
        _('Genus'),
        blank=False,
        null=False,
        max_length=consts.MAN_TAXON_LENGTH,
    )
    species = models.TextField(
        _('Species'),
        blank=False,
        null=False,
        max_length=consts.MAN_TAXON_LENGTH,
    )
    domain = models.TextField(
        _('Domain'),
        blank=True,
        null=True,
        max_length=consts.MAN_TAXON_LENGTH,
    )
    kingdom = models.TextField(
        _('Kingdom'),
        blank=True,
        null=True,
        max_length=consts.MAN_TAXON_LENGTH,
    )
    phylum = models.TextField(
        _('Phylum'),
        blank=True,
        null=True,
        max_length=consts.MAN_TAXON_LENGTH,
    )
    klass = models.TextField(_('Class'), blank=True, null=True, max_length=consts.MAN_TAXON_LENGTH)
    ordo = models.TextField(_('Type'), blank=True, null=True, max_length=consts.MAN_TAXON_LENGTH)
    family = models.TextField(
        _('Family'),
        blank=True,
        null=True,
        max_length=consts.MAN_TAXON_LENGTH,
    )
    subspecies = models.TextField(
        _('Subspecies'),
        blank=True,
        null=True,
        max_length=consts.MAN_TAXON_LENGTH,
    )

    class Meta:
        db_table = '"garden"."taxon"'

    def __str__(self) -> str:
        return f'{self.id} {self.genus} {self.species}'
