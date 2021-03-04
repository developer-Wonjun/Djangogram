#테스트코드없이 테스트를한다면 테스트를 위해서 서버를 껐다켯다해야함.
#상황에 맞춰 다양하게 테스트를 해야하기때문에만듬
 
from django.test import TestCase
from django.urls import reverse

class TestPosts(TestCase):

    def test_get_posts_page(self):

        url = revers('post:post_create')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_create.html')
        