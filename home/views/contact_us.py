from django.shortcuts import render,redirect
from django.core.exceptions import ValidationError

from ticket.models import TicketModel


def contact_us(request):

    if request.method == "POST":
        author = request.POST.get("author", "").strip()
        phone_number = request.POST.get("phone_number", "").strip()
        message = request.POST.get("message", "").strip()

        if not author or not phone_number or not message:
            return render(request, "contact.html", {
                "error": "لطفاً تمام فیلدها را تکمیل کنید."
            })

        _ticket = TicketModel(
            author=author,
            phone_number=phone_number,
            message=message,
        )

        try:
            _ticket.full_clean()
        except ValidationError as e:
            return render(request, "contact.html", {
                "error": e.messages[0],
            })
        _ticket.save()

        return redirect("home:contact_us")

    else:
        return render(request, "contact.html")