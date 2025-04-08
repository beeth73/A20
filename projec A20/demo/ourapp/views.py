from django.shortcuts import render, redirect
from .models import Festival, Tradition
from datetime import datetime
import calendar
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def about(request):
    return render(request, 'about.html')  # Ensure the template exists in the templates folder

def login_view(request):
    return render(request, 'login.html')  # Ensure the template exists in the templates folder

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')  # Redirect to login after signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def generate_calendar(year, month):
    # Get the name of the month and the number of days in that month
    month_name = calendar.month_name[month]
    _, num_days = calendar.monthrange(year, month)
    days = list(range(1, num_days + 1))
    return {"month_name": month_name, "days": days}

# Home view
def home(request):
    # Get current year and month, or use parameters from GET request
    current_year = datetime.now().year
    current_month = datetime.now().month
    
    # Get the month number from the request, if available
    if 'month' in request.GET:
        month = int(request.GET['month'])
    else:
        month = current_month
    
    # Get calendar data for the given month and year
    calendar_data = generate_calendar(current_year, month)
    
    # Prepare the previous and next month values
    prev_month = month - 1 if month > 1 else 12
    next_month = month + 1 if month < 12 else 1
    
    return render(
        request,
        'calender.html',
        {
            'calendar_data': calendar_data,
            'current_year': current_year,
            'current_month': month,
            'prev_month': prev_month,
            'next_month': next_month,
        }
    )

# Festival details view: Fetch from DB
def festival_detail(request, festival_id):
    festival = Festival.objects.get(id=festival_id)  # Fetch the festival by ID
    return render(request, 'festival_detail.html', {"festival": festival})

# Archive view: Fetch all traditions from DB
def archive(request):
    traditions = Tradition.objects.all()  # Get all traditions
    return render(request, 'archive.html', {"traditions": traditions})

# Add entry view: Handle form submission for traditions
def add_entry(request):
    if request.method == "POST":
        # Get form data from the request
        name = request.POST.get("name")
        event_day = request.POST.get("event_day")  # Get event day
        description = request.POST.get("description", "")  # Optional description
        
        # Ensure both name and event_day are provided
        if name and event_day:
            # Create the new tradition entry
            Tradition.objects.create(
                name=name,
                event_day=event_day,
                description=description,
                date_added=timezone.now()  # Automatically set the current time
            )
            return redirect("archive")  # Redirect to the archive page after saving
        else:
            return render(request, "add_entry.html", {"error": "Both Event Name and Event Day are required!"})

    # Handle GET requests: render the form
    return render(request, "add_entry.html")

def calendar_view(request):
    # Get year and month dynamically (default to current year and month)
    year = int(request.GET.get('year', datetime.now().year))
    month = int(request.GET.get('month', datetime.now().month))
    today = datetime.now()
    month_name = calendar.month_name[month]
    _, last_day = calendar.monthrange(year, month)

    # Generate calendar data
    month_days = [0] * datetime(year, month, 1).weekday() + list(range(1, last_day + 1))
    weeks = [month_days[i:i+7] for i in range(0, len(month_days), 7)]

    context = {
        'today': today,
        'year': year,
        'month': month,
        'month_name': month_name,
        'calendar_data': weeks,
        'next_years': [2024, 2025, 2026],  # Next 2 years
    }
    return render(request, 'calender.html', context)