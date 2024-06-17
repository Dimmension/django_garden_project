"""Tests API."""
from django.contrib.auth.models import User
from django.test import TestCase
from garden_app import models
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


def create_api_test(model, url, creation_attrs):
    """Create a TestCase class for API testing.

    Args:
        model: The Django model class to be tested.
        url: The API endpoint URL.
        creation_attrs: A dictionary of attributes for creating instances of the model.

    Returns:
        A TestCase class for API testing.
    """
    class ApiTest(TestCase):
        def setUp(self) -> None:
            self.client = APIClient()

            self.user = User.objects.create(
                username='vadim',
                password='vadim',
            )
            self.superuser = User.objects.create(
                username='admin',
                password='admin',
                is_superuser=True,
            )

            self.user_token = Token(user=self.user)
            self.superuser_token = Token(user=self.superuser)

        def manage(
            self,
            user: User,
            token: Token,
            post_expected: int,
            put_expected: int,
            delete_expected: int,
        ):
            self.client.force_authenticate(user=user, token=token)

            self.assertEqual(self.client.get(url).status_code, status.HTTP_200_OK)
            self.assertEqual(self.client.head(url).status_code, status.HTTP_200_OK)
            self.assertEqual(self.client.options(url).status_code, status.HTTP_200_OK)

            created_id = model.objects.create(**creation_attrs).id
            instance_url = f'{url}{created_id}/'

            put_response = self.client.put(instance_url, creation_attrs)
            self.assertEqual(put_response.status_code, put_expected)

            delete_response = self.client.delete(instance_url, creation_attrs)
            self.assertEqual(delete_response.status_code, delete_expected)
            self.assertEqual(self.client.post(url, creation_attrs).status_code, post_expected)

        def test_superuser(self):
            self.manage(
                self.superuser,
                self.superuser_token,
                post_expected=status.HTTP_201_CREATED,
                put_expected=status.HTTP_200_OK,
                delete_expected=status.HTTP_204_NO_CONTENT,
            )

        def test_user(self):
            self.manage(
                self.user,
                self.user_token,
                post_expected=status.HTTP_403_FORBIDDEN,
                put_expected=status.HTTP_403_FORBIDDEN,
                delete_expected=status.HTTP_403_FORBIDDEN,
            )

    return ApiTest


url = '/api/'


CollectPlaceApiTest = create_api_test(
    models.CollectPlace, f'{url}collect_places/', {'country': 'Russia', 'region': 'Moscow'},
)

CommentApiTest = create_api_test(
    models.Comment, f'{url}comments/', {'description': 'some_description'},
)

CoordApiTest = create_api_test(
    models.Coord, f'{url}coords/', {'altitude': 3.893, 'longitude': 21.433, 'latitude': 12.343},
)

FloraApiTest = create_api_test(
    models.Flora, f'{url}floras/', {'alive': True, 'author': 'Ford', 'taxonomycol': 'Forda'},
)

HerbariumApiTest = create_api_test(
    models.Herbarium, f'{url}herbariums/', {'depart': 'Russia', 'region': 'Moscow'},
)

LabelApiTest = create_api_test(
    models.Label, f'{url}labels/', {'institute': 'Russia', 'project': 'Moscow', 'name': 'forda'},
)

TaxonApiTest = create_api_test(models.Taxon, f'{url}taxons/', {'genus': 'asd', 'species': 'asd'})
