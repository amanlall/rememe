from restframework import serializers
from blog.models import Post

class BlogSerializers(serializers.ModelSerializers):
    class Meta:
        model = Postsfiles= ['title' , 'image'] 