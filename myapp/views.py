
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact  # Your Contact model
from .forms import ContactForm  # Your ContactForm
from .forms import LoginForm
from .models import Authenticate as authenticate
from django.contrib.auth.decorators import login_required


@login_required
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save data to the database
            return render(request, 'thank_you.html', {'name': form.cleaned_data['name']})
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})



from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.timezone import now
from .models import ContactChangeLog

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.timezone import now
from .models import ContactChangeLog
import pytz
from django.utils.timezone import now

@login_required
def contact_edit_view(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)

        if form.is_valid():
            # Fetch the original instance from the database again to ensure consistency
            original_contact = Contact.objects.get(pk=pk)
            
            # Track changes dynamically
            changes = {}

            # Get the dynamically changed fields from the form
            for field in form.changed_data:
                old_value = getattr(original_contact, field)  # Old value from the database
                new_value = form.cleaned_data[field]  # New value from the form

                # Add the change to the dictionary
                changes[field] = {
                    "old": old_value,
                    "new": new_value,
                }

            # Save the updated contact
            form.save()

            # Convert the timestamp to Pakistan Standard Time (PST)
            pakistan_tz = pytz.timezone('Asia/Karachi')
            timestamp = now().astimezone(pakistan_tz)

            # Log changes dynamically
            for field, change in changes.items():
                ContactChangeLog.objects.create(
                    username=request.user.username,
                    contact=contact,
                    field_name=field,
                    old_value=change["old"],
                    new_value=change["new"],
                    timestamp=timestamp,
                )

            return redirect('contact_edit', pk=pk)

    else:
        form = ContactForm(instance=contact)

    # Pass the original field values to the template
    initial_values = {field.name: getattr(contact, field.name) for field in form}

    return render(request, 'edit_contact.html', {'form': form, 'contact': contact, 'initial_values': initial_values})

from django.shortcuts import redirect

@login_required
def contact_list_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save data to the database
            # Redirect to the same page after saving the form data
            return redirect('contact_list')  # Replace 'contact_list' with your URL name for the contact list view
    else:
        form = ContactForm()

    contacts = Contact.objects.all()  # Fetch all records from the database
    return render(request, 'contact_list.html', {'form': form, 'contacts': contacts})




from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/contact")  # Redirect to home or dashboard page
        else:
            msg = "Invalid credentials"
    elif request.method == "POST":
        msg = "Error validating the form"

    return render(request, "Login.html", {"form": form, "msg": msg})

