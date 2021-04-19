from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from django.http import HttpResponse
import datetime
from .models import Post,Category,Comment,CommentForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import  Q
# Create your views here.
def blog(request):
    blog = Post.objects.order_by('-timestamp')
    categories = Category.objects.filter()
    paginator = Paginator(blog, 2)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    # category_count = get_category_count()

    context = {
        'listings':paged_listings,
        'categories':categories,
        
    }
    return render(request, 'blog/blog.html',context)
def blogdetails(request,slug):
  
    post = get_object_or_404(Post,  slug=slug)   
    posts = Post.objects.all()
    latest_post = Post.objects.order_by('-timestamp')[:4]
    categories = Category.objects.all()
    # list of active parent comments
    comments = post.comments.filter(active=True, parent__isnull=True)
    if request.method == 'POST':
        # comment has been added
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            parent_obj = None
            # get parent comment id from hidden input
            try:
                # id integer e.g. 15
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            # if parent_id has been submitted get parent_obj id
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                # if parent object exist
                if parent_obj:
                    # create replay comment object
                    replay_comment = comment_form.save(commit=False)
                    # assign parent_obj to replay comment
                    replay_comment.parent = parent_obj
            # normal comment
            # create comment object but do not save to database
            new_comment = comment_form.save(commit=False)
            # assign ship to the comment
            new_comment.post = post
            # save
            new_comment.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()
    return render(request,'blog/blogdetails.html',
                  {'obj': post,
                  
                   'comments': comments,
                   'posts':posts,
                   'latest_post':latest_post,
                    'categories': categories,
                   'comment_form': comment_form})    



def Posts_in_CategoryView(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts_in_cat = category.post_set.all()

    

    # pagination
    paginator = Paginator(posts_in_cat, 1) # Show 8 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
            'posts_in_cat':posts_in_cat,
            'cat_name': category,
            'page_obj': page_obj,
    }
   
   
    
    return render(request, 'blog/posts_in_category.html', context)
    
def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset,
        'query':query
    }
    return render(request, 'blog/search_results.html', context)                     