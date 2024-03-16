from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# posts = [
#     {
#         'author': 'saud mukhair',
#         'title':  'Post 1 ',
#         'content': 'dont fight ! all anime are best peace! ',
#         'date_posted':'4 th feb 2024'
#     },
#     {
#         'author': 'naruto',
#         'title':  'Post 2',
#         'content': 'naruto is the best anime in entire history of anime  ',
#         'date_posted':'3 th feb 2024'
#     },
#     {
#         'author': 'asta',
#         'title':  'Post 3 ',
#         'content': 'black clover is best anime  ',
#         'date_posted':'2 nd feb 2024'
#     }, {
#         'author': 'zain mukhair',
#         'title':  'baby care shop ',
#         'content': 'here u will get all kind of diapers',
#         'date_posted':'4 th feb 2024'
#     }


# ]


def home(request):

    context = {
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title':'about'})