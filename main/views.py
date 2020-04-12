from django.shortcuts import render
from .forms import EmailConForm
from django.core.mail import send_mail


def view(request):
    sent = False
    if request.method == 'POST':
        form = EmailConForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = 'send'
            message = 'name: {}\nemail: {}\nphone {}'.format(cd['name'], cd['email'], cd['number'])
            send_mail(subject, message, 'lkek91540@gmail.com', ['agentall228@gmail.com'])

        else:
            form = EmailConForm()
            return render(request, 'index.html', {'form': form})
    return render(request, 'index.html', {'form': form})
