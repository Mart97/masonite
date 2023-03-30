from masonite.authentication import Auth
from masonite.routes import Route

ROUTES = [
    Route.get('/', 'WelcomeController@show').name('welcome'),
    # Blog Routes
    Route.get('/blog', 'BlogController@show'),
    Route.post('/blog/create', 'BlogController@store'),
    # Post Routes
    Route.get('/posts', 'PostController@show'),
    Route.get('/post/@slug', 'PostController@single'),
    Route.get('/post/@id/delete', 'PostController@delete'),
    Route.get('/post/@id/update', 'PostController@update'),
    Route.post('/post/@id/update', 'PostController@store')
]

ROUTES += Auth.routes()
