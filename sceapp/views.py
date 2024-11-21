from django.http import HttpResponse
from django.shortcuts import render
# django.views.generic.baseからListViewをインポート
from django.views.generic import ListView,DetailView
from .models import ScheduleManage
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage

class IndexView(ListView):
    '''トップページのビュー
    
    テンプレートのレンダリングに特化したTemplateviewを継承
    '''
    
    template_name = 'index.html'
    
    context_object_name = 'orderby_records'
    
    queryset = ScheduleManage.objects.order_by('-posted_at')
    
    paginate_by = 6
    
class SceDetail(DetailView):
    
    template_name = 'post.html'
    model = ScheduleManage
    
class HobbyViews(ListView):
    template_name = 'hobby.html'
    model = ScheduleManage
    context_object_name = 'hobby_records'
    queryset = ScheduleManage.objects.filter(
        category='hobby').order_by('-posted_at')
    paginate_by = 4
    
class StudyViews(ListView):
    template_name = 'study.html'
    model = ScheduleManage
    context_object_name = 'study_records'
    queryset = ScheduleManage.objects.filter(
        category='study').order_by('-posted_at')
    paginate_by = 4
    
class OtherViews(ListView):
    template_name = 'other.html'
    model = ScheduleManage
    context_object_name = 'other_records'
    queryset = ScheduleManage.objects.filter(
        category='other').order_by('-posted_at')
    paginate_by = 4
    
class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('sceapp:contact')
    
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