from django.test import TestCase
from accounts.serializers import UserSerializer

class UserSerializerTest(TestCase):
    def setUp(self):
        # Crie um usuário de exemplo para ser usado nos testes
        self.user_data = {
            'email': 'test@example.com',
            'username': 'testuser',
            'password': 'testpassword',
            'first_name': 'Test',
            'last_name': 'User',
            'bio': 'This is a test bio.',
            'website': 'http://www.example.com',
            'profile_picture': None,  # Substitua isso pelo caminho real da imagem, se necessário
        }

    def test_user_serializer(self):
        # Serialize os dados do usuário
        serializer = UserSerializer(data=self.user_data)
        self.assertTrue(serializer.is_valid())

        # Salve o usuário no banco de dados
        user_instance = serializer.save()

        # Verifique se os dados serializados correspondem aos dados salvos
        self.assertEqual(serializer.data['email'], self.user_data['email'])
        self.assertEqual(serializer.data['username'], self.user_data['username'])
        # Adicione verificações adicionais conforme necessário

        # Verifique se a senha foi definida corretamente
        self.assertTrue(user_instance.check_password(self.user_data['password']))
