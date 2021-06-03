from django.db import models
from accounts.models import CustomUser
from django.core.validators import MaxValueValidator, MinValueValidator

class Beer(models.Model):
    BEER_TYPE = [
        ('エール', 'エール'),
        ('ラガー', 'ラガー')
    ]

    beer_name = models.CharField(max_length=50, verbose_name = 'ビール名', unique=True)
    maker = models.CharField(max_length=100, verbose_name = '製造会社', blank=True, null=True)
    origin_place = models.CharField(max_length=100, verbose_name = '生産地', blank=True, null=True)
    alcohol_degree = models.FloatField(max_length=2, verbose_name='アルコール度数', blank=True, null=True)
    type = models.CharField(max_length=10, choices=BEER_TYPE, default='エール', verbose_name='種類', blank=True, null=True)
    price = models.IntegerField(verbose_name='値段', blank=True, null=True)
    capacity = models.IntegerField(verbose_name='内容量', blank=True, null=True)
    features = models.TextField(verbose_name='特徴', blank=True, null=True)
    url = models.URLField(verbose_name='公式サイト', blank=True, null=True)

    def __str__(self):
        return self.beer_name


class Favo(models.Model):
    beer = models.ForeignKey(Beer, verbose_name='ビール', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE)
    created_dt = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)

    def __str__(self):
        return 'お気に入り'


class Review(models.Model):
    beer = models.ForeignKey(Beer, verbose_name='ビール', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE)
    score = models.FloatField(verbose_name='総合評価', null=False, default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    taste_kire = models.FloatField(verbose_name='キレ', null=False, default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    taste_sannmi = models.FloatField(verbose_name='酸味', null=False, default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    taste_nigami = models.FloatField(verbose_name='苦味', null=False, default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    taste_amami = models.FloatField(verbose_name='甘味', null=False, default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    taste_koku = models.FloatField(verbose_name='コク', null=False, default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    content = models.TextField(verbose_name='コメント', blank=True, null=True)
    image1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    image2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    image3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    created_dt = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_dt = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    def __str__(self):
        return self.content


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE)
    review = models.ForeignKey(Review, verbose_name='レビュー', on_delete=models.CASCADE)
    comment = models.TextField(max_length=200, verbose_name = 'ビール名', unique=True)
    created_dt = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)

    def __str__(self):
        return self.comment