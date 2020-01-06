from flask import Flask
from agwui import inject_class_app
from agwui.ExtraType import FileType, ImageType

class SampleClass:
    """
       SampleClass Object Description
    """

    def __init__(self):
        pass
    
    def f(self, f: FileType) -> FileType:
        return FileType(f.file_obj)

    def g(self, image: ImageType) -> ImageType:
        return ImageType(image.file_obj)
    
    def h(self,s: str) -> str:
        return "hoge"+s

if __name__=="__main__":
    app = Flask(__name__)

    obj = SampleClass()

    inject_class_app(app, obj)
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)
