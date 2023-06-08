from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from .models import *


# Create your views here.
def index(request):
    return render(request, 'bincom_app/index.html')


def polling_unit_result(request, polling_unit_id):
    result = AnnouncedPuResult.objects.all()
    party_scores = result.values_list('party_score', flat=False)
    party_abbreviations = result.values_list('party_abbreviation', flat=False)
    context = {
        'result': result,
        'party_scores': party_scores,
        'party_abbreviations': party_abbreviations
    }
    return render(request, 'bincom_app/polling_unit_result.html', context)


def lga_result_page(request):
    lgas = AnnouncedLgaResult.objects.values('lga_name').distinct()

    if request.method == 'POST':
        selected_lga = request.POST.get('selected_lga')
        total_score = AnnouncedLgaResult.objects.filter(lga_name=selected_lga).aggregate(Sum('party_score'))

        context = {
            'lgas': lgas,
            'selected_lga': selected_lga,
            'total_score': total_score['party_score__sum'],
        }

        return render(request, 'bincom_app/lga_result.html', context)

    context = {
        'lgas': lgas,
    }

    return render(request, 'bincom_app/lga_result.html', context)


def store_results(request):
    if request.method == 'POST':
        ward_name = request.POST.get('ward_name')
        party_scores = request.POST.getlist('party_score[]')
        party_abbreviations = request.POST.getlist('party_abbreviation[]')
        entered_by_user = request.POST.get('entered_by_user')
        user_ip_address = request.META.get('REMOTE_ADDR')

        for score, abbreviation in zip(party_scores, party_abbreviations):
            result = AnnouncedWardResult.objects.create(
                ward_name=ward_name,
                party_abbreviation=abbreviation,
                party_score=score,
                entered_by_user=entered_by_user,
                date_entered=timezone.now(),
                user_ip_address=user_ip_address
            )
            result.save()

        return HttpResponse('Results stored successfully.')

    return render(request, 'bincom_app/store_results.html')
