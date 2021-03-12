from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuario, EditarUsuarioForm, EditarPerfilForm


def registrar(request):
    if request.method == 'POST':
        form = RegistroUsuario(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, message=f'Conta criada para {username}!')
            return redirect('login')
    else:
        form = RegistroUsuario()

    context = {
        'form': form,
    }

    return render(request, 'registrar.html', context)


@login_required()
def perfil(request):
    if request.method == 'POST':
        u_form = EditarUsuarioForm(request.POST, instance=request.user)
        p_form = EditarPerfilForm(request.POST,
                                  request.FILES,
                                  instance=request.user.perfil)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, message=f'Conta modificada!')
            return redirect('perfil')
    else:
        u_form = EditarUsuarioForm(instance=request.user)
        p_form = EditarPerfilForm(instance=request.user.perfil)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'perfil.html', context)
