import pytest

# GET /genres Test
def test_get_all_genres_with_no_records(client):
    # Act
    response = client.get("/genres")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


def test_get_all_genres_with_records(client, two_saved_genres):
    # Act
    response = client.get("/genres")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [
        {
            "id": 1,
            "name": "Biography"
        },
        {
            "id": 2,
            "name": "Non-fiction"
        }
    ]


# POST /genres Test
def test_create_one_genre(client):
    # Act
    response = client.post("/genres", json={
        "name": "New genre",
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "New genre",
    }


# POST - EDGE tests cases create_genre
def test_create_one_genre_no_title(client):
    # Arrange
    test_data = {}

    # Act
    response = client.post("/genres", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {'message': 'Invalid request: missing name'}