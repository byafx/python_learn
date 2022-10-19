# from selenium import webdriver
# browser = webdriver.PhantomJS(executable_path=r"D:\Python_PaCo\phantomjs-2.1.1-windows\bin\phantomjs.exe")
# browser.get('https://www.baidu.com')
# print(browser.current_url)

# from bs4 import BeautifulSoup
# soup = BeautifulSoup('<p>Hello</p>', 'lxml')
# print(soup.p.string)

# import tesserocr
# from PIL import Image
# image = Image.open(r'D:\Python_PaCo\image\test1.png')
# print(tesserocr.image_to_text(image))
#
# print(tesserocr.file_to_text(r'D:\Python_PaCo\image\test1.png'))

# from flask import Flask
# app = Flask(__name__)
#
# @app.route("/")
# def hello():
#     return "hello world!"
#
# if __name__ == "__main__":
#     app.run()

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello,world")

def make_app():
    return tornado.web.Application([(r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()