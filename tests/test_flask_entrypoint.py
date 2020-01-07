from flask import Flask
from agwui import inject_class_app


def test_inject_class_app():
    class SampleClass:
        """
        SampleClass Object Description
        """

        def __init__(self):
            pass

        def f(self, n: int) -> int:
            return n * 10

    app = Flask(__name__)

    obj = SampleClass()

    inject_class_app(app, obj)
    test_app = app.test_client()

    assert test_app.get("/").status_code == 200
    assert test_app.get("/f").status_code == 200
    assert test_app.post("/f", data={"n": 10}).data == b"100"
    assert test_app.get("/f/schema").status_code == 200


def test_inject_class_multi_functions_app():
    class SampleClass:
        """
        SampleClass Object Description
        """

        def __init__(self):
            pass

        def f(self, n: int) -> int:
            return n * 10

        def g(self, s: str) -> str:
            return s + "a"

    app = Flask(__name__)

    obj = SampleClass()

    inject_class_app(app, obj)
    test_app = app.test_client()

    assert test_app.get("/f").status_code == 200
    assert test_app.get("/g").status_code == 200
