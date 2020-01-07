from agwui.FunctionEntrypoint import make_function_entrypoint
from agwui.FunctionDefinition import make_function_definition

def test_make_function_entrypoint():
    def f():
        return 10
    
    definition = make_function_definition(f)
    entrypoint = make_function_entrypoint(definition)

    assert entrypoint.path == "/f"
    assert entrypoint.schema_path == "/f/schema"
    assert entrypoint.function_definition is definition
        