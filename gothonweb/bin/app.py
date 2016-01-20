import web

urls = (
    '/', 'index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

greetings = "Hello World"


class index(object):
    def GET(self):
        return greeting
        # return render.index(greeting=greetings)


if __name__ == "__main__":
    app.run()
