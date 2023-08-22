import unittest
from speciallecture.CSVPrinter import CSVPrinter

class TestCSVPrinter(unittest.TestCase):

    def test_read(self):
        printer = CSVPrinter("sample.csv")
        l = printer.read()
        self.assertEqual(3,len(l))

    def test_read2(self):
        printer = CSVPrinter("sample.csv")
        line = printer.read()
        self.assertEqual(3,len(line))

    def test_read3(self):
        printer = CSVPrinter("sample.csv")
        comma = printer.read()
        self.assertEqual("old",comma[1][1])

    def test_read4(self):
        try:
            printer = CSVPrinter("sample.csv")
            printer.read()
            unittest.TestCase.fail("There is None.")
        except Exception:
            pass
