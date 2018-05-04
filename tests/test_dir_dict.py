import unittest
import os
import tempfile

from dir_dict import DirDict

class DirDictTestCase(unittest.TestCase):
    tmpdirname = tempfile.TemporaryDirectory()


    def test_make_dict(self):
        tmpdirname = tempfile.TemporaryDirectory()
        d = DirDict(os.path.join(str(tmpdirname),'dict/storage'))
        d['lang'] = 'Python'
        self.assertEqual('Python',d['lang'])
        tmpdirname.cleanup()

    def test_del(self):
        tmpdirname = tempfile.TemporaryDirectory()
        d = DirDict(os.path.join(str(tmpdirname), 'dict/storage'))
        d['lang'] = 'Python'
        del d['lang']
        self.assertEqual(0,len(d))
        tmpdirname.cleanup()

    def test_keys(self):
        tmpdirname = tempfile.TemporaryDirectory()
        d = DirDict(os.path.join(str(tmpdirname), 'dict/storage'))
        d['lang'] = 'Python'
        d['lib'] = 'unittest'
        self.assertEqual(['lang','lib'], d.keys())
        tmpdirname.cleanup()

    def test_values(self):
        tmpdirname = tempfile.TemporaryDirectory()
        d = DirDict(os.path.join(str(tmpdirname), 'dict/storage'))
        d['lang'] = 'Python'
        d['lib'] = 'unittest'
        self.assertEqual(['Python','unittest'], d.values())
        tmpdirname.cleanup()

    def test_items(self):
        tmpdirname = tempfile.TemporaryDirectory()
        d = DirDict(os.path.join(str(tmpdirname), 'dict/storage'))
        d['lang'] = 'Python'
        d['lib'] = 'unittest'
        self.assertEqual([('lang','Python'),('lib','unittest')], d.items())
        tmpdirname.cleanup()


if __name__ == '__main__':
    unittest.main()




