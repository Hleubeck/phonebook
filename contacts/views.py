from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Contacts
from django.http import Http404


def index(request):
    contacts = Contacts.objects.order_by('name')
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
