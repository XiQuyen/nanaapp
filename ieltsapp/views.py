from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views import generic
from django.views.generic.list import BaseListView
from .forms import AuthorForm, BookForm, ArticleForm, NameForm, ContactForm, ColorfulContactForm
from django.utils import timezone
from django.utils import six
from django.http import HttpResponse
from django.template import loader, Context
from django.template import Template
from datetime import datetime
from ieltsapp import search as NaSearch
from ieltsapp.models import Book, Author
from ieltsapp.forms import PostForm
from ieltsapp.view_data.posts import *
from ieltsapp.view_data.css import *
from ieltsapp.view_data.search import *

# Manage->Settings->URL->VIEWS->TEMPLATES
# USING MODEL AND CSS and DATABASE

class SearchView(SearchMixin, generic.ListView):
    """View that performs a search and returns the search results."""
    template_name = "search_results.html"

class SearchApiView(SearchMixin, BaseListView):
    """A JSON-based search API."""

    def render_to_response(self, context, **response_kwargs):
        """Renders the search results to the response."""
        content = json.dumps({
            "results": [
                {
                    "title": result.title,
                    "description": result.description,
                    "url": result.url,
                    "meta": result.meta,
                } for result in context[self.get_context_object_name(self.get_queryset())]
            ]
        }).encode("utf-8")
        # Generate the response.
        response = HttpResponse(content, **response_kwargs)
        response["Content-Type"] = "application/json; charset=utf-8"
        response["Content-Length"] = len(content)
        return response

# Older function-based views.

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):	
        return render(request, 'index.html', context=None)

# Add this view
#class AboutPageView(TemplateView):
def AboutPageView(request):
    from ieltsapp.view_data.about import NaAboutDataView
    data = NaAboutDataView()
    return render(request, "about.html", {'user':self.data.user,
	                                      'text':self.data.text,  
										  'n'   : range(len(self.data.array1)),
										  'array1':self.data.array1, 
										  'link':self.data.link, 
										  'array2':self.data.array2, 
										  'link2':self.data.link2})
	

# Add this view
class ReadingPageView(TemplateView):
    from ieltsapp.view_data.reading import NaReadingDataView
    template_name = "reading.html"    
    data = NaReadingDataView()
    def get_context_data(self, **kwargs):
        context = super(ReadingPageView, self).get_context_data(**kwargs)
        context.update({'var1': self.data.var1, 'var2': self.data.var2, 'list': self.data.paragraph[0], 'data': self.data.data, 'keywords': self.data.keywords})
        return context
	
# Add this view
class WritingPageView(TemplateView):
    from ieltsapp.view_data.writing import NaWritingDataView
    template_name = "writing.html"
    data = NaWritingDataView()
    def get_context_data(self, **kwargs):
        context = super(WritingPageView, self).get_context_data(**kwargs)
        context.update({'part1': self.data.part1, 'part2': self.data.part2, 'part3': self.data.part3, 'list': self.data.paragraph[0], 'data': self.data.data, 'keywords': self.data.keywords})
        return context
	
# Add this view
class ContactPageView(TemplateView):
    template_name = "contact.html"
    var1 = 0
    var2 = 1
    def get_context_data(self, **kwargs):
        context = super(ContactPageView, self).get_context_data(**kwargs)
        context.update({'var1': self.var1, 'var2': self.var2})
        return context	
	
# Add this view
class SpeakingPageView(TemplateView):
    from ieltsapp.view_data.speaking import NaSpeakingDataView
    template_name = "speaking.html"
    data = NaSpeakingDataView()
    def get_context_data(self, **kwargs):
        context = super(SpeakingPageView, self).get_context_data(**kwargs)
        context.update({'part1': self.data.part1, 'part2': self.data.part2, 'part3': self.data.part3})
        return context	
	
# Add this view
class ListeningPageView(TemplateView):
    from ieltsapp.view_data.listening import NaListeningDataView
    template_name = "listening.html"
    data = NaListeningDataView()
    def get_context_data(self, **kwargs):
        context = super(ListeningPageView, self).get_context_data(**kwargs)
        context.update({'section1': self.data.section1, 'section2': self.data.section2, 'section3': self.data.section3, 'section4': self.data.section4})
        return context	
	

class Template:
    def __init__(self, template):
        self.template = template

    def render(self, context=None, request=None):
        if context is None:
            context = {}
        if request is not None:
            context['request'] = request
            context['csrf_input'] = csrf_input_lazy(request)
            context['csrf_token'] = csrf_token_lazy(request)
        return self.template.render(context)
		


def current_datetime(request):
    now = datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    # My first name is {{ first_name }}. My last name is {{ last_name }}.
    return HttpResponse(html)

def user_profile_page(request, username=None): 
    #users = {}  
    #users['lenguyen'] = "Le Nguyen"   
    #users['hihi'] = "Tram Le"    
    #users['huhu'] = "Le Nguyen"    
    #users['hoho'] = "Le Nguyen"    
    #users['hehe'] = "Le Nguyen" 
    #html = "<p>You're looking at user %s.</p>" % username
    #html= html + "<p> </p>"
    #html= html + "<li><a href=""/"">Go back home</a>"
    #return HttpResponse(html)
    
    #response = HttpResponse()
    #response.write("<p>Here's the text of the Web page %s.</p>" % username)
    #return response
    #return render(request, "profile.html", {'username':username})
    authors = Author.objects.all()
    return render(request, 'blog/author_list.html', {'authors': authors})

def index(request, question_id):
    return HttpResponse("You're looking at date %s." % question_id)

def tim_kiem():
    html = []	
    html.append("<div class=""book_container"">")    
    html.append("</div>")
    return html

def sach_moi_dang():
    html = []	
    html.append("<div class=""book_container"">")    
    html.append("</div>")
    return html

def dong_dau():
    html = []	
    html.append("<div class=""book_container"">")    
    html.append("</div>")
    return html

def dan_ma_vach():
    html = []	
    html.append("<div class=""book_container"">")    
    html.append("</div>")
    return html

def mota_tailieu():
    html = []	
    html.append("<div class=""book_container"">")    
    html.append("</div>")
    return html

def phanloai_tailieu():
    html = []	
    html.append("<div class=""book_container"">")    
    html.append("</div>")
    return html

def bosung_tailieu():
    html = []	
    html.append("<div class=""book_container"">")    
    html.append("</div>")
    return html

def baocao_tailieumoi():
    html = []	
    html.append("<div class=""book_container"">")    
    html.append("</div>")
    return html

def baocao_tailieu_phobien():
    html = []	
    html.append("<div class=""book_container"">")    
    html.append("</div>")
    return html

def danhgia_chung():
    html = []	
    html.append("<div class=""book_container"">")    
    html.append("</div>")
    return html

def lap_ke_hoach():
    html = []	
    html.append("<div class=""book_container"">")    
    html.append("</div>")
    return html

def bao_cao_tai_chinh():
    html = []	
    html.append("<div class=""book_container"">")    
    html.append("</div>")
    return html

def du_toan():
    html = []	
    html.append("<div class=""book_container"">")    
    html.append("</div>")
    return html

def hach_toan():
    html = []	
    html.append("<div class=""book_container"">")    
    html.append("</div>")
    return html

def post_detail_voca(voca, explaination):
    html = []
    html.append("<dl>")
    html.append("<dt>%s</dt>" % voca)
    html.append("<dd>%s</dd>" % explaination)
    html.append("<dt>%s</dt>" % voca)
    html.append("<dd>%s</dd>" % explaination)
    html.append("</dl>")
    return html

def post_detail_header(book_name, book_short_info):
    html = []	
    html.append("<div class=""book_container"">")
    html.append("<p class=""p_book_title"">%</p>" % book_name)
    html.append("<p>class=""p_book_detail""%</p>" % book_short_info)	
    html.append("</div>")
    return html
def post_detail(request, user_id=None):
    users = {}    
    users['500'] = "Le Nguyen"
    users['400'] = "Trinh Truong"
    users['300'] = "Ha Tran"
    users['200'] = "Vu Dao"
    users['100'] = "Tram Le"
    # Rest of the method
    text = request.GET.get('text')
    published_date = request.GET.get('published_date')
    response = HttpResponse()
    go_home(response)
    response.write("<div class=""floating-content"">")
    response.write("<p>I never thought that she has many thing to do like that and I am sorry about what she  </p>")
    response.write("<div class=""floating-inside"">")
    response.write("<p>read book </p>")
    response.write("</div>")
    response.write("<div class=""floating-inside"">")
    response.write("<p>read book </p>")
    response.write("</div>")
    response.write("<div class=""floating-inside"">")
    response.write("<p>read book </p>")
    response.write("</div>")
    response.write("<div class=""floating-inside-clear"">")
    response.write("</div>")
    response.write("</div>")
    response.write("<div class=""floating-box"">")
    response.write("<p>This is the message from %s.</p>" % users[user_id])
    response.write("<p>On the date %s.</p>" % published_date)
    response.write("<p>With the message %s.</p>" % text)
    response.write("<form action=""/vote/100/"" method=""get"">")
    response.write("<input type=""submit"" value=""Continue..."">")
    response.write("</form>")
    response.write("</div>")	
    response.write("<div class=""floating-box"">")
    response.write("<p>Skill become every year </p>")
    response.write("</div>")
    response.write("<div class=""floating-box"">")
    response.write("<p>continue learning </p>")
    response.write("</div>")
    response.write("<div class=""floating-box"">")
    response.write("<p>read book </p>")
    response.write("</div>")
    response.write("<div class=""floating-box"">")
    response.write("<p>read sixty minutes a day </p>")
    response.write("<p>comment| rating</p>")
    response.write("</div>")
    response.write("<div class=""floating-box"">")
    response.write("<p>center </p>")
    response.write("<p>comment| rating</p>")
    response.write("</div>")
    response.write("<div class=""floating-box"">")
    response.write("<p>center </p>")
    response.write("<p>comment| rating</p>")
    response.write("</div>")
    response.write("<div class=""floating-box"">")
    response.write("<p>center </p>")
    response.write("<p>comment| rating</p>")
    response.write("</div>")
    response.write("<div class=""floating-box"">")
    response.write("<p>center </p>")
    response.write("</div>")
    response.write("<div class=""floating-clear"">")
    response.write("<p> </p>")
    response.write("</div>")	
    response.write("<table style=""width:100%"">")
    books = []
    book =["Cho den mau giao thi da muon", "Smith", "Day la mot quyen sach hay danh cho cac quy phu huynh dang co con em o do tuoi chua di hoc" ]
    books.append(book)
    book =["Lam nhu choi", "Minh niem", "Mot quyen sach thay doi quan niem song cua moi nguoi va tu do moi nguoi co cach nhin khac ve cong viec minh dang lam. Hay tran trong tinh yeu danh cho gia dinh va doi xu tot voi ban than minh" ]
    books.append(book)
    book =["Lam nhu choi", "Minh niem", "Mot quyen sach thay doi quan niem song cua moi nguoi va tu do moi nguoi co cach nhin khac ve cong viec minh dang lam. Hay tran trong tinh yeu danh cho gia dinh va doi xu tot voi ban than minh" ]
    books.append(book)
    book =["Lam nhu choi", "Minh niem", "Mot quyen sach thay doi quan niem song cua moi nguoi va tu do moi nguoi co cach nhin khac ve cong viec minh dang lam. Hay tran trong tinh yeu danh cho gia dinh va doi xu tot voi ban than minh" ]
    books.append(book)
    book =["Lam nhu choi", "Minh niem", "Mot quyen sach thay doi quan niem song cua moi nguoi va tu do moi nguoi co cach nhin khac ve cong viec minh dang lam. Hay tran trong tinh yeu danh cho gia dinh va doi xu tot voi ban than minh" ]
    books.append(book)
    response.write("<tr>")
    response.write("<th>Name</th>")
    response.write("<th>Author</th> ")
    response.write("<th>About</th>")
    response.write("</tr>")
    for book in books:
        response.write("<tr>")
        response.write("<td>%s</td>" % book[0])
        response.write("<td>%s</td>" % book[1])
        response.write("<td>%s</td>" % book[2])
        response.write("</tr>")
    response.write("</table>")
    response.write("<div class=""floating-clear"">")
    response.write("<p> </p>")
    response.write("</div>")
    go_home(response)
    return response
    #return HttpResponse("You're looking at date %s %s." % (user_id, message))
	#---------------------------------------------------------
    #post = get_object_or_404(Post, user_id=user_id)
    #post.published_date = request.GET.get('published_date')
    #post.title = request.GET.get('title')
    #template = loader.get_template('my_template.html')
	#---------------------------------------------------------    
	#template = Template("My name is {{ my_name }} on the date {{ my_date }} with {{ my_text}}.")
    #context = Context({"my_name": user_id}, {"my_date": published_date}, {"my_text": text})
    #return HttpResponse(template.render(context))
    #return render(request, 'post_detail.html', {'post': post})
def quan_ly_nhan_su():
    html = []	
    html.append("<div class=""book_container"">")    
    html.append("</div>")
    return html
def quan_ly_tai_chinh():
    html = []	
    html.append("<div class=""book_container"">") 	
    html.append("doanh so") 	
    html.append("gia von")     
    html.append("</div>")
    return html
def quan_ly_nghiep_vu():
    html = []	
    html.append("<div class=""book_container"">")    
    html.append("luan chuyen") 	
    html.append("luan chuyen") 	
    html.append("</div>")
    return html
def quan_ly_co_so_vat_chat():
    html = []	
    html.append("<div class=""book_container"">")    
    html.append("</div>")
    return html

def book_detail(request, book_id=None):
    #html = ""
    #response = HttpResponse()
    #response.write(html) 
    #books = Book.objects..filter(publisher__name='BaloneyPress').order_by('name')
    books = Book.objects.all()
    return render(request, 'blog/book_list.html', {'books': books, 'book_id':book_id})
def vote_detail(request, user_id=None):
    users = {}    
    users['500'] = quan_ly_nhan_su()
    users['400'] = quan_ly_tai_chinh()
    users['300'] = quan_ly_nghiep_vu()
    users['200'] = quan_ly_co_so_vat_chat()
    nccs = []   
    ncc =["Chi", "", ""]
    nccs.append(ncc)  
    ncc =["Tan", "0938 946 938", "tanduong.tta@gmail.com"]
    nccs.append(ncc)
    response = HttpResponse() 
    go_home(response)
    now = datetime.now()
    htmls = users[user_id] 
    html_child = "You're looking at date %s." % user_id
    html = "<html><body><p style=""color:rgb(255,0,0);"">It is now %s. %s </p></body></html>" % (now, html_child)
    response.write(html)
    go_home(response)
    for html in htmls:	        	
        response.write(html)
    for ncc in nccs:	 
        html = ""	
        response.write(html) 
    return response
    
def add_post_edit(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

def add_author_edit(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():

            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('victory')
    else:
        form = AuthorForm()

    return render(request, "author.html", {'form': form})

def add_people(request, firstname, lastname):
    return HttpResponse("You're looking at question %s %s." % (firstname,lastname))
	
def add_wiki_edit(request):
    wikiform = WikiForm()
    template = loader.get_template('base.html', wikiform)
    context = RequestContext(request, {})

    return HttpResponse(template.render(context))
	
def view_question(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
'''	
def render_detail(request, question_id):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    latest_question_list = [id, text]
    template = loader.get_template('render.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
'''	
def book_review(request, book_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % book_id)
	
def view_results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def view_vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def search(request, **kwargs):
    """Renders a page of search results."""
    return SearchView.as_view(**kwargs)(request)

def search_json(request, **kwargs):
    """Renders a JSON representation of matching search entries."""
    return SearchApiView.as_view(**kwargs)(request)
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = ContactForm()
    return render(request, 'home.html', {'form': form})
def listening(request, topic_id):
    response = "You're listening topic %s."
    return HttpResponse(response % topic_id)
def speaking(request, topic_id):
    response = "You're speaking at the results of question %s."
    return HttpResponse(response % topic_id)
def reading(request, topic_id):
    response = "You're reading at the results of question %s."
    return HttpResponse(response % topic_id)
def writing(request, topic_id):
    response = "You're writing at the results of question %s."
    return HttpResponse(response % topic_id)