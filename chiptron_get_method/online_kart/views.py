from django.shortcuts import redirect, render
from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import *
from .utils import *
import logging
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
import json


# def home(request):
#     item_codes = Sale.objects.values_list('item_code', flat=True).distinct()
#     item_code_form = ItemCodeForm(request.GET)

#     if item_code_form.is_valid():
#         selected_item_code = item_code_form.cleaned_data.get('item_code', '')
#         start_date = item_code_form.cleaned_data.get('start_date')
#         start_time = item_code_form.cleaned_data.get('start_time')
#         end_date = item_code_form.cleaned_data.get('end_date')
#         end_time = item_code_form.cleaned_data.get('end_time')

#         start_datetime = None
#         end_datetime = None

#         if start_date and start_time:
#             start_datetime = datetime.combine(start_date, start_time)
#             start_datetime = make_aware(start_datetime)

#         if end_date and end_time:
#             end_datetime = datetime.combine(end_date, end_time)
#             end_datetime = make_aware(end_datetime)

#         chart_all_items = get_plot(item_codes, start_datetime, end_datetime)

#         chart_selected_item = None
#         if selected_item_code and start_datetime and end_datetime:
#             chart_selected_item = get_date_plot(selected_item_code, start_date, end_date, start_time, end_time)
#     else:
#         chart_all_items = None
#         chart_selected_item = None

#     return render(request, "shop/index.html", {
#         'chart_all_items': chart_all_items,
#         'chart_selected_item': chart_selected_item,
#         'item_codes': item_codes,
#         'item_code_form': item_code_form,
#     })

# def home(request):
#     item_codes = Sale.objects.values_list('item_code', flat=True).distinct()

#     current_datetime = datetime.now()
#     item_code_form = ItemCodeForm(request.GET or None)

#     chart_all_items = None
#     chart_selected_item = None

#     if item_code_form.is_valid():
#         selected_item_code = item_code_form.cleaned_data.get('item_code', '')
#         start_date = item_code_form.cleaned_data.get('start_date')
#         start_time = item_code_form.cleaned_data.get('start_time')
#         end_date = item_code_form.cleaned_data.get('end_date')
#         end_time = item_code_form.cleaned_data.get('end_time')

#         start_datetime = make_aware(datetime.combine(start_date, start_time))
#         end_datetime = make_aware(datetime.combine(end_date, end_time))

#         chart_all_items = get_plot(item_codes, start_datetime, end_datetime)

#         if selected_item_code and start_datetime and end_datetime:
#             chart_selected_item = get_date_plot(selected_item_code, start_date, end_date, start_time, end_time)

#     return render(request, "shop/index.html", {
#         'chart_all_items': chart_all_items,
#         'chart_selected_item': chart_selected_item,
#         'item_codes': item_codes,
#         'item_code_form': item_code_form,
#     })



def home(request):
    item_codes = Sale.objects.values_list('item_code', flat=True).distinct()

    current_datetime = datetime.now()
    item_code_form = ItemCodeForm(request.GET or None)

    chart_all_items = None
    chart_selected_item = None

    if item_code_form.is_valid():
        selected_item_code = item_code_form.cleaned_data.get('item_code', '')
        start_date = item_code_form.cleaned_data.get('start_date')
        start_time = item_code_form.cleaned_data.get('start_time')
        end_date = item_code_form.cleaned_data.get('end_date')
        end_time = item_code_form.cleaned_data.get('end_time')

        start_datetime = make_aware(datetime.combine(start_date, start_time))
        end_datetime = make_aware(datetime.combine(end_date, end_time))

        chart_all_items = get_plot(item_codes, start_datetime, end_datetime)

        if selected_item_code and start_datetime and end_datetime:
            chart_selected_item = get_date_plot(selected_item_code, start_date, end_date, start_time, end_time)

    return render(request, "shop/index.html", {
        'chart_all_items': chart_all_items,
        'chart_selected_item': chart_selected_item,
        'item_codes': item_codes,
        'item_code_form': item_code_form,
    })

def reg(request):
  form=CustomUserForm()
  if request.method=='POST':
    form=CustomUserForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request,"Registration Success You can Login Now..!")
      return redirect('/log_in')
  return render(request,"shop/register.html",{'form':form})
def log_out(request):
   if request.user.is_authenticated:
    logout(request)
    messages.success(request,"Logged out Successfully")
   return redirect("/")
def log_in(request):
    if request.method=='POST':
      name=request.POST.get('username')
      pwd=request.POST.get('password')
      user=authenticate(request,username=name,password=pwd)
      if user is not None:
        login(request,user)
        messages.success(request,"Logged in Successfully")
        return redirect("/")
      else:
        messages.error(request,"Invalid User Name or Password")
        return redirect("log_in")
    return render(request,"shop/login.html")




from django.shortcuts import render, redirect
from .forms import CategoryForm

def add_category(request):
    if request.method == 'POST':
        form = Category(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the tree view
    else:
        form = CategoryForm()
    return render(request, 'catagory1.html', {'form': form})


from django.http import JsonResponse
def get_tree(request):
    root_nodes = Category.objects.filter(parent_id=0)
    tree_data = build_tree(root_nodes)
    return JsonResponse(tree_data, safe=False)
def build_tree(nodes):
    tree = []
    for node in nodes:
        children = Category.objects.filter(parent_id=node.id)
        subtree = {
            'id': node.id,
            'name': node.name,  # Add the 'name' from the database
             # Add the 'menu_description' from the database
            'children': build_tree(children)
        }
        tree.append(subtree)
    return tree
def catagory(request):
    return render(request, 'shop/catagory.html')



from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator,  EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from datetime import datetime
@login_required(login_url='accounts/login')


def ShowAllProducts(request):
    
    category = request.GET.get('category')

    if category == None:
        products = Product.objects.order_by('-price').filter(is_published=True)
        page_num = request.GET.get("page")
        paginator = Paginator(products,8)
        try:
            products = paginator.page(page_num)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)             
    else:
        products = Product.objects.filter(category__name=category)
       
    
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories
    }

    return render(request, 'shop/showProducts.html', context)



@login_required(login_url='showProducts')
def productDetail(request, pk):
    eachProduct = Product.objects.get(id=pk)

    num_comments = Comment.objects.filter(product=eachProduct).count()

    context = {
        'eachProduct': eachProduct,
        'num_comments': num_comments,
    }

    return render(request, 'shop/productDetail.html', context)



@login_required(login_url='showProducts')
def addProduct(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('showProducts')
    else:
        form = ProductForm()

    context = {
        "form":form
    }

    return render(request, 'shop/addProduct.html', context)


@login_required(login_url='showProducts')
def updateProduct(request,pk):
    product = Product.objects.get(id=pk)

    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('showProducts')

    context = {
        "form":form
    }

    return render(request, 'shop/updateProduct.html', context)



@login_required(login_url='showProducts')
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('showProducts')



@login_required(login_url='showProducts')
def searchBar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            products = Product.objects.filter(name__icontains=query) 
            return render(request, 'shop/searchbar.html', {'products':products})
        else:
            print("No information to show")
            return render(request, 'shop/searchbar.html', {})

@login_required(login_url='showProducts')
def add_comment(request, pk):
    eachProduct = Product.objects.get(id=pk)

    form = CommentForm(instance=eachProduct)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=eachProduct)
        if form.is_valid():
            name = request.user.username
            body = form.cleaned_data['comment_body']
            c = Comment(product=eachProduct, commenter_name=name, comment_body=body, date_added=datetime.now())
            c.save()
            return redirect('showProducts')
        else:
            print('form is invalid')    
    else:
        form = CommentForm()    


    context = {
        'form': form
    }

    return render(request, 'shop/add_comment.html', context)


def delete_comment(request, pk):
    comment = Comment.objects.filter(product=pk).last()
    product_id = comment.product.id
    comment.delete()
    return redirect(reverse('product', args=[product_id]))







@login_required(login_url='showProducts')

def cart(request):
  if request.user.is_authenticated:
    cart=Cart.objects.filter(user=request.user)
    return render(request,"shop/cart.html",{"cart":cart})
  else:
    return redirect("/")
  



@login_required(login_url='showProducts')
def add_to_cart(request):
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
    if request.user.is_authenticated:
      data=json.load(request)
      product_qty=data['product_qty']
      product_id=data['pid']
      #print(request.user.id)
      product_status=Product.objects.get(id=product_id)
      if product_status:
        if Cart.objects.filter(user=request.user.id,product_id=product_id):
          return JsonResponse({'status':'Product Already in Cart'}, status=200)
        else:
          if product_status.quantity>=product_qty:
            Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
            return JsonResponse({'status':'Product Added to Cart'}, status=200)
          else:
            return JsonResponse({'status':'Product Stock Not Available'}, status=200)
    else:
      return JsonResponse({'status':'Login to Add Cart'}, status=200)
   else:
    return JsonResponse({'status':'Invalid Access'}, status=200)

@login_required(login_url='showProducts')

def remove_cart(request,cid):
  cartitem=Cart.objects.get(id=cid)
  cartitem.delete()
  return redirect("/cart")
 
