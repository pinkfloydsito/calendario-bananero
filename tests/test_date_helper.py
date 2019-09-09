from datetime import datetime, timedelta
import unittest, os, sys

sys.path.append(os.path.abspath('..'))

from date_helper_pkg import DateHelper


class TestDatehelper(unittest.TestCase):
    """
    Tested according to dates available in http://190.90.66.114:8080/banasan/index.php?module=calendar&view=0&PHPSESSID=&ano=2017&mes=0&cal=2
    """

    def __init__(self, *args, **kwargs):
        super(TestDatehelper, self).__init__(*args, **kwargs)
        self.gen_test_data()

    def gen_test_data(self):
        dates = {
            2019: datetime.now().date().replace(year=2018, month=12, day=30),
            2018: datetime.now().date().replace(year=2017, month=12, day=28)
        }

        self.date_helper = DateHelper(dates)

    def test_get_leap(self):
        self.assertEqual(self.date_helper.get_leap(2019).days, -2, "Should be -2")

    def test_get_leap_2(self):
        self.assertEqual(self.date_helper.get_leap(2018).days, -4, "Should be -4")

    def test_get_weekdates_range(self):
        range = self.date_helper.get_weekdates_range(2019, 1)
        self.assertEqual(range[0], datetime.now().date().replace(year=2018, month=12, day=30), "Should be equal to 2018-12-30")

        self.assertEqual(range[1], datetime.now().date().replace(year=2019, month=1, day=5), "Should be equal to 2019-1-05")

    def get_periods_date_range(self):
        pass


if __name__ == '__main__':
    unittest.main()
