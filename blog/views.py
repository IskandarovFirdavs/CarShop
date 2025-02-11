from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Comment, Rating

@login_required
def post_details(request, id):
    post = get_object_or_404(Post, id=id)
    comments = post.comments.filter(approved=True).order_by('-pk')
    user_liked = request.user in post.likes.all()
    rating_range = range(1, 6)

    if request.method == 'POST':
        if 'like' in request.POST:
            if user_liked:
                post.likes.remove(request.user)
                messages.info(request, "Siz postni yoqtirishni bekor qildingiz.")
            else:
                post.likes.add(request.user)
                messages.success(request, "Siz postni yoqtirdingiz.")
            return redirect('blog:details', id=post.id)

        # Comment functionality
        if 'comment' in request.POST:
            comment_text = request.POST.get('comment')
            if comment_text:
                Comment.objects.create(post=post, user=request.user, text=comment_text)
                messages.success(request, "Izoh qo'shildi.")
            else:
                messages.error(request, "Izoh matni bo'sh bo'lishi mumkin emas.")
            return redirect('blog:details', id=post.id)

        if 'rating' in request.POST:
            rating_value = request.POST.get('rating')
            try:
                rating_value = int(rating_value)
                if 1 <= rating_value <= 5:
                    Rating.objects.update_or_create(
                        post=post,
                        user=request.user,
                        defaults={'value': rating_value}
                    )
                    messages.success(request, "Reyting muvaffaqiyatli qo'shildi.")
                else:
                    messages.error(request, "Reyting qiymati 1 dan 5 gacha bo'lishi kerak.")
            except ValueError:
                messages.error(request, "Noto'g'ri reyting qiymati.")
            return redirect('blog:details', id=post.id)

    context = {
        'post': post,
        'comments': comments,
        'user_liked': user_liked,
        'rating_range': rating_range,
    }
    return render(request, 'blog.html', context)

