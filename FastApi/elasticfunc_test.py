import unittest
import elasticfunc

class elasticfunc_test(unittest.TestCase):
    def test_get_data_id_company(self):
        result = {'id': '33060',
                  'inn': '8932856627',
                  'revenue': -1882500.0,
                  'profit': 357000.0,
                  'name': 'Крупный возвращение',
                  'is_ip': False,
                  'reg_date': '2016-04-01',
                  'liq_date': None,
                  'okved': '18.9.13.1',
                  'region': '89'}
        self.assertEqual(elasticfunc.get_data_id(33060), result)
    def test_get_data_id_person(self):
        result = {
                  "lastname": "Гаврилов",
                  "firstname": "Глеб",
                  "patronymyic": "Алериевич",
                  "inn": "438340953608",
                  "id": "128"
                }
        self.assertEqual(elasticfunc.get_data_id(128), result)