import inspect
import typing
from functools import wraps
fn_s = """
def magic_func {0}:
    {1}
                """

def type_check_fast(fn):
    sig = inspect.signature(fn)
    annotation = typing.get_type_hints(fn)
    return_type = annotation.pop('return',None)
    if annotation:
        assert_str = 'assert ' + ' and '.join(["isinstance({k},{v})".format(k=k,v=v.__name__) for k,v in annotation.items()])
        exec(fn_s.format(sig,assert_str))
        func = locals()['magic_func']
    @wraps(fn)
    def deced(*args,**kwargs):
        if annotation:
            func(*args,**kwargs)
        return_value = fn(*args,**kwargs)
        if return_type:
            assert isinstance(return_value,return_type)
        return return_value
    return deced

def auto_dec(name,dic_locals):
    for k,v in dic_locals.items():
        if hasattr(v,'__module__') and v.__module__ == name and inspect.isfunction(v):
            dic_locals[k] = type_check_fast(v)