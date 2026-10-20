from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib import messages

from ticket.models import TicketModel


def contact_us(request):

    if request.method == "POST":
        author = request.POST.get("author", "").strip()
        phone_number = request.POST.get("phone_number", "").strip()
        message = request.POST.get("message", "").strip()

        if not author or not phone_number or not message:
            messages.error(
                request,
                "لطفاً تمام فیلدها را تکمیل کنید."
            )
            return redirect("home:contact_us")

        _ticket = TicketModel(
            author=author,
            phone_number=phone_number,
            message=message,
        )

        try:
            _ticket.full_clean()

        except ValidationError as e:
            for error in e.messages:
                messages.error(request, error)

            return redirect("home:contact_us")

        _ticket.save()

        messages.success(
            request,
            "تیکت شما با موفقیت ثبت شد."
        )

        return redirect("home:contact_us")

    return render(request, "contact.html")