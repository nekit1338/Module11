from pprint import pprint


def introspection_info(obj: object):
    attributes = dir(obj)
    methods = [attr for attr in attributes if callable(getattr(obj, attr))]
    attributes = [attr for attr in attributes if attr not in methods]
    info = {
        'type': type(obj),
        'attributes': attributes,
        'methods': methods,
        'module': obj.__module__,
        'isCallable': callable(obj)
    }
    if isinstance(obj, object):
        info['Base class'] = obj.__class__.__bases__
    return info


class A:

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def method(self):
        print(self.a)

    def method_01(self):
        print(self.b)


if __name__ == '__main__':

    obj = A(10, 20)
    number_info = introspection_info(obj)
    pprint(number_info)
