import os

from random import choice
import tempfile

class DirDict:

    def __init__(self,path):
        self.path = path
        self.cur_path = os.path.join(tempfile.gettempdir(), self.path)
        os.makedirs(path)

    def __getitem__(self, key):

        try:
            with open(os.path.join(self.cur_path,key), 'r') as f:
                return f.read()
        except FileNotFoundError:
            raise KeyError

    def __setitem__(self, key, value):
        os.chdir(self.cur_path)

        with open(key, 'w') as f:
            f.write(str(value))


    def __delitem__(self, key):
        os.remove(os.path.join(self.cur_path,key))


    def __len__(self):
        count = 0
        print(os.getcwd())

        for _ in os.listdir(self.cur_path):
            count += 1
        return count

    def __repr__(self):
        d = {}

        for elem in os.listdir(os.getcwd()):
            if os.path.isfile(elem):
                with open(elem,'r') as f:
                    d[elem] = f.read()
            return d

    def __iter__(self):

        for elem in os.listdir(os.path.join(os.getcwd(),self.path)):
            with open(elem,'r') as f:
                yield f.read()

    def __contains__(self, item):

        if item in os.listdir(self.cur_path):
            return True
        else:
            return False

    def __eq__(self, other):
        if sorted(os.listdir(self.cur_path)) == sorted(os.listdir(os.path.join(os.getcwd(),other.path))):
            return True
        else:
            return False

    def __ne__(self, other):
        if sorted(os.listdir(self.cur_path)) != sorted(os.listdir(os.path.join(os.getcwd(),other.path))):
            return True
        else:
            return False

    def __sizeof__(self):
        size = 0
        for elem in os.listdir(os.getcwd()):
            size += os.path.getsize(elem)

        return size

    def __str__(self):
        dictionary = {}
        for elem in os.listdir(self.cur_path):
            with open(os.path.join(self.cur_path,elem), 'r') as f:
                dictionary[elem] = f.read()
        return str(dictionary)

    def clear(self):
        for elem in os.listdir(self.cur_path):
            os.remove(self.cur_path + '/' + elem)


    def copy(self):

        os.mkdir(self.path + '_copy')
        for elem in os.listdir(os.path.join(os.getcwd(),self.path)):
            with open(os.path.join(self.cur_path,elem), 'r') as f:
                data = f.read()
            with open(os.path.join(self.cur_path + '_copy',elem), 'w') as f:
                f.write(data)

    def get(self, k, d=None):
        if k in os.listdir(os.path.join(os.getcwd(),self.path)):
            with open(os.path.join(self.cur_path,k),'r') as f:
                return f.read()
        else:
            with open(os.path.join(self.cur_path,k),'w') as f:
                f.write(d)
                return d

    def items(self):
        items = []
        for elem in os.listdir(self.cur_path):
            with open(os.path.join(self.cur_path,elem), 'r') as f:
                items.append((elem,f.read()))

        return items


    def keys(self):
        keys = os.listdir(self.cur_path)

        return keys

    def pop(self, k, d=None):
        if k in os.listdir(self.cur_path):
            with open(os.path.join(self.cur_path,k),'r') as f:
                del self[k]

                return f.read()
        else:

            return d

    def popitem(self):
        k = choice(os.listdir(self.cur_path))
        with open(os.path.join(self.cur_path,k),'r') as f:
            del self[k]

            return k, f.read()

    def setdefault(self, k, d=''):
        if k in os.listdir(self.cur_path):

            with open(os.path.join(self.cur_path,k),'r') as f:
                return f.read()

        else:
            with open(os.path.join(self.cur_path,k),'w') as f:
                f.write(str(d))

                return k, d

    def update(self, *args):
        for elem in args:
            for k, v in elem.items():
                with open(os.path.join(self.cur_path,k), 'w') as f:
                    f.write(v)


    def values(self):
        values = []

        for elem in os.listdir(self.cur_path):
            with open(os.path.join(self.cur_path,elem), 'r') as f:
                values.append(f.read())
        return values





