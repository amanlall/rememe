from PIL import Image
from django import forms
from django.core.files import File
from .models import Post
from datetime import datetime
#from . models import Comments
import os

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)


class PostPhotoForm(forms.ModelForm):

    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = Post
        fields = ('image', 'x', 'y', 'width', 'height','title' )
        
    def __init__(self, *args, **kwargs):
        super(PostPhotoForm, self).__init__(*args, **kwargs)
    
    


    def save(self):
        photo = super(PostPhotoForm, self).save()
        
        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')
        t = self.cleaned_data.get('title')
        
        print("------------------------------++++---------------------------------")
        print(x)
        print(y)
        print(w)
        print(h)
        print(t)
        print("------------------------------++++---------------------------------")
        print(photo.image)
        img = Image.open(photo.image)
        print("img = Image.open(photo.image)")
        print(img)
        cropped_image = img.crop((x, y, w+x, h+y))
        print("cropped_image = img.crop((x, y, w+x, h+y))")
        print(cropped_image)
        #resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
        #print("resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)")
        #print(resized_image)
        cropped_image.save(photo.image.path)
        print("photo.image.path")
        print(photo.image.path)
        #now = datetime.now()
        #current_time = now.strftime("%H%M%S")
        #new_name= "rememe_"+str(current_time)+ "_" +t
        #print(new_name)
       # os.rename(cropped_image.path.url, new_name )
        

        #img.save(photo.image.path)
        #print(resized_image)

        return photo


'''
class CommentForm(forms.ModelForm):
    content= forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':'text goes here', 'rows': '4', 'cols':'50'}))
    class Meta:
        model=Comments
        fields=['content',]'''