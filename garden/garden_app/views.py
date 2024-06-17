"""Module that provides views."""
from typing import Any

from django.contrib.auth import decorators, mixins
from django.core import paginator as django_paginator
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from garden_app import models, serializers, forms
from rest_framework import authentication, permissions, viewsets


class MyPermission(permissions.BasePermission):
    """Custom permission class that allows safe/unsafe methods for auth users and superusers."""

    _safe_methods = 'GET', 'HEAD', 'OPTIONS', 'PATCH'
    _unsafe_methods = 'POST', 'PUT', 'DELETE'

    def has_permission(self, request, _):
        """Check if the request has permission to access the resource.

        Args:
            request (HttpRequest): The incoming request.
            _: Placeholder for the view argument, not used in this permission.

        Returns:
            bool: True if the request has permission, False otherwise.
        """
        if request.method in self._safe_methods and (
            request.user and request.user.is_authenticated
        ):
            return True
        elif request.method in self._unsafe_methods and (
            request.user and request.user.is_superuser
        ):
            return True
        return False


def home_page(request):
    """Render the home page."""
    return render(
        request,
        'index.html',
        {
            'floras': models.Flora.objects.count(),
            'herbariums': models.Herbarium.objects.count(),
            'collectplaces': models.CollectPlace.objects.count(),
            'taxons': models.Taxon.objects.count(),
            'comments': models.Comment.objects.count(),
            'labels': models.Label.objects.count(),
            'coords': models.Coord.objects.count(),
        },
    )


def create_list_view(model_class, plural_name, template):
    """Create a generic ListView class.

    Args:
        model_class: The model class to use for the view.
        plural_name: The plural name of the model, used for context variables.
        template: The template to use for rendering the view.

    Returns:
        A custom ListView class.
    """

    class CustomListView(mixins.LoginRequiredMixin, ListView):
        """Custom ListView class."""

        model = model_class
        template_name = template
        paginate_by = 10
        context_object_name = plural_name

        def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
            """Get context data for the view."""
            context = super().get_context_data(**kwargs)
            books = model_class.objects.all()
            paginator = django_paginator.Paginator(books, 10)
            page = self.request.GET.get('page')
            page_obj = paginator.get_page(page)
            context[f'{plural_name}_list'] = page_obj
            return context

    return CustomListView


def create_view(model_class, context_name, template):
    """
    Create a view function that renders a template with an optional object.

    Args:
        model_class (type): The model class to retrieve an object from.
        context_name (str): The name of the context variable for the object.
        template (str): The path to the template to render.

    Returns:
        function: The view function.
    """

    @decorators.login_required
    def view(request):
        id_ = request.GET.get('id', None)
        target = model_class.objects.get(id=id_) if id_ else None
        context = {context_name: target}
        return render(
            request,
            template,
            context,
        )

    return view


def create_viewset(model_class, serializer):
    """
    Create a viewset for a given model class and serializer.

    Args:
        model_class (type): The model class to create a viewset for.
        serializer (type): The serializer class for the model.

    Returns:
        type: A custom viewset class.
    """

    class CustomViewSet(viewsets.ModelViewSet):
        serializer_class = serializer
        queryset = model_class.objects.all()
        permission_classes = [MyPermission]
        authentication_classes = [authentication.TokenAuthentication]

    return CustomViewSet


# REST Views
FloraViewSet = create_viewset(models.Flora, serializers.FloraSerializer)
CollectPlaceViewSet = create_viewset(models.CollectPlace, serializers.CollectPlaceSerializer)
LabelViewSet = create_viewset(models.Label, serializers.LabelSerializer)
CoordsViewSet = create_viewset(models.Coord, serializers.CoordSerializer)
TaxonViewSet = create_viewset(models.Taxon, serializers.TaxonSerializer)
CommentViewSet = create_viewset(models.Comment, serializers.CommentSerializer)
HerbariumViewSet = create_viewset(models.Herbarium, serializers.HerbariumSerializer)

# List Views
FloraListView = create_list_view(models.Flora, 'floras', 'catalog/floras.html')
CollectPlaceListView = create_list_view(
    models.CollectPlace, 'collect_places', 'catalog/collect_places.html',
)
LabelListView = create_list_view(models.Label, 'labels', 'catalog/labels.html')
CoordsListView = create_list_view(models.Coord, 'coords', 'catalog/coords.html')
TaxonListView = create_list_view(models.Taxon, 'taxons', 'catalog/taxons.html')
CommentListView = create_list_view(models.Comment, 'comments', 'catalog/comments.html')
HerbariumListView = create_list_view(models.Herbarium, 'herbariums', 'catalog/herbariums.html')

# Detail Views
flora_view = create_view(models.Flora, 'flora', 'entities/flora.html')
collect_place_view = create_view(
    models.CollectPlace, 'collect_place', 'entities/collect_place.html',
)
label_view = create_view(models.Label, 'label', 'entities/label.html')
coords_view = create_view(models.Coord, 'coord', 'entities/coord.html')
taxon_view = create_view(models.Taxon, 'taxon', 'entities/taxon.html')
comment_view = create_view(models.Comment, 'comment', 'entities/comment.html')
herbarium_view = create_view(models.Herbarium, 'herbarium', 'entities/herbarium.html')


class FloraCreateView(CreateView):
    """View for creating a new Flora object."""

    model = models.Flora
    form_class = forms.FloraForm
    template_name = 'flora_form.html'
