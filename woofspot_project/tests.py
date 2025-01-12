from django.test import TestCase, RequestFactory
from .views import trigger_400, trigger_403, trigger_500


class Custom400PageTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_400_error_page(self):
        request = self.factory.get("/trigger-400/")

        response = trigger_400(request)

        self.assertEqual(response.status_code, 400)

        self.assertIn(b"This is a test for the 400 error page", response.content)


class Custom403PageTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_403_error_page(self):
        request = self.factory.get("/trigger-403/")
        response = trigger_403(request)
        self.assertEqual(response.status_code, 403)
        self.assertIn(b"Access denied", response.content)


class Custom404PageTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_404_error_page(self):
        response = self.client.get("/non-existent-url/")
        self.assertEqual(response.status_code, 404)
        self.assertContains(response, "Oops! Page Not Found", status_code=404)



class Custom500PageTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_500_error_page(self):
        request = self.factory.get("/trigger-500/")

        with self.assertRaises(Exception) as context:
            trigger_500(request)

        self.assertEqual(str(context.exception), "This is a test exception for the 500 error page.")
