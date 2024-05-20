import os

from django import forms
from django.core.mail import EmailMessage
from .models import Inquiry


class InquiryForm(forms.ModelForm):
    POSSIBILITY_CHOICES = [
        ('採用', '採用'),
        ('不採用', '不採用'),
    ]
    REUSE_CHOICES = [
        ('未', '未'),
        ('済', '済'),
    ]
    GENRE_CHOICES = [
        ('シンプル', 'シンプル'),
        ('イラストレーション', 'イラストレーション'),
        ('写真重視', '写真重視'),
        ('レトロ', 'レトロ'),
        ('カラフル', 'カラフル'),
        ('情報重視', '情報重視'),
        ('タイポグラフィ', 'タイポグラフィ'),
    ]

    possibility = forms.ChoiceField(label='採用の可否', choices=POSSIBILITY_CHOICES, required=False)
    reuse = forms.ChoiceField(label='再利用', choices=REUSE_CHOICES, required=False)

    # チェックボックスのフィールドを追加
    genres = forms.MultipleChoiceField(
        label='デザインの種類',
        choices=GENRE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Inquiry
        exclude = ['created_at']  # created_at を除外
        fields = '__all__'

    # カスタムのバリデーションやウィジェットの設定が必要な場合はここに追加
    widgets = {
        'genres': forms.Select(choices=GENRE_CHOICES),
    }



    pdf_file = forms.FileField(label='PDFファイル', required=False)

    shiji_no = forms.CharField(label='指示書No', max_length=6)
    shiji_name = forms.CharField(label='品名', max_length=99, required=False)
    name = forms.CharField(label='制作者', max_length=30)
    email = forms.EmailField(label='メールアドレス', required=False)
    purpose = forms.CharField(label='用途', max_length=99)
    message = forms.CharField(label='備考', widget=forms.Textarea, required=False)
    design_image = forms.ImageField(label='デザイン画像', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = " " #ラベルの末尾につくコロンを消す

        self.fields['shiji_no'].widget.attrs['class'] = 'form-control'
        self.fields['shiji_no'].widget.attrs['placeholder'] = '指示書Noをここに入力してください。'

        self.fields['shiji_name'].widget.attrs['class'] = 'form-control'
        self.fields['shiji_name'].widget.attrs['placeholder'] = '品名をここに入力してください。'

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = '制作者をここに入力してください。'

        self.fields['possibility'].widget.attrs['class'] = 'form-select'

        self.fields['reuse'].widget.attrs['class'] = 'form-select'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスをここに入力してください。'

        self.fields['purpose'].widget.attrs['class'] = 'form-control'
        self.fields['purpose'].widget.attrs['placeholder'] = '用途をここに入力してください。（例：Webサイト）'

        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = '備考をここに入力してください。'
        self.fields['message'].widget.attrs['rows'] = 3

        self.fields['design_image'].widget.attrs['class'] = 'form-control'

        self.fields['pdf_file'].widget.attrs['class'] = 'form-control'
        self.fields['pdf_file'].widget.attrs['accept'] = '.pdf'

    # 既存のフォームセットに新しいフィールドを追加
    def clean(self):
        cleaned_data = super().clean()
        design_image = cleaned_data.get('design_image')
        pdf_file = cleaned_data.get('pdf_file')
        genres = cleaned_data.get('genres')

        # どちらかのファイルがアップロードされていることを確認
        if not design_image and not pdf_file:
            raise forms.ValidationError("デザイン画像またはPDFファイルのいずれかをアップロードしてください。")

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        purpose = self.cleaned_data['purpose']
        message = self.cleaned_data['message']

        subject = 'お問い合わせ {}'.format(name)
        message = '送信者名: {0}\nメールアドレス: {1}\nメッセージ:\n{2}'.format(name, email, message)
        from_email = os.environ.get('FROM_EMAIL')
        to_list = [
            os.environ.get('FROM_EMAIL')
        ]
        cc_list = [
            email
        ]

        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list, cc=cc_list)
        message.send()





# views.py

from django.shortcuts import render, get_object_or_404
from django.views import View  # Viewを追加
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from .models import Inquiry
from .forms import InquiryForm

class EditInquiryView(View):
    template_name = 'edit_inquiry.html'

    def get(self, request, inquiry_id):
        inquiry = get_object_or_404(Inquiry, id=inquiry_id)
        form = InquiryForm(instance=inquiry)
        # genresのchoicesを指定
        form.fields['genres'].widget.choices = InquiryForm.GENRE_CHOICES
        return render(request, self.template_name, {'form': form, 'inquiry': inquiry})




class EditInquiryForm(forms.ModelForm):
    # 他のフィールドの定義...

    genres = forms.MultipleChoiceField(
        choices=[('シンプル', 'シンプル'), ('イラストレーション', 'イラストレーション'), ...],
        widget=forms.CheckboxSelectMultiple,
        required=False  # 必要に応じて変更
    )

    class Meta:
        model = Inquiry  # 適切なモデルに変更
        fields = '__all__'









# forms.py に追加
class InquirySearchForm(forms.Form):
    # 他のフィールド...
    genres = forms.CharField(label='デザインの種類', required=False)
