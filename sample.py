from flask import Flask
from agwui import inject_class_app

class SampleClass:
    """
       SampleClass Object Description
    """

    def __init__(self):
        pass
    
    def f(self, n):
        return 3*n

    def g(self,n: int) -> int:
        return 2*n
    
    def h(self,s: str) -> str:
        return "hoge"+s

if __name__=="__main__":
    app = Flask(__name__)

    obj = SampleClass()

    inject_class_app(app, obj)
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)
