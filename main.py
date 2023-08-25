import unittest
from unittest.mock import MagicMock, Mock


class Test (unittest.TestCase):

    magic_mock = MagicMock()

    mockObj = Mock()

    mockObj.return_value = 5
    magic_mock.side_effect = [2, 5, 3]

    print(mockObj())
    print(magic_mock())
    print(magic_mock())
    print(magic_mock())

    mockObj.assert_called_once()
    magic_mock.assert_called()


class Test2 (unittest.TestCase):
    def testEq(self):
        expect = 4
        got = 5
        self.assertEqual(expect, got, f"Expected {expect}, but got {got}")
        print("got expected results = 4")


unittest.main()
