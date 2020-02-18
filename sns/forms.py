from django import forms
from .models import Message,Group,Friend,Good
from django.contrib.auth.models import User

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['owner','group','content']

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['owner','title']

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['owner','user','group']

class GoodForm(forms.ModelForm):
    class Meta:
        model = Good
        fields = ['owner','Message']

class SearchForm(forms.Form):
    class Meta:
        search = forms.CharField(max_length=100)

class GroupCheckForm(forms.Form):
    def __init__(self,user,*args,**kwargs):
        super(GroupCheckForm,self).__init__(*args,**kwargs)
        public = User.objects.filter(username='public').first()
        self.fields['groups'] =　forms.MultipleChoiceField(choice=[(item.title,item.title) for item in\
                Group.objects.filter(owner__in=[user,public])],widget=forms.CheckboxselectMultiple(),)

class GroupSelectForm(forms.Form):
    def __init__(self,user,*args,**kwargs):
        super(GroupCheckForm,self).__init__(*args,**kwargs)
        self.fields['groups'] =　forms.ChoiceField(choice=[('-','-')+[(item.title,item.title)\
                for item in Group.objects.filter(owner=user)],)

class FriendsForm(forms.Form):
    def __init__(self,user,friend=[],vals,*args,**kwargs):
        super(FriendsForm,self).__init__(*args,**kwargs)
        self.fields['friends'] =forms.MultipleChoiceField(choices=[(item.user,item.user) for item in friends],
        widget=forms.CheckboxselectMultiple(),
        initial = vals
        )
class CreateGroupForm(forms.Form):
    group_name = form.CharField(max_length=50)

class PostForm(forms.Form):
    content = forms.CharField(max_length=500,\
            widget = forms.Textarea)

    def __init__(self,user,*args,**kwargs):
        super(PostForm,self).__init__(*args,**kwargs)
        public = User.objects.filter(username='public').filter()
        self.fields['group'] = forms.ChoiceField(choice=[('-','-')]+[item.title,item.title\
                for item in Group.objects. \
                filter(owner__in=[user,public])],
        )
