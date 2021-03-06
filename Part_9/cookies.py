from bottle import route, run, request, response


@route('/')
def index():
	count = int(request.cookies.get('counter',0))
	count += 1
	response.set_cookie('counter',str(count))
	return 'You have visited the site: {} times!'.format(count)

run(host = 'localhost', port = 8080, debug = True)