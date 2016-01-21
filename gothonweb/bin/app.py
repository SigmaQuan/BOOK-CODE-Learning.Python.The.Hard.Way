import web

render = web.template.render('/home/quan/Documents/Code/BOOK-CODE-Learning.Python.The.Hard.Way/gothonweb/templates/')


class index(object):
    def GET(self):
        greeting = "Hello Quan"
        return render.index(greeting=greeting)

if __name__ == "__main__":
    urls = (
        '/', 'index'
    )
    app = web.application(urls, globals())
    app.run()
