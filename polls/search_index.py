from polls.models import Question,Choice,Comment,Post

class ChoiceIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    choice_text =indexes.CharField(model_attr='choice_text')
    #votes = models.IntegerField(default=0,model_attr='votes')
    def get_model(self):
        return Choice
    def __str__(self):              # __unicode__ on Python 2
        return self.choice_text

class QuestionIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    question = indexes.CharField(model_attr='question_text')
    #comment = indexes.CharField(model_attr='comment')
    #pub_date = models.DateTimeField('date published')
    def get_model(self):
        return Question
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
    
class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    text1 = indexes.CharField(model_attr='text')
    #author = models.ForeignKey(User)
    def get_model(self):
        return Post
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        def __str__(self):
            return self.text+' - '+self.author.username                