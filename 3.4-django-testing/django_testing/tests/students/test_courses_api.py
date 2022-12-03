import pytest
from random import randint


@pytest.mark.django_db
def test_get_courses_list(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    for i, c in enumerate(data):
        assert c['name'] == courses[i].name


@pytest.mark.django_db
def test_get_courses_retrieve(client, course_factory):
    course = course_factory()
    response = client.get(f'/api/v1/courses/{course.id}/')
    assert response.status_code == 200
    assert response.json()['name'] == course.name


@pytest.mark.django_db
def test_get_courses_id_filtering(client, course_factory):
    courses = course_factory(_quantity=10)
    some_id = courses[randint(0,len(courses)-1)].id
    some_course = [c for c in courses if c.id == some_id]
    response = client.get(f'/api/v1/courses/?id={some_id}')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(some_course) == 1
    assert data[0]['name'] == some_course[0].name


@pytest.mark.django_db
def test_get_courses_name_filtering(client, course_factory):
    courses = course_factory(_quantity=10)
    some_name = courses[randint(0,len(courses)-1)].name
    some_courses = [c for c in courses if c.name == some_name]
    some_courses.sort(key=lambda x: x.id)
    response = client.get(f'/api/v1/courses/?name={some_name}')
    assert response.status_code == 200
    data = response.json()
    data.sort(key=lambda x: x['id'])
    assert len(data) == len(some_courses)
    for i, c in enumerate(data):
        assert c['id'] == some_courses[i].id


@pytest.mark.django_db
def test_post_courses(client):
    response = client.post('/api/v1/courses/', {'name': 'test'}, format='json')
    assert response.status_code == 201
    assert response.json()['name'] == 'test'


@pytest.mark.django_db
def test_put_courses(client, course_factory):
    course = course_factory()
    response = client.put(f'/api/v1/courses/{course.id}/', {'name': 'test'}, format='json')
    assert response.status_code == 200
    assert response.json()['name'] == 'test'


@pytest.mark.django_db
def test_delete_courses(client, course_factory):
    course = course_factory()
    assert client.delete(f'/api/v1/courses/{course.id}/').status_code == 204
    assert client.get(f'/api/v1/courses/{course.id}/').status_code == 404
