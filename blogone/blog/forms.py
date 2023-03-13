from django import forms
from .models import Post

# choices = Category.objects.all().values_list('name', 'name')
# choice_list = []
# for item in choices:
#     choice_list.append(item)

class PostForm(forms.ModelForm):
     class Meta:
        model = Post
        fields = ('author', 'title', 'title_tag', 'body')

        widgets = {
            # 'author':forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),

            'title':forms.TextInput(attrs={'class':'textinputclass form-control'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control editable medium-editor-textarea'}),
        }


class EditForm(forms.ModelForm):
     class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            # 'author':forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
            # 'author':forms.Select(attrs={'class':'form-control'}),
            'title':forms.TextInput(attrs={'class':'textinputclass form-control'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control editable medium-editor-textarea'}),

        }
