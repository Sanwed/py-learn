import inspect
from pprint import pprint

def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    obj_module = obj.__module__

    return {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module
    }

class MyTestClass:
    def __init__(self):
        self.attr1 = 'value1'
        self.attr2 = 'value2'

    def method1(self):
        return 'method1 called'

    def method2(self):
        return 'method2 called'

number_info = introspection_info(MyTestClass())
pprint(number_info)
