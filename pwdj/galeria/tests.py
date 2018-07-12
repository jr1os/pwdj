import pytest
from django.urls import reverse

from pwdj.django_assertions import dj_assert_contains
from pwdj.galeria.models import Model


def test_app_link_in_home(client):
    response = client.get('/')
    dj_assert_contains(response, reverse('galeria:index'))


@pytest.fixture
def galeria(db):
    model = Model(
        titulo='Social media now takes',
        preco='400.00',
        descricao='We need people like you, and we need people not like')

    model.save()
    return [model]


@pytest.fixture
def resp(client, galeria):
    return client.get(reverse('galeria:index'))


def test_status_code(resp):
    assert 200 == resp.status_code


@pytest.mark.parametrize(
    'content', [
        'TechPortfolio_Twitter_DeveloperHotfix-816x459_v1-1.jpg?w=816',
        'We need people like you', '400,00',
    ]
)
def test_index_content(resp, content):
    dj_assert_contains(resp, content)