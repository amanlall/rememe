from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
#from PIL import Image
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView)
from django.shortcuts import get_object_or_404    
from .forms import PostPhotoForm #, CommentForm
from PIL import Image
from users.models import Profile
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import render_to_string
# Create your views here.

'''
def home(request):
    context={
        'posts':Post.objects.all() 
    }
    return render(request,'index_new.html', context)
'''
from django.views.generic import TemplateView

'''
class MultipleModelView(TemplateView):
    template_name = 'index_new.html'
    
    ordering =[ '-date_posted']
    def get_context_data(self, **kwargs):
        context = super(MultipleModelView, self).get_context_data(**kwargs)
        pic_icon=[]
        verified=[]

        context['posts'] = Post.objects.all()
        return context
'''
def PostListView(request):
       
    pic=[]
    ver=[]
    is_liked=[]
    t_likes=[]
    p=Post.objects.all().order_by('-date_posted')
    print(p)
    
    i=1
    for i in range(len(p)):
        #form.append(comment_form)
        #comm.append(Comments.objects.filter(post=p[i],reply=None).order_by('-id'))
        pic.append(Profile.objects.filter(user_id=p[i].author_id)[0].image.url)
        ver.append(Profile.objects.filter(user_id=p[i].author_id)[0].verified)
        is_liked.append( p[i].likes.filter(id=request.user.id).exists())
        t_likes.append( p[i].total_likes())
    #print (p)
    #print (pic)
    #print (ver)
    context=list(zip(p,pic,ver,is_liked,t_likes))
    print(context)
    #comment_form=CommentForm()
    #context2= {
    #    'comment_form':comment_form,
    #    }
    #if request.is_ajax():
    #    html =render_to_string('blog/like_section.html', context, request=request)
    #    return JsonResponse({'form':html })     
    return render(request, 'index_new.html', {'context':context})


def PostDetailView(request,pk):
    p=Post.objects.filter(id=pk)
    pic=Profile.objects.filter(user_id=p[0].author_id)[0].image.url
    ver=Profile.objects.filter(user_id=p[0].author_id)[0].verified
    is_liked= p[0].likes.filter(id=request.user.id).exists()
    t_likes= p[0].total_likes()
    context2= {
            'p':p,
        'pic':pic,
         'ver': ver,
         "is_liked":is_liked,
         "t_likes":t_likes,

        }
    return render(request, 'blog/post_detail.html', {'context2':context2})

def RememerList(request):
    rm=Profile.objects.all().order_by('user_id')
    return render(request, 'blog/about.html', {'rm':rm})


class PostCreateView(LoginRequiredMixin, CreateView):
    model=Post
    fields=['image', 'title']
    def form_valid(self, form):
        
        form.instance.author=self.request.user

        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title', 'image']
    order=[ '-date_posted']
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post= self.get_object()
        print('*-**-***-*-**-**-*-*-*-*-*')
        print(post)
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model=Post
    success_url='/'
    def test_func(self):
        post= self.get_object()
       
        print(post)
        if self.request.user == post.author:
            return True
        return False


def contact(request):
    return render (request, 'blog/contact.html')

def sitemap(request):
    return render (request, 'sitemaps/sitemap.xml')    

@login_required
def ProfileDetailView(request,slugs):
    if request.method=='POST':
        u_form= UserUpdateForm(request.POST, instance=request.user)
        p_form= ProfileUpdateForm(request.POST, 
                                   request.FILES, 
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account updated')
            return redirect('blog-home')
    else:
        u_form= UserUpdateForm(instance=request.user)
        p_form= ProfileUpdateForm(instance=request.user.profile)             
    
    context= {
        'u_form':u_form,
         'p_form': p_form
        }
   
    users=User.objects.all()
    posts=Post.objects.all().order_by('-date_posted')
    profile=Profile.objects.all()
    memer_name=users.get(username=slugs)
    memer_id=memer_name.id
    memer_post_details=posts.filter(author_id=memer_id)
    memer_profile_details=profile.filter(user_id=memer_id)
    MDP=memer_profile_details.get().image.url
    MN=slugs
    NOP=len(memer_post_details)
    MPT=[]
    MPIU=[]
    MPDP=[]
    POSTid=[]

    for i in range(len(memer_post_details)):
        MPT.append(memer_post_details[i].title)
        MPIU.append(memer_post_details[i].image.url)
        MPDP.append(memer_post_details[i].date_posted)
        POSTid.append(memer_post_details[i].id)
    NOL=0
    for i in memer_post_details:
        NOL=NOL+ (i.total_likes())
    
    is_ver=Profile.objects.filter(user_id=memer_id)[0].verified
    #MPT.reverse()
    #MPIU.reverse()
    #MPDP.reverse()
    #POSTid.reverse()

    PDS=list(zip(MPT,MPIU,MPDP,POSTid))
    #print('*-**-***nno of posts, -*-**-**-*-*-*-*-*')
        #for i in range(len(memer_post_details)):
    #print(PDS)
        #print(memer_profile_details.username)
    #print('*-**-***-*-**-**-*-*-*-*-*')
    return render (request, 'users/meme.html', {'PDS':PDS,'NOL':NOL, 'NOP':NOP,'MDP':MDP,'slugs':slugs, 'is_ver':is_ver ,'context':context})



@login_required
def photo_list(request):
    if request.method == 'POST':
        form = PostPhotoForm(request.POST,request.FILES)
        print(request.FILES)     
        form.instance.author=request.user   
        if form.is_valid():
            form.save()
            return redirect('blog-home')
    else:
        form = PostPhotoForm()
    return render(request, 'blog/post_form.html', {'form': form})

@login_required
def like_post(request):
    post= get_object_or_404(Post, id=request.POST.get('id'))
    is_liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked=False
    else:
        post.likes.add(request.user)
        is_liked=True

    context={
       'post':post,
       'is_liked' : is_liked,                    
       't_likes' : post.total_likes(),
    }
    if request.is_ajax():
        html =render_to_string('blog/like_section.html', context, request=request)
        return JsonResponse({'form':html })

'''
def comment_post(request):
    if request.method=='POST':
        post= get_object_or_404(Post, id=request.POST.get('id'))
        print(post)
        comment_form=CommentForm(request.POST or None)
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print(comment_form)
        content =request.POST.get('content')
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print(content)
        post=request.POST.get('comment_on_post_id')
        reply_id= request.POST.get('c_id')
        comment_qs=None
        if reply_id:
            comment_qs= Comments.objects.create(post=post,usr=request.user.id,content=content, reply=comment_qs)
        comment=Comments.objects.create(post=post, usr=request.user, content=content)
        print(comment)
        if comment_form.is_valid():
            comment.save()
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print(done)

'''