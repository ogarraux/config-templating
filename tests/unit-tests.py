import unittest
from CsvDataSource import CsvDataSource


class CsvDataSourceTests(unittest.TestCase):
    def test_variables(self):
        cds = CsvDataSource("examples/test.csv")
        self.assertEqual(cds.variables,
                         ['instance_title', 'head1', 'head2', 'head3'])

if __name__ == "__main__":
    unittest.main()
