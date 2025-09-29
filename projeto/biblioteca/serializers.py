# biblioteca/serializers.py
from rest_framework import serializers
from .models import Usuario, Livro, Emprestimo
from django.utils import timezone

class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=6)

    class Meta:
        model = Usuario
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'telefone', 'password']
        read_only_fields = ['id']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Usuario(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        pw = validated_data.pop('password', None)
        for k, v in validated_data.items():
            setattr(instance, k, v)
        if pw:
            instance.set_password(pw)
        instance.save()
        return instance


class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'autor', 'ano', 'genero', 'disponivel']
        read_only_fields = ['id']


class EmprestimoSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
    livro = serializers.PrimaryKeyRelatedField(queryset=Livro.objects.all())

    class Meta:
        model = Emprestimo
        fields = ['id', 'usuario', 'livro', 'data_emprestimo', 'data_devolucao', 'status']
        read_only_fields = ['id', 'data_emprestimo']

    def validate(self, data):
        # Se criando empréstimo: livro precisa estar disponível
        if self.instance is None:
            livro = data.get('livro')
            if not livro.disponivel:
                raise serializers.ValidationError("Livro não está disponível para empréstimo.")
        return data

    def create(self, validated_data):
        livro = validated_data['livro']
        # marcar livro como não disponível
        livro.disponivel = False
        livro.save()
        emprestimo = Emprestimo.objects.create(**validated_data)
        return emprestimo

    def update(self, instance, validated_data):
        # Se está sendo devolvido (status mudando para DEVOLVIDO ou data_devolucao preenchida),
        # marcar livro como disponível.
        status = validated_data.get('status', instance.status)
        data_devolucao = validated_data.get('data_devolucao', instance.data_devolucao)

        instance = super().update(instance, validated_data)

        if status == 'DEVOLVIDO' or data_devolucao is not None:
            livro = instance.livro
            livro.disponivel = True
            livro.save()
            instance.status = 'DEVOLVIDO'
            if instance.data_devolucao is None:
                instance.data_devolucao = timezone.now().date()
            instance.save()

        return instance
