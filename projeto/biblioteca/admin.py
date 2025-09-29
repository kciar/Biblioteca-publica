# biblioteca/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Livro, Emprestimo

# Registrar o modelo de usuário customizado
@admin.register(Usuario)
class CustomUserAdmin(UserAdmin):
    model = Usuario
    list_display = ("username", "email", "first_name", "last_name", "telefone", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Informações Pessoais", {"fields": ("first_name", "last_name", "email", "telefone")}),
        ("Permissões", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
        ("Datas", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "telefone", "password1", "password2", "is_staff", "is_active")}
        ),
    )
    search_fields = ("username", "email", "first_name", "last_name")
    ordering = ("username",)

# Registrar o modelo de livros
@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "ano", "genero", "disponivel")
    list_filter = ("genero", "disponivel")
    search_fields = ("titulo", "autor")

# Registrar o modelo de empréstimos
@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ("livro", "usuario", "data_emprestimo", "data_devolucao", "status")
    list_filter = ("status", "data_emprestimo")
    search_fields = ("livro__titulo", "usuario__username")
