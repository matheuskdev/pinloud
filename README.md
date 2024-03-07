# PinLoud

PinLoud é uma aplicação Django e Django Rest Framework para compartilhamento de pins.

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/pinloud.git
   ```

2. Crie um ambiente virtual e instale as dependências:

   ```bash
   cd pinloud
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   # Ou para Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Execute as migrações do banco de dados:

   ```bash
   python manage.py migrate
   ```

4. Crie um superusuário para acessar o painel de administração:

   ```bash
   python manage.py createsuperuser
   ```

5. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

A aplicação estará disponível em http://127.0.0.1:8000/.

## Uso

- Acesse o painel de administração em http://127.0.0.1:8000/admin/ para gerenciar usuários, pins e outras configurações.

- Utilize as APIs REST disponíveis em http://127.0.0.1:8000/api/v1/ para interagir programaticamente com a aplicação.

- Inteaja com a APIs REST disponível em http://127.0.0.1./swagger/ vizualizando de melhor forma os endpoins.

## Contribuindo

Se quiser contribuir, por favor, siga estas etapas:

1. Faça o fork do repositório.
2. Crie um branch para a sua feature (`git checkout -b feature/sua-feature`).
3. Commit suas mudanças (`git commit -m 'Adiciona alguma funcionalidade'`).
4. Push para o branch (`git push origin feature/sua-feature`).
5. Abra um Pull Request.
