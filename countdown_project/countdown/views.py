from django.shortcuts import render
from datetime import datetime, timedelta

def countdown(request):
    # Set the target date and time
    target_date = datetime(2024, 7, 30, 0, 0, 0)  # Example target date
    now = datetime.now()
    time_remaining = target_date - now

    context = {
        'days': f"{time_remaining.days:02}",
        'hours': f"{time_remaining.seconds // 3600:02}",
        'minutes': f"{(time_remaining.seconds % 3600) // 60:02}",
        'seconds': f"{time_remaining.seconds % 60:02}",
    }

    return render(request, 'countdown.html', context)