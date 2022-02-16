from django.shortcuts import render
from django.http import HttpResponse
from  django.template import  loader,RequestContext
from  booktest.models import BookInfo
# Create your views here.
def index(request):
    # #获取模板
    # temmplate=loader.get_template('index.html')
    # #定义上线文
    # context=RequestContext(request,{'title':'图书列表','list':range(10)})
    # #渲染模板
    # return HttpResponse(temmplate.render(context))

    # context = RequestContext(request, {'title': '图书列表', 'list': range(10)})
    # return  render(request,'index.html',context)
    booklist=BookInfo.objects.all()
    return  render(request,'index.html',{'booklist':booklist})

def detail(request,bid):
    book=BookInfo.objects.get(id=int(bid))
    heros=book.heroinfo_set.all()
    return  render(request,'detail.html',{'book':book,'heros':heros})
