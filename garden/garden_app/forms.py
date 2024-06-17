"""Module that provides forms."""
from django import forms
from garden_app import consts, models


class FloraForm(forms.ModelForm):
    """Form for Flora model."""

    class Meta:
        model = models.Flora
        fields = '__all__'
        widgets = {
            'author': forms.TextInput(attrs={'maxlength': consts.MAX_LENGTH_AUTHOR}),
            'taxonomycol': forms.TextInput(
                attrs={'maxlength': consts.MAX_LENGTH_TAXONOMY_COL},
            ),
            'geo_author': forms.TextInput(
                attrs={'maxlength': consts.MAX_LENGTH_GEO_AUTHOR, 'required': False},
            ),
            'rus_name': forms.TextInput(
                attrs={'maxlength': consts.MAX_LENGTH_RUS_NAME, 'required': False},
            ),
            'picture': forms.FileInput(),
        }
