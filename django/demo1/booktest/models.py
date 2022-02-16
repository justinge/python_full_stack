from django.db import models

# Create your models here.
class BookInfo(models.Model):
    btitle=models.CharField(max_length=30)
    bpub_date=models.DateField()
    def __str__(self):
        return self.btitle
class HeroInfo(models.Model):
    hname=models.CharField(max_length=30)
    hcomment=models.CharField(max_length=30)
    hbook=models.ForeignKey('BookInfo')#一对多在多的一方定义
    def __str__(self):
        return self.hname
