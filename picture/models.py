# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(verbose_name=u"名称", null=False, blank=False, max_length=32, unique=True, db_index=True)
    
    class Meta:
        db_table = "category"
        verbose_name = u'分类'
        verbose_name_plural = u'分类'


class CP(models.Model):
    name = models.CharField(verbose_name=u"名称", null=False, blank=False, max_length=32, unique=True, db_index=True)
    
    class Meta:
        db_table = "cp"
        verbose_name = u'cp'
        verbose_name_plural = u'cp'


class Tag(models.Model):
    name = models.CharField(verbose_name=u"名称", null=False, blank=False, max_length=32, unique=True, db_index=True)
    
    class Meta:
        db_table = "tag"
        verbose_name = u'标签'
        verbose_name_plural = u'标签'

class Media(models.Model):
    name = models.CharField(verbose_name=u"名称", null=False, blank=False, max_length=32, unique=True, db_index=True)
    
    class Meta:
        db_table = "media"
        verbose_name = u'media'
        verbose_name_plural = u'media'


class Picture(models.Model):
    title = models.CharField(verbose_name=u"标题", null=False, blank=True, max_length=128, db_index=True, default="")
    desc = models.TextField(verbose_name=u"描述", null=False, blank=True, default="")
    creator = models.ForeignKey(User, related_name='+', verbose_name=u"最近操作者", null=True, blank=True)
    create_time = models.DateTimeField(verbose_name=u"入库时间", null=False, blank=False, auto_now_add=True, db_index=True)
    update_time = models.DateTimeField(verbose_name=u"更新时间", null=False, blank=False, auto_now=True, db_index=True)
    cp = models.ForeignKey(CP, related_name="+", verbose_name=u"CP", null=True, blank=True)
    meida = models.ForeignKey(Media, related_name="+", verbose_name=u"品牌", null=True, blank=True)


    category_set = models.ManyToManyField(Category, related_name="album_category_set+", verbose_name=u"分类",
                                          null=True, blank=True)

    tag_set = models.ManyToManyField(Tag, related_name="album_tag_set+",
                                     verbose_name=u"标签", null=True, blank=True)
    image_url = models.CharField(verbose_name=u"图片地址", default="", max_length=1024)

    class Meta:
        db_table = "picture"
        verbose_name = u'图片'
        verbose_name_plural = u'图片'

