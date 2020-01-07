from agwui.function_injector import FunctionInjector
from agwui.function_extractor import FunctionExtractor


def test_function_injector(mocker):
    class SampleClass:
        def f():
            pass

        def g():
            pass

    obj = SampleClass()
    function_injector_handler_mock = mocker.MagicMock()
    function_extractor = FunctionExtractor()
    function_injector = FunctionInjector(
        function_extractor,
        [
            function_injector_handler_mock
        ]
    )

    function_injector.process(obj)

    assert function_injector_handler_mock.mock_calls == [
        mocker.call.process(obj.f),
        mocker.call.process(obj.g)
    ]
