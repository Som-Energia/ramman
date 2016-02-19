import os
import csv
import unittest
from ramman import Ramman


def read_from_file(filename):
    entries = []
    with open(filename, 'rb') as f:
        reader = csv.reader(f, delimiter=';')
        entries = [row for row in reader]
    return entries


class HemanResultsTest(unittest.TestCase):
    client = None

    @classmethod
    def setUpClass(self):
        config = {
            'url': os.getenv('HEMAN_URL', None),
            }
        self.client = Ramman(config)

    def test_ot101_1(self):
        attrs = [u'diffAverageConsumption',
                 u'criteriaSelected',
                 u'numberCustomersEff',
                 u'consumption',
                 u'consumptionNumberOfDays',
                 u'averageEffConsumption',
                 u'month',
                 u'numberCustomers',
                 u'averageConsumption',
                 u'diffAverageEffConsumption',
                 u'contractId']

        contract = read_from_file('data/test_ot101_1.csv')[0]
        results = self.client.get(contract[0], contract[1], 'OT101')

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].keys(), attrs)

if __name__ == '__main__':
    unittest.main()
