# biblioteca/views.py
from rest_framework import viewsets
from .models import Usuario, Livro, Emprestimo
from .serializers import UsuarioSerializer, LivroSerializer, EmprestimoSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_permissions(self):
        # permitir registro (create) sem autenticação
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]


class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    permission_classes = [IsAuthenticated]


class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.select_related('usuario', 'livro').all()
    serializer_class = EmprestimoSerializer
    permission_classes = [IsAuthenticated]

    # endpoint extra opcional para devolver um livro rapidamente
    @action(detail=True, methods=['post'])
    def devolver(self, request, pk=None):
        emprestimo = self.get_object()
        if emprestimo.status == 'DEVOLVIDO':
            return Response({'detail': 'Empréstimo já está devolvido.'}, status=status.HTTP_400_BAD_REQUEST)
        emprestimo.status = 'DEVOLVIDO'
        emprestimo.data_devolucao = emprestimo.data_devolucao or timezone.now().date()
        emprestimo.save()
        # marcar livro disponível
        livro = emprestimo.livro
        livro.disponivel = True
        livro.save()
        serializer = self.get_serializer(emprestimo)
        return Response(serializer.data)
