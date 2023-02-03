import os
import importlib

path = os.listdir(os.path.dirname(os.path.abspath(__file__)))

views = [i for i in path if i.endswith('.py') and i != '__init__.py']

for view in views:
    importlib.import_module(os.path.dirname(os.path.realpath(__file__)).split('/')[-1] + "." + view[:-3])
    print('App imported %s' % view)
# import products.urls
