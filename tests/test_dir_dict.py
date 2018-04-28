import unittest

from dir_dict import DirDict

class DirDictTestCase(unittest.TestCase):

    def test_make_dict(self):
        d = DirDict('dict1/storage')
        d['lang'] = 'Python'
        self.assertEqual('Python',d['lang'])

    def test_del(self):
        d = DirDict('dict2/storage')
        d['lang'] = 'Python'
        del d['lang']
        self.assertEqual(0,len(d))

    def test_keys(self):
        d = DirDict('dict/storage')
        d['lang'] = 'Python'
        d['lib'] = 'unittest'
        self.assertEqual(['lang','lib'], d.keys())

    def test_values(self):
        d = DirDict('dict/storage')
        d['lang'] = 'Python'
        d['lib'] = 'unittest'
        self.assertEqual(['Python','unittest'], d.values())

    def test_items(self):
        d = DirDict('dict/storage')
        d['lang'] = 'Python'
        d['lib'] = 'unittest'
        self.assertEqual([('lang','Python'),('lib','unittest')], d.items())


if __name__ == '__main__':
    unittest.main()



