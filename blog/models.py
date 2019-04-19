from django.db import models
# from django.contrib.auth.models import User   # User 임포트 chap15. 이거보다 settings 사용하는 게 좋음
from django.conf import settings
from pytz import timezone  # 현지 시각 출력을 위하여
from django.urls import reverse


def local_time(input_time):
    fmt = '%Y-%m-%d %H:%M'
    my_zone = timezone(settings.TIME_ZONE)
    my_local_time = input_time.astimezone(my_zone)
    return my_local_time.strftime(fmt)


class Post(models.Model):
    author = models.ForeignKey(  # default값으로 pk 중 1 값을 넣음 - post.author를 보면 1에 해당하는 User인 hywoman이 들어있음
    # u1 변수에 hywoman을 넣고 이 유저가 쓴 모든 글을 보려면, u1.post_set.all()로 확인 가능. 자식인 Post는 소문자로 쓴다. - chap15의 related_name 부분 참고
    # Post.objects.filter(author=u1)도 related_name과 같은 결과. == u1.post_set.all() 과 같음
        settings.AUTH_USER_MODEL,  # 'auth.User'라고 쓰는 것보다 강추
        on_delete=models.CASCADE,
        # related_name='post_set',  # 기본 설정과 동일하므로 주석 처리
        related_name='posts',  # post_set 대신 이거로 씀
        verbose_name='게시자',  # admin 화면에서 author가 게시자로 표시됨
    )
    # verbose_name: 관리자 화면 등에서 열 제목으로 사용될 속성
    # 관계 필드에서 첫 인자는 관계 대상 모델, verbose_name 키워드 인자로 처리
    # 관계 필드가 아닌 일반 필드의 (생략 가능한) 첫 인자는 verbose_name
    # 위의 ForeignKey와 CharField를 비교해서 보기!
    title = models.CharField('제목', max_length=100)
    content = models.TextField('내용')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='tags')
    # Tag는 verbose_name이 아니라 관계 대상 모델!!

    class Meta:
        ordering = ['-id']  # Post 객체의 기본 정렬 순서 지정

    def __str__(self):
        return self.title

    # 내용이 존재하면 20까지 자르고 뒤에 ...을 붙이는 함수
    def short_content(self):  # 속성으로 존재하는 것처럼 만들기
        if self.content:
            t = self.content[:20] + '...'   # content 속성의 일부만 반환
        else:
            t = '(내용 없음)'
        return t
    # 아래는 일반 필드의 verbose_name과 비슷함
    short_content.short_description = '간략 내용'

    # tags는 태그 집합(리스트)를 보여주기 때문에 태그 이름만 문자열로 출력해주는 함수
    def tagged(self):
        ts = self.tags.all()  # self.tags는 관리자!
        # 방법1
        return '{' + ', '.join(map(str, ts)) + '}'
        # 방법2
        # return ', '.join(ts)  # 이건 에러!!
        
        #방법3
        # if ts:
        #     tag_string = '{'
        #     for t in ts:  # M2M 속성은 관리자이지, 쿼리셋이 아님  -> Tag.objects처럼 관리자. ts는 self.tags를 사용하면 안됨
        #         tag_string += t.name + ', '  # t가 아니라 t.name
        #     tag_string = tag_string[:len(tag_string)-2] + '}'
        #     # tag_string 후미 ', '를 '}'으로 치환
        # else:
        #     tag_string = '{ }'
        # return tag_string
    tagged.short_description = '태그 집합'
    # 클래스 메소드로 속성을 대신할 때, verbose_name 대신에 short_description

    # 생성된 시각과 수정된 시각 중 수정 시각을 보여줌
    def updated(self):
        return local_time(self.updated_at)
    updated.short_description = '수정 일시'

    def get_absolute_url(self):
        # return reverse('blog:post_detail', args=[self.pk])
        return reverse('blog:post_detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    # post = models.ForeignKey(Post)  # 오류! 아래가 정답
    # Comment의 부모는 Post이다. 자식객체.부모모델이름 가능
    # p = Post.objects.get(title__contains='하시')
    # p.comment_set.all() 두 명령으로 '하시'가 포함된 글의 모든 댓글을 확인할 수 있음
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments', verbose_name='게시물')
    message = models.TextField('댓글')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:  # id는 Comment의 id
        ordering = ['-post__id', '-id']  # '-post__id', '-id'
    
    def __str__(self):
        return self.message
    
    def updated(self):
        return local_time(self.updated_at)
    
    updated.short_description = '수정 일시'


class Tag(models.Model):
    name = models.CharField('태그', max_length=100, unique=True)
    
    class Meta:
        ordering = ['-id']  # Tag 객체의 기본 정렬 순서 지정
    
    def __str__(self):
        return self.name
