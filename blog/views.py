from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.


def blog_post(request, article_id):

    blog_posts = [
        {'id': 1, 'title': 'First Blog Post Title','author': 'Inyang Ukpong', 'content': 'This is a summary of the first blog post', 'date': "January 2, 2024"},
        {'id': 2, 'title': 'Second Blog Post Title','author': 'Queenie Walker', 'content': 'This is a summary of the second blog post', 'date': "January 4, 2024"},
        {'id': 3, 'title': 'Third Blog Post Title','author': 'Johnny Swagger', 'content': 'This is a summary of the third blog post that will exeed fifty characters to demonstrate truncation.', 'date': "January 6, 2024"}
    ]

    selected_post = None

    for post in blog_posts:
        if article_id == post['id']:
            selected_post = post
            break

    if selected_post == None:
        raise Http404("No Post Found")
    
    return render(request, 'blog/post.html', selected_post)

def blog_archive(request):
    # get all the blog posts from the database
    # put them in a list
    blog_posts = [
        {'id': 1, 'title': 'First Blog Post Title','author': 'Inyang Ukpong', 'content': 'This is a summary of the first blog post', 'date': "January 2, 2024"},
        {'id': 2, 'title': 'Second Blog Post Title','author': 'Queenie Walker', 'content': 'This is a summary of the second blog post', 'date': "January 4, 2024"},
        {'id': 3, 'title': 'Third Blog Post Title','author': 'Johnny Swagger', 'content': 'This is a summary of the third blog post that will exeed fifty characters to demonstrate truncation.', 'date': "January 6, 2024"}
    ]

    context = {"list_of_posts": blog_posts}
    return render(request, 'blog/index.html', context)





# def blog(request, article_id):
    if request.method == "GET":
        # get the specific article
        pass
    elif request.method == "POST":
        # create a new article with this id
        pass
    elif request.mehtod == "PUT":
        # update the article
        pass
    elif request.mehtod == "DELETE":
        # delete this article
        pass
    return HttpResponse(f"<h1>Blog {article_id}</h1>")