

from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from notes.models import Note

User = get_user_model()

class TestRoutes(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.author = User.objects.create(username='testuser')
        cls.reader = User.objects.create(username='testreader')
        cls.note = Note.objects.create(
            title='test',
            text='текст',
            slug='test_slug',
            author=cls.author,
        )

    def test_page_avalidaility(self):
        urls = (
            'notes:home',
            'users:login',
            'users:logout',
            'users:signup',
        )
        for page in urls:
            with self.subTest(page=page):
                url = reverse(page)
                response = self.client.get(url)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_redirect_page(self):
        login_url = reverse('users:login')
        urls = (
            'notes:add',
            'notes:list',
        )
        for page in urls:
            with self.subTest(page=page):
                url = reverse(page)
                redirect_url = f'{login_url}?next={url}'
                response = self.client.get(url)
                self.assertRedirects(response, redirect_url)








# [Done!] 1. Главная страница доступна анонимному пользователю.
# 2. Страница отдельной новости НЕ доступна анонимному пользователю.
# 3. Страницы списка заметок, удаления и редактирования комментария доступны автору комментария.
# 4. При попытке перейти на страницу редактирования или удаления комментария анонимный пользователь перенаправляется на страницу авторизации.
# 5. Авторизованный пользователь не может зайти на страницу списока записок, редактирования или удаления чужих комментариев (возвращается ошибка 404).
# 6. Страницы регистрации пользователей, входа в учётную запись и выхода из неё доступны анонимным пользователям.