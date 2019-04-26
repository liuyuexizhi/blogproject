import markdown
from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from comments.forms import CommentForm


# Create your views here.
def index(request):
    post_list = Post.objects.all().order_by('-created_time')

    return render(request, 'blog/index.html', context={
        'post_list': post_list
    })


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    post.body = markdown.markdown(
        post.body,
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ]
    )

    form = CommentForm()
    comment_list = post.comment_set.all()

    context = {
        'post': post,
        'form': form,
        'comment_list': comment_list
    }

    '''
    注意这里我们用到了从 django.shortcuts 模块导入的 get_object_or_404 方法，
    其作用就是当传入的 pk 对应的 Post 在数据库存在时，就返回对应的 post，
    如果不存在，就给用户返回一个 404 错误，表明用户请求的文章不存在。
    '''
    return render(request, 'blog/detail.html', context=context)


def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    )
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request, 'blog/index.html', context={'post_list': post_list})
