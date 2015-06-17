import imp
import sys

def find_and_load(module, path):
    file, pathname, description = imp.find_module(module, path)
    try:
        n = len(sys.path)
        sys.path += path
        return imp.load_module(module, file, pathname, description)
    finally:
        del sys.path[n:]
    
m = find_and_load('bar',['../b'])
print m.tweedledee() + m.tweedledum()
