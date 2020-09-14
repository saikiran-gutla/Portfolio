from django.http import HttpResponse
from django.shortcuts import redirect


def is_user_unauthenticated(view_func):
    def wrapper_fun(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('blogger_homepage')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_fun
