from django.shortcuts import render

posts =[
	{
		'author': 'David Fitzgerald',
		'title': 'Post',
		'content': 'First post content',
		'date_posted': 'June 22, 2019'
	},
	{
		'author': 'Madelaine Feakins',
		'title': 'Post 2',
		'content': 'Second post content',
		'date_posted': 'June 23, 2019'
	}
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blogApp/home.html', context)

def about(request):
	return render(request, 'blogApp/about.html', {'title': 'About'})
