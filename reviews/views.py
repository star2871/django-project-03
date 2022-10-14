from django.shortcuts import render, redirect
from reviews.models import Review
from .forms import ReviewForm

# Create your views here.
def create(request):
    # title = request.POST.get("title")
    # content = request.POST.get("content")
    # Article.objects.create(title=title, content=content)
    # return redirect("articles:index")
    if request.method == "POST":
        # DB에 저장하는 로직
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect("accounts:index")
    else:
        review_form = ReviewForm()
    context = {"review_form": review_form}
    return render(request, "reviews/create.html", context=context)


def index(request):
    reviews = Review.objects.order_by("-pk")
    context = {
        "reviews": reviews,
    }
    return render(request, "reviews/index.html", context)


def detail(request, pk):
    # 특정 글을 가져온다.
    review = Review.objects.get(pk=pk)
    # template에 객체 전달
    context = {
        "review": review,
    }
    return render(request, "reviews/detail.html", context)
