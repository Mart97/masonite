from masonite.controllers import Controller
from masonite.facades import Gate
from masonite.request import Request
from masonite.response import Response
from masonite.views import View

from app.models.Post import Post


class BlogController(Controller):
    def show(self, view: View):
        if not Gate.allows("create-post"):
            return Response.redirect("/")
        return view.render('blog')

    def store(self, request: Request):
        Post.create(
            title=request.input('title'),
            body=request.input('body'),
            author_id=request.user().id
        )
        return 'post created'
