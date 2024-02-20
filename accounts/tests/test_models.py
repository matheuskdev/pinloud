from django.test import TestCase
from django.contrib.auth import get_user_model

class UserModelTests(TestCase):
    def setUp(self):
        self.user_data = {
            'email': 'testuser@example.com',
            'username': 'testuser',
            'password': 'testpassword',
        }
        self.user = get_user_model().objects.create_user(**self.user_data)

    def test_create_user(self):
        # Testa a criação de um usuário com sucesso
        User = get_user_model()
        user = User.objects.create_user(
            email='test@example.com',
            username='unique_testuser',
            password='testpassword'
        )
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.username, 'unique_testuser')
        self.assertTrue(user.check_password('testpassword'))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        # Testa a criação de um superusuário com sucesso
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            email='admin@example.com',
            username='adminuser',
            password='adminpassword'
        )
        self.assertEqual(admin_user.email, 'admin@example.com')
        self.assertEqual(admin_user.username, 'adminuser')
        self.assertTrue(admin_user.check_password('adminpassword'))
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

    def test_email_normalize(self):
        # Testa se o email é normalizado corretamente
        normalized_email = get_user_model().objects.normalize_email('testuser@EXAMPLE.com')
        self.assertEqual(normalized_email, 'testuser@example.com')

    def test_str_representation(self):
        # Testa a representação de string do modelo
        self.assertEqual(str(self.user), self.user_data['email'])
