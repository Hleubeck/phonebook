from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Contacts
from django.http import Http404
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages


def index(request):
    contacts = Contacts.objects.order_by('-id')
    paginator = Paginator(contacts, 15)
    page = request.GET.get('p')
    contacts = paginator.get_page(page)
    return render(request, 'contacts/index.html', {
        'contacts': contacts
    })


def contact_info(request, contact_id):
    contact = get_object_or_404(Contacts, id=contact_id)
    if not contact.hidecontact:
        raise Http404()
    return render(request, 'contacts/contact_info.html', {
        'contact': contact
    })


def search(request):
    keyword = request.GET.get('lookingfor')

    if keyword is None or not keyword:
        messages.add_message(request, messages.ERROR,
                             "Busca Inválida!")
        return redirect('index')
    fullname_field = Concat('name', Value(' '), 'surname')
    contacts = Contacts.objects.annotate(
        fullname=fullname_field).filter(
            Q(fullname__icontains=keyword) | Q(uf=keyword) | Q(state=keyword)
        )
    paginator = Paginator(contacts, 15)
    page = request.GET.get('p')
    contacts = paginator.get_page(page)
    return render(request, 'contacts/search.html', {
        'contacts': contacts
    })
