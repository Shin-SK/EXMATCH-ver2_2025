# master/views.py
from django.shortcuts import render
from django.http import Http404, HttpResponseForbidden
from django.template.exceptions import TemplateDoesNotExist

def serve_static_page(request, filename):
    # ディレクトリトラバーサル防止
    if '..' in filename or '/' in filename or '\\' in filename:
        return HttpResponseForbidden("Forbidden")

    try:
        return render(request, filename)
    except TemplateDoesNotExist:
        raise Http404("Page not found")
