from django import forms
from comments.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ('pub_date',)
        labels = {
            'author': 'What`s your name?',
        }
        widgets = {
            'parent_id': forms.HiddenInput(),
            'article': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(CommentForm, self).__init__(*args, **kwargs)
        if self.request.user.is_authenticated:
            self.fields['author'].required = False
            self.fields['article'].required = False
            self.fields['parent_id'].required = False
            self.fields['author'].widget = forms.HiddenInput()
        else:
            self.fields['author'].required = True
            self.fields['article'].required = False
            self.fields['parent_id'].required = False


