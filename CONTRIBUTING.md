# Guia de Contribuição

Obrigado por seu interesse em contribuir com a Biblioteca Pública Digital! Seguindo estas diretrizes, você nos ajuda a manter um projeto organizado e colaborativo.

## Como Posso Contribuir?

### 🐛 Reportando Bugs
1. **Verifique se o bug já foi reportado** na [seção de Issues](https://github.com/seu-usuario/biblioteca-publica/issues)
2. **Use o template de bug report** e inclua:
   - Descrição clara do problema
   - Passos para reproduzir
   - Comportamento esperado vs atual
   - Screenshots (se aplicável)
   - Ambiente (SO, navegador, versões)

### 💡 Sugerindo Melhorias
1. **Pesquise se a ideia já foi sugerida**
2. **Descreva detalhadamente** sua sugestão
3. **Explique o porquê** seria útil para o projeto
4. **Inclui exemplos** de uso, se possível

### 🔧 Primeira Contribuição

Procuramos marcar issues com `good-first-issue` para novos contribuidores:

1. **Encontre uma issue** marcada com `good-first-issue`
2. **Comente na issue** dizendo que gostaria de trabalhar nela
3. **Siga o processo de desenvolvimento abaixo**

## Processo de Desenvolvimento

### 1. Configuração do Ambiente
```bash
# Fork e clone o repositório
git clone https://github.com/seu-usuario/biblioteca-publica.git
cd biblioteca-publica

# Configure backend
cd projeto
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt

# Configure frontend
cd ../frontend
npm install

2. Criando uma Branch
bash
git checkout -b feature/nome-da-feature
# ou
git checkout -b fix/nome-do-bug
3. Fazendo as Alterações
Siga o padrão de código existente

Adicione testes quando possível

Atualize a documentação

Certifique-se de que o código passa nos testes

4. Commits
Use mensagens de commit claras e descritivas:

bash
git commit -m "feat: adiciona busca por autor no catálogo"
git commit -m "fix: corrige validação de data de empréstimo"
5. Enviando as Alterações
bash
git push origin sua-branch
6. Abrindo um Pull Request
Preencha o template de PR completamente

Descreva suas mudanças e o motivo

Linke as issues relacionadas

Aguarde o review da equipe

Padrões de Código
Backend (Django)
Siga as convenções do Django

Use docstrings para documentação

Mantenha as views e serializers organizados

Frontend (React)
Use componentes funcionais com hooks

Siga a estrutura de pastas existente

Mantenha os estilos consistentes

Dúvidas?
Abra uma issue para discussão

Entre em contato com os maintainers

Consulte a documentação do projeto

Obrigado por contribuir! 🎉
