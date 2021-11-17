from django.shortcuts import render,get_object_or_404
from rest.models import Category,Food,Comment,Cook
from django.views.generic import ListView,DetailView
from rest.forms import CommentForm
# Create your views here.


def base(request):
    category = Category.objects.all()
    food = Food.objects.all()
    cook = Cook.objects.all()
    comment = Comment.objects.all()

    context = {
        'category':category,
        'food':food,
        'cook':cook,
        'comment':comment,
    }

    return render(request, 'rest/index.html',context)






# class CategoryView(ListView):
    
#     context_object_name = 'category'
#     template_name = 'index.html'


# class FoodView(ListView):
#     queryset = Food.objects.all()
#     context_object_name = 'food'
#     template_name = 'index.html'


# class CookView(ListView):
#     queryset = Cook.objects.all()
#     context_object_name = 'cook'
#     template_name = 'index.html'


# class CommentView(ListView):
#     queryset = Comment.objects.all()
#     context_object_name = 'comment'
#     template_name = 'index.html'

#     def comment_detail(request):
#         comments = Comment.objects.filter(active=True)
#         new_comment = None
#         if request.method == "POST":
#             form = CommentForm(request.POST)
#             if form.is_valid():
#                 new_comment = form.save(commit=False)
#                 new_comment.save()
#         else:
#             form = CommentForm()