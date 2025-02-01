from django.db import models


class CarModel(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    color = models.CharField(max_length=30)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    location = models.FloatField()
    fuel = models.CharField(max_length=100)
    acceleration = models.FloatField()
    transmission = models.CharField(max_length=100)
    discount = models.IntegerField(default=0, null=True, blank=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def get_price(self):
        if self.discount:
            return self.price - self.price / 100 * self.discount
        return self.price

    def get_average_rating(self):
        comments = self.comments.all()
        total_rating = sum([comment.rating for comment in comments])
        if comments.count() > 0:
            return total_rating / comments.count()
        return 0



class CommentModel(models.Model):
    product = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.PositiveIntegerField(
        default=5,
        choices=[(i, f'{i} Star{"s" if i > 1 else ""}') for i in range(1, 6)],
        help_text='Rating between 1 (worst) and 5 (best)'
    )

    def __str__(self):
        return f'Comment {self.comment} by {self.name}'

