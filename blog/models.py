from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()

    # 文章的创建时间和最后修改时间
    created_time = models.DateField()
    modified_time = models.DateField()

    # 文章的摘要，该字段允许为空
    excerpt = models.CharField(max_length=200, blank=True)

    # 文章的分类和标签
    # 分类使用的一对多的关系
    # 标签使用的是多对多的关系，同时标签字段可以为空
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    # 文章作者, Django自带用户类
    # 文章表使用外键关联用户类（一对多的关联关系）
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time']
