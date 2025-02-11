from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect
from product.models import CarModel, CommentModel
from django.contrib import messages


def home(request):
    products = CarModel.objects.order_by('-pk')[:3]
    rating_range = range(1, 6)
    search_query = request.GET.get('search', '')
    # def tags(request, tag_slug):
    #     tag = get_object_or_404(Tag, slag=tag_slug)


    if search_query:
        products = CarModel.objects.filter(name__icontains=search_query)

    if 'like' in request.GET:
        car_id = request.GET.get('like')
        car = CarModel.objects.get(id=car_id)
        car.likes += 1
        car.save()

    context = {
        'products': products,
        'search_query': search_query,
        'rating_range': rating_range,
    }
    return render(request, 'home.html', context)



@login_required()
def details(request, id):
    product = get_object_or_404(CarModel, id=id)
    comments = CommentModel.objects.filter(product=product)
    rating_range = range(1, 6)

    if request.method == "POST":
        comment_text = request.POST.get("comment")
        rating = request.POST.get('rating')
 
        if comment_text and rating:
            try:
                rating = int(rating)
                comment = CommentModel.objects.create(
                    product=product,
                    name=request.user.username,
                    comment=comment_text,
                    rating=rating,
                )
                return redirect('product:details', id=product.id)
            except ValueError:
                pass

    context = {
        'product': product,
        'comments': comments,
        'rating_range': rating_range,
    }
    return render(request, 'details.html', context)


