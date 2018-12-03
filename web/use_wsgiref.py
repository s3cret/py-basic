from wsgiref.simple_server import make_server

# write your own application (func)
def app(environment, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['<h1>Hello, web!</h1>'.encode('utf-8')]

def app1(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    print(environ)
    return [body.encode('utf-8')]


if __name__ == '__main__':
    host = 'localhost'
    port = 8080
    httpd = make_server(host, port, app1)
    print('Serving HTTP on port %d' % port )
    httpd.serve_forever()

