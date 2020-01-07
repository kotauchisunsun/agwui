from agwui.class_handler import ClassHandler
from agwui.class_injector import ClassInjector

def test_class_inject(mocker):
    obj = mocker.MagicMock()

    #handlerをモックで定義する
    class_injector_handler_mock = mocker.MagicMock()

    #class_injectorにhandlerを登録する
    class_injector = ClassInjector([
        class_injector_handler_mock
    ])

    #processする
    class_injector.process(obj)

    #handlerが呼び出されたことを検証する
    assert class_injector_handler_mock.mock_calls == [mocker.call.process(obj)]
