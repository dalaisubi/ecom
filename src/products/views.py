from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from carts.models import Cart
from .models import Product
# Create your views here.

class ProductFeatureListView(ListView):
	template_name = "product/product_list.html"

	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.all().featured()

class ProductFeatureDetailView(DetailView):
	template_name = "product/featured-detail.html"

	def get_queryset(self, *args, **kwargs):
		request = self.request
		pk = self.kwargs.get('pk')
		print(pk, request,'===')
		return Product.objects.all().featured()	

class ProductListView(ListView):
	model = Product
	template_name = "product/product_list.html"

	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	print(context)
	# 	return context

def product_list_view(request):
	queryset = Product.objects.all()

	context = {
		"object_list": queryset
	}	

	return render(request, "product/product_list.html", context)

class ProductDetailSlugView(DetailView):
	model = Product
	template_name = "product/product_detail.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailSlugView,self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context['cart'] = cart_obj
		return context

	def get_object(self, *args, **kwargs):
		request = self.request
		slug = self.kwargs.get('slug')
		#instance = get_object_or_404(Product, slug=slug, active=True)
		try:
			instance = Product.objects.get(slug=slug, active=True)
		except Product.DoesNotExist:
			raise Http404("Not found.")
		except Product.MultipleObjectsReturned:
			qs = Product.objects.filter(slug=slug, active=True)
			instance = qs.first()
		except:
			return Http404("Error")	
		return instance	

class ProductDetailView(DetailView):
	#model = Product
	template_name = "product/product_detail.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		print(context, '-------------')
		return context

	def get_object(self, *args, **kwargs):
		request = self.request
		pk = self.kwargs.get('pk')
		instance = Product.objects.get_by_id(pk)
		if instance is None:
			raise Http404("This product doesn't exist")

		return instance	

def product_detail_view(request, slug=None):
	#queryset = get_object_or_404(Product, pk=slug)
	# try:
	# 	queryset = Product.objects.get(pk=slug)
	# except Product.DoesNotExist:
	# 	print("No product here")
	# 	raise Http404("Product doesn't exist")	
	# except:
	# 	print("huh?")	
	instance = Product.objects.get_by_id(id = slug)
	print(instance,'get_by_id')

	if instance is None:
		raise Http404("Product doesn't exist")
	# qs = Product.objects.filter(pk=slug)
	# if qs.count() == 1:
	# 	queryset = qs.first()
	# else:
	# 	raise Http404("Product doesn't exist")	
	context = {
		"object": instance
	}	
	print(queryset, slug, context)
	return render(request, "product/product_detail.html", context)	