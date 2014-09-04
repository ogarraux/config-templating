from DataSource import DataSource
import csv

# Assumptions:
#  - first line of CSV = headers that correspond to variables in template


class CsvDataSource(DataSource):
    def __init__(self, csv_file_path, delimiter=','):
        """
        :param csv_file_path: Path to CSV data source file
        :param delimiter: delimiter that CSV file uses
        """
        super(CsvDataSource, self).__init__()
        csv_fh = open(csv_file_path, 'rb')
        self._csv_r = csv.reader(csv_fh, delimiter=delimiter)
        # First row must be headers
        self.variables = self._csv_r.next()
        self.index = 0

    def next(self):
        """
        :return: dict containing mapping of header to value
        """
        try:
            next_values_list = self._csv_r.next()
            self.index += 1
            return {self.variables[i]: next_values_list[i]
                    for i in range(0, self.variables.__len__())}
        except IndexError:
            raise StopIteration
