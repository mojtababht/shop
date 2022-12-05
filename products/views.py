from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.contrib import messages


def search(req,search):
    if req.method == "POST":
        if req.POST.get('search') != None:
            if req.POST.get('search') !='':
                return redirect('/search/' + req.POST.get('search'))
    categories = []
    product = []
    item=search
    for x in Product.objects.all():
        if (item.capitalize() or item.lower() or item.title() or item.upper()) in x.title:
            product.append(x)
    for x in Category.objects.all():
        if item in x.title:
            categories.append(x)
    if categories==[] and product==[] :
        return render(req,'products/searchNotFound.html',{'Sproduct':product,'Scategories':categories})
    return render(req,'products/search.html',{'Sproduct':product,'Scategories':categories})



def Home(req):
    if req.method == "POST":
        if req.POST.get('search') != None:
            if req.POST.get('search') != '':
                return redirect('/search/' + req.POST.get('search'))

    product=Product.objects.filter(is_top=True)


    return render(req ,'products/home.html',{'product':product})

def productsView(req):
    if req.method == "POST":
        if req.POST.get('search') != None:
            if req.POST.get('search') != '':
                return redirect('/search/' + req.POST.get('search'))
    product=Product.objects.all()
    return render(req,'products/products.html',{'product':product})

def productDetile(req,id):
    if req.method == "POST":
        if req.POST.get('search') != None:
            if req.POST.get('search') != '':
                return redirect('/search/' + req.POST.get('search'))
    product=get_object_or_404(Product,id=id)
    product=Product.objects.get(id=id)
    number=0
    if req.user.is_authenticated:
        cart = Cart.objects.get(user=req.user)
        cartitem = CartItem(cart=cart, product=product)
        item = cart.cartitem_set.filter(product=product)
        number= len(item)
    if req.method=='POST':
        cartitem.save()






        return redirect("/products/"+str(id))


    return render(req,'products/productdetile.html',{"product" :product ,'number':number } )

def categoryView(req):
    if req.method == "POST":
        if req.POST.get('search') != None:
            if req.POST.get('search') != '':
                return redirect('/search/' + req.POST.get('search'))
    categories=Category.objects.all()
    return render(req,'products/category.html',{'categories':categories})

def categoryDetile(req,title):
    if req.method == "POST":
        if req.POST.get('search') != None:
            if req.POST.get('search') != '':
                return redirect('/search/' + req.POST.get('search'))
    category=get_object_or_404(Category,title=title)
    category=Category.objects.get(title=title)
    subcat=Category.objects.filter(parent=category)
    products=Product.objects.filter(categories=category)
    return render(req,'products/catrgorydetile.html',{'category':category,"products":products,'subcat':subcat})


def cartDetile(req):
    if req.method == "POST":
        if req.POST.get('search') != None:
            if req.POST.get('search') != '':
                return redirect('/search/' + req.POST.get('search'))
    cart=Cart.objects.get(user=req.user)
    cartitem=CartItem.objects.filter(cart=cart)
    if req.method=='POST':
        if not('pay' in req.POST.keys()):
            dict1={}
            dict1=dict(req.POST)
            list1=list(dict1.keys())
            delitem=CartItem.objects.get(id=list1[1])
            if delitem != None:
                delitem.delete()
                return redirect('/cartdetile/')

    return render(req,'products/cartdetile.html',{'cart':cart,'cartitem':cartitem})


def orderRegister(req):
    cart = Cart.objects.get(user=req.user)
    price=0
    for x in cart.cartitem_set.all():
        price=price + x.product.price
    if req.method == "POST":
        if req.POST.get('search') != None:
            if req.POST.get('search') != '':
                return redirect('/search/' + req.POST.get('search'))

    if req.method=='POST':
        if req.POST.get('address')!= None:
            if req.POST.get('address') != '':
                order=Order.objects.create(user=req.user,address=req.POST.get('address'))
                order.save()
                for p in cart.cartitem_set.all():
                    orderitem=OrderItem.objects.create(order=order,product=p.product)
                    orderitem.save()
                cart.delete()
                cart=Cart.objects.create(user=req.user)
                return redirect('/orderreceived')
            else:
                messages.info(req,'fill in the address field')
                return redirect('/orderregister')
    return render(req,'products/orderregister.html',{'price':price})

def orderReceived(req):
    if req.method == "POST":
        if req.POST.get('search') != None:
            if req.POST.get('search') != '':
                return redirect('/search/' + req.POST.get('search'))
    return render(req,'products/orderreceived.html',{})


