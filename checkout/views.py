from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required
def checkout(request):
    if request.method == 'POST':
        token = request.POST[stripeToken]
        print(token)
    context = {}
    templates = 'checkout.html'
    return render(request, templates, context)
