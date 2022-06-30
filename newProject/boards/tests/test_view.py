from django.contrib.auth.models import User
from django.test import TestCase, Client

from boards.models import Post


class TestViews(TestCase):
    def setUp(self):
        self.client = Client() #사용자처럼 요청을 보낼 수 있게 해주는 아이
        self.user01 = User.objects.create_user(username = 'user01',password='qwer1234!')  #얘는 테스트 케이스 실행시 생성 완료시 삭제되느모 db에 연관되지 않음
        self.user02 = User.objects.create_user(username='user02',
                                             password='qwer1234!')  # 얘는 테스트 케이스 실행시 생성 완료시 삭제되느모 db에 연관되지 않음
        self.post = Post.objects.create(
            title='title1',
            contents='contents1',
            writer=self.user01
        )
    def test_post_create_GET(self):
        response = self.client.get('/board/create')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'board/create.html') #어떤 템플릿을 가져다 썼는지 확인

    def test_post_create_GET_with_login(self):
        self.client.login(username = 'user01',password = 'qwer1234!')
        response = self.client.get('/board/create')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'board/create.html')  # 어떤 템플릿을 가져다 썼는지 확인

    def test_post_create_GET_without_login(self):
        #로그인이 실패한 경우이니 로그인 페이지가 뜨는지 확인
        response = self.client.get('/board/create')
        self.assertEqual(response.status_code,302)
        #나는 여기서 로그인 페이지까지 띄우는걸 생각했는데 302만 확인하네, 왜냐면 302r가 redirect 코드거덩

    def test_post_create_POST_with_login(self):
        self.client.login(username='user01', password='qwer1234!')


        response = self.client.post(
            '/board/create',
            data = {'title':'title1','contents':'contents1'}
        )

        post = Post.objects.get(title = 'title1')
        self.assertEqual(post.title,'title1')
        self.assertEqual(response.status_code,302)

    def test_post_read_POST_with_login(self):
        self.client.login(username='user01', password='qwer1234!')

        response = self.client.post(
            '/board/create',
            data={'title': 'a', 'contents': 'contents1'}
        )

        messages = list(response.context['messages'])

        self.assertEqual(len(messages),1)
        self.assertEqual(str(messages[0]), '제목은 5글자 이상이어야 합니다.')
        #self.assertEqual(response.url,'/error') #27번째 줄에서 시도했던 어디로 redirect 됐는가를 확인할 수 있음
        self.assertEqual(response.status_code, 400)

    def test_post_read_GET_with_writer(self):
        self.client.login(username='user01', password='qwer1234!')

        # self.client.post(
        #     '/board/create',
        #     data={'title': 'title1', 'contents': 'contents1'}
        # )

        response = self.client.get('/read/1') #이렇게 무언가를 체크해야 하는 상황에서는 상대경로가 아닌 절대경로를 사용해야함.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'board/list.html')
        self.assertInHTML('<button>수정</button>',response.content.decode())

    def test_post_read_GET_without_writer(self):
        self.client.login(username='user02', password='qwer1234!')
        response = self.client.get('/read/1')
        self.assertTemplateUsed(response, 'board/list.html')
        self.assertNotIn('<button>수정</button>', response.content.decode())
    def test_post_read_GET_with_otherwriter(self):
        response = self.client.get('/read/1')
        self.assertTemplateUsed(response, 'board/list.html')
        self.assertNotIn('<button>수정</button>', response.content.decode())
