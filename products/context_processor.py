from products.models import Category


def extras(request):
    categories = Category.objects.all()
    return {'categories': categories}
