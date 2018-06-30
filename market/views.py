from django.shortcuts import render, redirect, reverse
from .models import *
from index.models import User

from django.contrib import messages
from STC_NWSUAF.tools import login_required

# Create your views here.

def index_views(request):
    if request.method == 'GET':

        return redirect(reverse('goods_index'))
#付费文档页面
def docs_views(request):
    if request.method == 'GET':
        return render(request,'docs_index.html',locals())
#二手商品页面

def goods_views(request):
    if request.method == 'GET':
        goods = Good.objects.all().order_by('-create_time') 
        page_now = request.GET.get('page')
        if not page_now:
            page_now = 1
        page_now = int(page_now)
        per_page = 4
        page_sum = len(goods)//per_page+1
        if page_sum > 6:
            page_sum = len(goods)//per_page
        else:
            page_sum = len(goods)//per_page+1
        start_page = (page_now-1)*per_page
        next_page = page_now + 1
        pre_page = page_now - 1
        goods = goods[start_page:start_page+per_page]
        show_sum = page_sum//6+1 
        lis = []
        for i in range(1,show_sum+1):
            lis.append(i)
        for i in lis:
            if page_now in range(i*6-5,i*6+1):
                    ranges = range(i*6-5,i*6+1)
        if page_sum in ranges:
                    ranges = range(i*6-5,page_sum+1)
        print(page_sum)
        return render(request,'goods_index.html',locals())
#商品详情页面
def good_detail_views(request,good_id):
    if request.method=='GET':
        good = Good.objects.get(id=good_id)
        return render(request,'good_detail.html',locals())

#确认购买页面
@login_required
def ordering_views(request, good_id):
    good = Good.objects.get(id=good_id)
    return render(request, 'ordering.html', locals())
#创建订单视图
@login_required
def new_order_views(request, good_id):
    if request.method == 'POST':
        good = Good.objects.get(id=good_id)
        confirm = request.POST.get('confirm-buy', '')
        if confirm == '':
            messages.warning(request, '你未确认交易信息')
            return render(request, 'ordering.html', locals())
        else:
            good = Good.objects.get(id=good_id)
            user = User.objects.get(username=request.session['username'])
            new_order = Order(status=0, creator=user, good=good)
            new_order.save()
            return redirect(reverse('paying', args=(new_order.id,)))

#支付页面
@login_required
def paying_views(request, order_id):
    if request.method == 'GET':
        order = Order.objects.get(id=order_id)
        good = order.good

        tmessages = TradeMessage.objects.filter(order=order).order_by('create_time')
        return render(request, 'paying.html', locals())
    return redirect('/')


#创建新商品页面
@login_required
def add_good_views(request):
    if request.method == 'GET':
        return render(request,'new_good.html',locals())

def order_views(request,orderstate):
    if request.method == 'GET':
        order_list = Order.objects.all().order_by('-create_time')
        #good = order_list.good__set.all()
        return render(request,'order_view.html',locals())
def order_finished_views(request,orderstate):
    if request.method == 'GET':
        return render(request,'order_finish.html',locals())
def order_complaint_views(request,orderstate):
    if request.method == 'GET':
        return render(request,'order_complaint.html',locals())
def order_cancel_views(request,orderstate):
    if request.method == 'GET':
        return render(request,'order_cancel.html',locals())
def order_detail_views(request,goodname):
    if request.method == 'GET':
        return render(request,'order_detail.html',locals())
def complaint_views(request,orderid):
    if request.method == 'GET':
        return render(request,'complaint.html',locals())
def add_tmessage_views(request, order_id):
    if request.method == 'POST':
        content = request.POST.get('content', '')
        order = Order.objects.get(id=order_id)
        good = order.good
        user = User.objects.get(username=request.session['username'])
        buyer = order.creator
        seller = good.creator
        if not content == '':
            if user.id == buyer.id:
                message = TradeMessage(sender=user, receiver=seller, order=order, content=content)
            else:
                message = TradeMessage(sender=user, receiver=buyer, order=order, content=content)

            message.save()

        messages.success(request,'已发送')
        return render(request, 'paying.html', locals())

