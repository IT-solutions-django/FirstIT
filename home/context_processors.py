from contacts.models import CompanyInfo
from contacts.forms import RequestForm


def company_info(request):
    try:
        info = CompanyInfo.get_instance()
    except CompanyInfo.DoesNotExist:
        info = None

    page_headings = {
        'services': 'Услуги', 
        'cases': 'Кейсы', 
        'about': 'Компания', 
    }

    page_heading = 'First IT Company'
    for key, value in page_headings.items(): 
        if request.path.endswith(f'{key}/'): 
            page_heading = value 
            break

    context = {
        'company_info': info,
        'page_heading': page_heading,
        'request_form': RequestForm(request.GET)
    }

    return context