from django.core.mail import send_mail
from django.utils.html import format_html


def send_confirmation_email(email, code):
    activation_url = f'http://localhost:8000/api/v1/account/activate/?u={code}'

    # message = format_html(
    #     'Hello, activate your account!'
    #     'Click on the link to activate'
    #     '<br>'
    #     '<a href="{}"></a>'
    #     '</br>'
    #     "Don't show it anyone",
    #     activation_url, activation_url
    # )
    message = format_html(
        'Hello, activate your account!'
        'Click on the link to activate'
        "{}"
        "Don't show it anyone",
        activation_url,
    )
    safe_output = format_html('<br><a href="{}">CLICK HERE</a></br>', activation_url)

    send_mail(
        'Hello, activate your account!',
        message,
        'checkemail@gmail.com',
        [email],
        fail_silently=False,
    )



