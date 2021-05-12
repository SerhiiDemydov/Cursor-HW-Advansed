import unittest
from unittest.mock import patch
from employee import Employee


class mockResponseTrue:
    status_code = 200
    elapsed = 100
    text = "response.ok = True"
    ok = True

    def __init__(self, *args, **kwargs):
        pass

class mockResponseFalse:
    status_code = 200
    elapsed = 100
    text = "response.ok = False"
    ok = False

    def __init__(self, *args, **kwargs):
        pass


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.classTest = Employee("Serhii", "Demydov", 15000)

    def test_email(self):
        self.assertEqual(self.classTest.email, "Serhii.Demydov@email.com")

    def test_fullname(self):
        self.assertEqual(self.classTest.fullname, "Serhii Demydov")

    def test_apply_raise(self):
        self.classTest.apply_raise()
        self.assertEqual(self.classTest.pay, 15750)

    @patch("employee.requests.get")
    def test_monthly_schedule(self, mocker):
        # mocker.return_value.status_code = 404
        mocker.side_effect = mockResponseTrue
        print(self.classTest.monthly_schedule('april'))
        self.assertEqual(self.classTest.monthly_schedule('april'), "response.ok = True")
        mocker.side_effect = mockResponseFalse
        print(self.classTest.monthly_schedule('april'))
        self.assertEqual(self.classTest.monthly_schedule('april'), "Bad Response!")


