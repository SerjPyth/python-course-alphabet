from django.views.generic import CreateView
from .models import Comment
from .forms import CommentForm
from django.urls import reverse
from article.models import Article


class CommentCreateView(CreateView):

    model = Comment
    template_name = 'comments/add_comment.html'
    form_class = CommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.comment = form.cleaned_data.get('comment')
        if self.request.user.is_authenticated:
            author = self.request.user.username
            comment.author = author
        article_id = self.kwargs['article_id']
        article = Article.objects.get(pk=article_id)
        comment.article = article
        comment.save()
        return super(CommentCreateView, self).form_valid(form)

    def get_context_data(self):
        context = super(CommentCreateView, self).get_context_data()
        context['article_id'] = self.kwargs['article_id']
        return context

    def get_success_url(self):
        article_id = self.kwargs['article_id']
        return reverse('detail', args=(article_id,))

    def get_form_kwargs(self):
        kwargs = super(CommentCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class CommentToCommentView(CreateView):

    model = Comment
    template_name = 'comments/reply_to_comment.html'
    form_class = CommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.comment = form.cleaned_data.get('comment')
        if self.request.user.is_authenticated:
            author = self.request.user.username
            comment.author = author
        article_id = self.kwargs['article_id']
        article = Article.objects.get(pk=article_id)
        comment.article = article
        parent_id = self.kwargs['comment_id']
        comment.parent_id = parent_id
        comment.save()
        return super(CommentToCommentView, self).form_valid(form)

    def get_context_data(self):
        context = super(CommentToCommentView, self).get_context_data()  # Empty dict
        context['comment_id'] = self.kwargs['comment_id']
        context['article_id'] = self.kwargs['article_id']
        return context

    def get_success_url(self):
        article_id = self.kwargs['article_id']
        return reverse('detail', args=(article_id,))

    def get_form_kwargs(self):
        kwargs = super(CommentToCommentView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
