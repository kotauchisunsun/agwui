from agwui.FunctionDefinition import make_function_definition

def test_check_name():
    def f():
        pass

    fd = make_function_definition(f)
    assert fd.name == "f"

def test_check_description():
    def f():
        """
        description
        """
        pass
    
    fd = make_function_definition(f)
    assert fd.description == "description"

def test_check_return_type():
    def f() -> int:
        return 10

    fd = make_function_definition(f)
    assert fd.return_type == int

def test_check_argument_parameter():
    def f(n: int = 10):
        pass

    fd = make_function_definition(f)
    assert len(fd.parameters) == 1
    param = fd.parameters[0]
    assert param.name == "n"
    assert param.arg_type == int
    assert param.default == 10

def test_check_nodefault_argument_parameter():
    def f(n):
        pass

    fd = make_function_definition(f)
    assert len(fd.parameters) == 1
    param = fd.parameters[0]
    assert param.name == "n"
    assert param.default == None