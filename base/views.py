from django.shortcuts import render

# Create your views here.

def index(request):
    """
    Render the index page of the application.
    
    Args:
        request: The HTTP request object.
        
    Returns:
        HttpResponse: Rendered index page.
    """
    return render(request, 'base/pages/home.html')   