import unittest
import os
import tempfile

from dir_dict import DirDict

class DirDictTestCase(unittest.TestCase):

    def test_make_dict(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            d = DirDict(os.path.join(str(tmpdirname),'dict1/storage'))
            d['lang'] = 'Python'
            self.assertEqual('Python',d['lang'])

    def test_del(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            d = DirDict(os.path.join(str(tmpdirname), 'dict2/storage'))
            d['lang'] = 'Python'
            del d['lang']
            self.assertEqual(0,len(d))


    def test_keys(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            d = DirDict(os.path.join(str(tmpdirname), 'dict3/storage'))
            d['lang'] = 'Python'
            d['lib'] = 'unittest'
            self.assertEqual(['lang','lib'], d.keys())

    def test_values(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            d = DirDict(os.path.join(str(tmpdirname), 'dict4/storage'))
            d['lang'] = 'Python'
            d['lib'] = 'unittest'
            self.assertEqual(['Python','unittest'], d.values())

    def test_items(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            d = DirDict(os.path.join(str(tmpdirname), 'dict5/storage'))
            d['lang'] = 'Python'
            d['lib'] = 'unittest'
            self.assertEqual([('lang','Python'),('lib','unittest')], d.items())



if __name__ == '__main__':
    unittest.main()




