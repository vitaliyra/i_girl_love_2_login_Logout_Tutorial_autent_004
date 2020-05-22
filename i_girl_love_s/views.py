from django.shortcuts import render
from django.http import HttpResponseRedirect
from . forms import UserForm
from . models import Sweetmeat

from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    if request.method == "POST":
        sweetmeat = Sweetmeat()
        sweetmeat .name = request.POST.get("name")
        sweetmeat.owner = request.user
        sweetmeat.save()
        return HttpResponseRedirect("/sw/")
    else:
        sweetmeats = [ii.name for ii in Sweetmeat.objects.filter(owner=request.user)]
        userform = UserForm()
        data = {"header": "Мои любимые сладости:", "remembrancies": sweetmeats,"form": userform}
        return render(request, "i_girl_love_s/index.html", context=data)





