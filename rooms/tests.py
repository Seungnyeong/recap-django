from email import header
from rest_framework.test import APITestCase
from . import models
from users.models import User


class TestAmenities(APITestCase):

    NAME = "Amentity Test"
    DESC = "Amentity Des"

    def setUp(self) -> None:
        models.Amenity.objects.create(name=self.NAME, description=self.DESC)

    def test_all_amenities(self):

        headers = {
            "jwt": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwayI6MX0.WTbJVh05F9lwVrOfc17S_o6_Bv2HW_gyd7PpCMm6f_g"
        }

        response = self.client.get("/api/v1/rooms/amenities/", headers)
        data = response.json()
        self.assertEqual(response.status_code, 200, "Status code isn't 200.")
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["name"], self.NAME)
        self.assertEqual(data[0]["description"], self.DESC)

    def test_create_amenity(self):
        new_amentity_name = "New Amenities"
        new_amentity_desc = "New Amenities Description"
        response = self.client.post(
            "/api/v1/rooms/amenities/",
            data={"name": new_amentity_name, "description": new_amentity_desc},
        )

        data = response.json()
        self.assertEqual(response.status_code, 200, "Nont 200 status code")
        self.assertEqual(data["name"], new_amentity_name)
        self.assertEqual(data["description"], new_amentity_desc)

        response = self.client.post("/api/v1/rooms/amenities/")
        self.assertEqual(response.status_code, 400)
        self.assertIn("name", data)


class TestAmenity(APITestCase):

    NAME = "Test Amenity"
    DESC = "Test Amenity Desc"

    def setUp(self):
        models.Amenity.objects.create(name=self.NAME, description=self.DESC)

    def test_get_amenity(self):
        response = self.client.get("/api/v1/rooms/amenities/2")
        self.assertEqual(response.status_code, 404)

        response = self.client.get("/api/v1/rooms/amenities/1")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["name"], self.NAME)
        self.assertEqual(data["description"], self.DESC)

    def test_delete_amenity(self):

        response = self.client.delete("/api/v1/rooms/amenities/")
        self.assertEqual(response.status_code, 204)


class TestRoom(APITestCase):
    def setUp(self):
        user = User.objects.craete(
            username="se",
        )
        user.set_password("!23")
        user.save()
        self.user = user

    def test_create_room(self):
        response = self.client.post("/api/v1/rooms/")
        self.assertEqual(response.status_code, 403)

        response = self.client.force_login(
            self.user,
        )

        response = self.client.post("/api/v1/rooms/")
