from django.shortcuts import redirect, render, get_object_or_404
from .models import Product
from .forms import ProductForm, RawProductForm

# view list products
def product_list_view(request):
    # obj = Product.objects.get(id=id)
    queryset = Product.objects.all()
    print(queryset)
    context = {"object_list": queryset}
    return render(request, "products/product.html", context)


# view product
def dynamic_lookup_view(request, id):
    # obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    context = {"object": obj}
    return render(request, "products/product_detail.html", context)


# delete product
def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("../../")
    context = {"object": obj}
    return render(request, "products/product_delete.html", context)


# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#     context = {"form": my_form}
#     return render(request, "products/product_create.html", context)


# Django form create product
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {"form": form}
    return render(request, "products/product_create.html", context)


# Pure hdml
# def product_create_view(request):
#     print(request.GET)
#     print(request.POST)
#     if request.method == "POST":
#         my_new_title = request.POST.get("title")
#         print(my_new_title)
#     context = {}
#     return render(request, "products/product_create.html", context)
