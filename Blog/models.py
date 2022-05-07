from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

CATEGORY = (
    ('python', 'Python'),
    ('kotlin', 'Kotlin'),
    ('javascript', 'Javascript'),
    ('html-css', 'HTML/CSS'),
    ('hacking', 'Ethical Hacking'),
    ('devops', 'DevOps'),
    ('django', 'Django'),
    ('reactjs', 'React JS'),
    ('other', 'Other'),
)


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    title = models.CharField(max_length=255, verbose_name='Blog Post Title')
    category = models.CharField(max_length=255, choices=CATEGORY)
    banner_image = models.ImageField(verbose_name='Cover Photo',
                                     help_text='This is the banner image'
                                               ' that users will see', blank=True, null=True)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    content = RichTextField(verbose_name='Your Blog Post Content')
    published_date = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=1, help_text=
    'This designates the status of this post after saving.'
                                 )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Blog Posts'
