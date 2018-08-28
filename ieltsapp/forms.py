from django import forms
from .models import Author, Book, Article, ModelPost
#from ieltsapp.questions.models import Answer, Question
from django.forms import ModelForm
'''
class AuthorForm(forms.Form):
    name = forms.CharField(max_length=100)
    title = forms.CharField(
        max_length=3,
        widget=forms.Select(choices=TITLE_CHOICES),
    )
    birth_date = forms.DateField(required=False)

class BookForm(forms.Form):
    name = forms.CharField(max_length=100)
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
'''
class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )
    source = forms.CharField(       # A hidden input for internal use
        max_length=50,              # tell from which page the user sent the message
        widget=forms.HiddenInput()
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')

class ColorfulContactForm(forms.Form):
    name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'style': 'border-color: blue;',
                'placeholder': 'Write your name here'
            }
        )
    )
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={'style': 'border-color: green;'})
    )
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(attrs={'style': 'border-color: orange;'}),
        help_text='Write here your message!'
    )
class UserSelectionForm(forms.Form):
    """form for selecting users"""
    def __init__(self, userlist, *args, **kwargs):
        self.custom_fields = userlist
        super(forms.Form, self).__init__(*args, **kwargs)
        for f in userlist:
            self.fields[str(f.id)] = forms.BooleanField(initial=False)    

    def get_selected(self):
        """returns selected users"""
        return filter(lambda u: self.fields[str(u.id)], self.custom_fields)
class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class ProfileForm(forms.Form):
    username = forms.CharField(label='User name', max_length=100)

class PostForm(forms.ModelForm):
    class Meta:
        model = ModelPost
        fields = ('title', 'text',)
	
class WikiForm(forms.Form):
    original = forms.Textarea()
    wikified = forms.Textarea()
    raw_html = forms.Textarea()


# or forms.ModelForm
class AuthorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MyModelForm, self).__init__(*args, **kwargs)
        self.fields["title"].min_length = 20
        self.fields["title"].validators.append(MinLengthValidator)
    class Meta:
        model = Author
        fields = ['name', 'title', 'birth_date']
        localized_fields = ('birth_date',)

# or forms.ModelForm
class BookForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MyModelForm, self).__init__(*args, **kwargs)
        self.fields["title"].min_length = 20
        self.fields["title"].validators.append(MinLengthValidator)
    class Meta:
        model = Book
        fields = ['name', 'authors']
		
# or forms.ModelForm
class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['pub_date', 'headline', 'content', 'reporter']
'''
class QuestionForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=255)
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        max_length=2000)

    class Meta:
        model = Question
        #fields = ['title', 'description', 'tags']
        fields = ['title', 'description']


class AnswerForm(forms.ModelForm):
    question = forms.ModelChoiceField(widget=forms.HiddenInput(),
                                      queryset=Question.objects.all())
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}),
        max_length=2000)

    class Meta:
        model = Answer
        fields = ['question', 'description']		
'''
