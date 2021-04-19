
from .models import Supply,ProductAttribute
from django.db.models import Min,Max
def get_filters(request):
	cartype=Supply.objects.distinct().values('cartypes__title','cartypes__id')
	catagories=ProductAttribute.objects.distinct().values('category__title','category__id')
	transmission=ProductAttribute.objects.distinct().values('transmission__title','transmission__id')
	minMaxPrice=ProductAttribute.objects.aggregate(Min('price'),Max('price'))
	data={
		'cats':cartype,
		'minMaxPrice':minMaxPrice,
		'catagory':catagories,
		'transmission':transmission
	}
	return data