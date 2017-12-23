def foo(fn):
    def wrap():
        return ">{}".format(fn())
    return wrap
@foo
def something():
    return "rasult"
print(something())