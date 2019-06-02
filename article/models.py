from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation

from course.models import Course
from comments.models import Comment

from taggit.managers import TaggableManager
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

import traceback



# Create your models here.

class ArticlesColumn(models.Model):
    """
    article栏目
    """
    title = models.CharField(max_length=100, blank=True, verbose_name='标题')
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = '栏目'

    def __str__(self):
        return self.title


class ArticlesPost(models.Model):
    """
    博客文章
    """
    author = models.ForeignKey(
        User,
        related_name='article',
        on_delete=models.CASCADE,
        verbose_name='作者',
    )

    comments = GenericRelation(Comment)

    column = models.ForeignKey(
        ArticlesColumn,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='column',
        verbose_name='栏目',
    )

    title = models.CharField(max_length=200, verbose_name='标题')

    # 教程中的标题, 若不填则自动填写
    course_title = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name='课程标题',
    )

    # 教程外键
    course = models.ForeignKey(
        Course,
        related_name='article',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name='教程',
    )

    # 博文在教程中的序号，用于给博文排序
    course_sequence = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name='教程序号',
    )

    # taggit
    tags = TaggableManager(blank=True, verbose_name='标签')

    body = models.TextField(verbose_name='正文')
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    total_views = models.PositiveIntegerField(default=0, verbose_name='浏览量')

    # 缩略图
    avatar_thumbnail = ProcessedImageField(
        upload_to='image/article/%Y%m%d',
        processors=[ResizeToFit(width=500)],
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True,
        verbose_name='标题图',
    )

    url = models.URLField(blank=True, verbose_name='标题图url')

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        重写save(), 自动填写教程序号
        """
        try:
            if not self.course_title:
                self.course_title = self.title

        #         # 跳过更新日期
        #         # if not kwargs.pop('skip_updated', False):
        #         #     self.updated = timezone.now()
            super().save(*args, **kwargs)
        except BaseException as e:
            print('SaveError')
            traceback.print_exc()

    # 获取文章地址
    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.id])

    # 获取文章api地址
    def get_api_url(self):
        return reverse('api_article:detail', args=[self.id])

    # 统计浏览量
    def increase_views(self):
        try:
            self.total_views += 1
            self.save(update_fields=['total_views'])
            # self.save()
        except BaseException as e:
            print('ArticlesPostModelIncreseViewsError3')
            traceback.print_exc()
