from django.shortcuts import render
from .forms import EmailConForm
from django.core.mail import send_mail


def view(request):
    form = EmailConForm()
    if request.method == 'POST':
        form = EmailConForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = 'send'
            message = 'name: {}\nemail: {}\nphone: {}'.format(cd['name'], cd['email'], cd['number'])
            send_mail(subject, message, 'lkek91540@gmail.com', ['agentall228@gmail.com'])
            form = EmailConForm()
            sends1 = True
            down = 1
            return render(request, 'index.html', {'form': form, 'send': sends1, 'down': down})
        else:
            sends1 = False
            down = 1
            return render(request, 'index.html', {'form': form, 'send': sends1, 'down': down})
    else:

        return render(request, 'index.html', {'form': form})
