from django.shortcuts import render
from .models import PaymentInfo

def payments_chart(request):
    payments = PaymentInfo.objects.select_related("payer_id").order_by("pay_date")
    data = [
        {
            "date": p.pay_date.strftime("%Y-%m-%d"),
            "amount": float(p.amount),
            "payer": f"{p.payer_id.first_name} {p.payer_id.last_name}"
        }
        for p in payments
    ]
    return render(request, "payments/chart.html", {"data": data})