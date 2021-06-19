from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.signing import BadSignature
from django.http import HttpResponse, Http404

from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.shortcuts import render, get_object_or_404, redirect

from main.forms import RegisterUserForm
from main.models import AdvUser
from main.utitlities import signer


def index(request):
    return render(request, 'main/index.html')

def other_page(request, page):
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))

class BBLoginView(LoginView):
    template_name = 'main/login.html'

@login_required
def profile(request):
    return render(request, 'main/profile.html')


class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'main/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main:register_done')


class RegisterDoneView(TemplateView):
    template_name = 'main/register_done.html'


def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'main/bad_signature.html')
    user = get_object_or_404(AdvUser, username=username)
    if user.is_activated:
        template = 'main/user_is_activated.html'
    else:
        template = 'main/activation_done.html'
        user.is_active = True
        user.is_activated = True
        user.save()
    return render(request, template)

