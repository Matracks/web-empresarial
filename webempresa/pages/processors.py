from .models import Page


def ctx_dict(request):
    ctx = {}
    pages = Page.objects.all()
    c = 1
    for page in pages:
        ctx[page.title] = c
        c += 1
    return ctx
