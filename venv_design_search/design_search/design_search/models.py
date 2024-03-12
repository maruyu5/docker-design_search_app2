from django.db import models


class Post(models.Model):
    # モデルのフィールドをここに定義する
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class EmailModel(models.Model):
    email = models.EmailField()


class Inquiry(models.Model):
    POSSIBILITY_CHOICES = [
        ('採用', '採用'),
        ('不採用', '不採用'),
    ]
    REUSE_CHOICES = [
        ('未', '未'),
        ('済', '済'),
    ]


    shiji_no = models.CharField(max_length=30)
    shiji_name = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    possibility = models.CharField(max_length=10, choices=POSSIBILITY_CHOICES, null=True, blank=True)
    reuse = models.CharField(max_length=10, choices=REUSE_CHOICES, null=True, blank=True)
    email = models.EmailField()
    purpose = models.CharField(max_length=30)
    message = models.TextField()
    design_image = models.ImageField(upload_to='inquiry_images/', null=True, blank=True)
    pdf_file = models.FileField(upload_to='inquiry_files/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    genres = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.shiji_no
