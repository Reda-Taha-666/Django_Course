from django.shortcuts import render


posts  = [
    {
        "author":"Tom",
        "title":"post 1",
        "date":"2034/2/4",
    },

    {
        "author":"Jak", 
        "title":"post 2",
        "date":"2034/2/4",
    },

    {
        "author":"Sam",
        "title":"post ",
        "date":"2034/9/7",
    },
]

# Create your views here.
def home (request):
    return render (request, 'pages/home.html',{"posts": posts})