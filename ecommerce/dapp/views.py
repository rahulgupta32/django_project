from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import  Dealer
from capp.models import Company
from django.shortcuts import get_object_or_404

def dealer_detail(request, dealer_id):
    company = request.user.company

    dealer = get_object_or_404(Dealer, id=dealer_id, company=company)

    response_data = {
        'dealer': dealer,
        'email_id': dealer.email_id,
        'ph_no': dealer.phone_number,
        'address': dealer.address,
        'nationality':dealer.nationality,
        'state': dealer.state,
        'city': dealer.city,
        'zipcode': dealer.zipcode,
        'experience_years': dealer.experience_years,
        'company': dealer.company,
    }

    return HttpResponse(response_data, content_type='application/json')


def search_feature(request):
    # Check if the request is a post request.
    if request.method == 'POST':
        # Retrieve the search query entered by the user
        search_query = request.POST['search_query']
        # Filter your model by the search query
        dealers = Dealer.objects.filter(dealer__contains=search_query)
        return render(request, 'ecommerce/index.html', {'query': search_query, 'dealers': dealers})
    else:
        return render(request, 'ecommerce/index.html', {})
