import imp

def find_and_load(module, path):
    file, pathname, description = imp.find_module(module, path)
    return imp.load_module(module, file, pathname, description)
    
m = find_and_load('bar',['../b'])
