import pytest


@pytest.mark.usefixtures("setup")
class TestDemo:

      def test_first(self):
         print("First Case")

      def test_second(self):
          print("Seond Test")

      def test_Third(self):
          print("Third Test")