import csv

class CSVPrinter:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        with open(self.file_name) as f:
            reader = csv.reader(f)
            lines = [row for row in reader]
        return lines

    def all_read(self):
        with open(self.file_name) as f:
            lines = f.reader()
        return lines

    def comma_read(self):
        with open(self.file_name) as f:
            lines = f.reader()
            commma = [row for row in lines.split(",")]
        return commma
