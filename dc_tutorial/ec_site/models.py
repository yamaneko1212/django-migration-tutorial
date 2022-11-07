from django.db import models


class Customer(models.Model):
    name = models.CharField('氏名', max_length=32)
    email = models.EmailField('メールアドレス')
    postal_code = models.CharField('郵便番号', max_length=8)
    address = models.CharField('住所', max_length=128)

    class Meta:
        verbose_name = '顧客'
        verbose_name_plural = verbose_name
