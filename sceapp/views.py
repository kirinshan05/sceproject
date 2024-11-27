from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from .models import Post

from django.views.generic import ListView,CreateView
from django.contrib.auth.models import User
from .models import Post

from django.views.generic import FormView
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.contrib import messages



# class Home(LoginRequiredMixin, ListView):
#     """HOMEページで、すべてのユーザー投稿をリスト表示"""
#     model = Post
#     template_name = 'index.html'
    
#     def get_queryset(self):
#         return Post.objects.all()
    

class CreatePost(LoginRequiredMixin, CreateView):
    """投稿フォーム"""
    model = Post
    template_name = 'create.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('mypost')

    def form_valid(self, form):
        """投稿ユーザーをリクエストユーザーと紐付け"""
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    
    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        
        subject = 'お問い合わせ: {}'.format(title)
        message = \
            '送信者名: {0}\nメールアドレス: {1}\n タイトル:{2}\n メッセージ:\n{3}' \
                .format(name, email, title, message)
        from_email = 'moveunderstand002@gmail.com'
        to_list = ['moveunderstand002@gmail.com']
        message = EmailMessage(subject=subject,
                                body=message,
                                from_email=from_email,
                                to=to_list,
                                )
        message.send()
        messages.success(
            self.request, 'お問い合わせは正常に送信されました。')
        return super().form_valid(form)
    
    
class Home(LoginRequiredMixin, ListView):
    """HOMEページで、自分以外のユーザー投稿をリスト表示"""
    model = Post
    template_name = 'index.html'

    def get_queryset(self):
        #リクエストユーザーのみ除外
        return Post.objects.exclude(user=self.request.user)
        
    
class MyPost(LoginRequiredMixin, ListView):
    """自分の投稿のみ表示"""
    model = Post
    template_name = 'index.html'

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)