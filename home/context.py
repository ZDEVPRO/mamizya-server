from site_settings.models import *


def settings(request):
    contact = ContactData.objects.last()

    context = {
        'contact': contact
    }
    return context
