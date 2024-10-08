from pprint import pprint

def introspection_info(obj):
    attrs = dir(obj)
    methods = [attr for attr in attrs if callable(getattr(obj, attr))]

    return {
        'type': type(obj).__name__,
        'attr': dir(obj),
        'methods': methods,
        'module': obj.__class__.__module__,
    }

number_info = introspection_info(42)
pprint(number_info)