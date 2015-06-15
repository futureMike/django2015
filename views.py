from django.shortcuts import render
from .forms import EmailForm, JoinForm
from .models import Join


def home(request):
    #print "stupid email address: %s" % request.POST["email"]
    #print "stupid name: %s" % request.POST["email_2"]
    #form = EmailForm(request.POST or None)
    #if form.is_valid():
    #    print form.cleaned_data['email']
    #    email =  form.cleaned_data['email']
    #    new_join, created = Join.objects.get_or_create(email=email)
    #   print "Join create sucessful: ", new_join, created
    #print new_join.timestamp
    
    #this is using model form:
    
    form = JoinForm(request.POST or None)
    if form.is_valid():
        new_join = form.save(commit=False)
        new_join.save()
        print "heaven helps the honkeelipped..."
    template = "home.html"
    context = {"form": form}
    return render(request, template, context)