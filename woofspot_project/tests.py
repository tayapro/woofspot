from django.test import TestCase, RequestFactory
from .views import trigger_500


class Custom500PageTest(TestCase):
    def setUp(self):
        # Initialize the RequestFactory
        self.factory = RequestFactory()

    def test_500_error_page(self):
        # Simulate a GET request to the 500 error trigger URL
        request = self.factory.get("/trigger-500/")

        # Call the `trigger_500` view function directly
        with self.assertRaises(Exception) as context:
            trigger_500(request)

        # Verify that the exception message matches the expected one
        self.assertEqual(str(context.exception), "This is a test exception for the 500 error page.")
