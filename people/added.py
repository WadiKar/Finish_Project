# #
# # # def signup(request):
# # #     if request.method == 'POST':
# # #         username = request.POST['username']
# # #         # jeśli żadania mają metodę POST kiedy uzytkownik jej szuka lub do niej wejdzie, to jest wywoływana za pomocą metody POST
# # #         username = request.POST['username']
# # #         email = request.POST['email']
# # #         password = request.POST['password']
# # #         password2 = request.POST['password2']
# # #
# # #         if password == password2:
# # #             if User.objects.filter(email=email).exists():
# # #                 messages.info(request, 'Email taken')
# # #                 return redirect('signup')
# # #             elif User.objects.filter(username=username).exists():
# # #                 messages.info(request, 'Username taken')
# # #                 return redirect('signup')
# # #             else:
# # #                 user = User.objects.create_user(username=username, email=email, password=password)
# # #                 user.save()
# # #                 # log user in and redirect to settings page
# # #                 user_login = auth.authenticate(username=username, password=password)
# # #                 auth.login(request, user_login)
# # #                 # create a Profile object for the new user
# # #                 user_model = User.objects.get(username=username)
# # #                 new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
# # #                 new_profile.save()
# # #                 return redirect('signup')  # było settings
# # #
# # #
# # #         else:
# # #             messages.info(request, 'Password Not Matching')
# # #             return redirect('signup')
# # #     else:
# # #         return render(request, 'base.html')
# # #
# # #
# # # class SigninView(View):
# # #     def get(self, request):
# # #         if request.method == 'POST':
# # #             username = request.POST['username']
# # #             password = request.POST['password']
# # #
# # #             user = auth.authenticate(username=username, password=password)
# # #
# # #             if user is not None:
# # #                 auth.login(request, user)
# # #                 return redirect('/')
# # #             else:
# # #                 messages.info(request, ' Invalid')
# # #                 return redirect('signin')
# # #
# # #         else:
# # #             return render(request, 'register.html')
# #
# #
# # #
# # # Jeszcze poziomo było tak :
# # # <div class="parent">
# # #   <strong class="inline1">
# # #     <a class="nav-link active" href="{% url 'register' %}">Worker</a>
# # # </strong>
# # #   <strong class="inline2">inline 2</strong>
# # #
# # # </div>
# #
# #
# # # migrations 0007
# # # # Generated by Django 4.1.3 on 2022-12-07 11:17
# # #
# # # from django.db import migrations, models
# # # import django.db.models.deletion
# # #
# # #
# # # class Migration(migrations.Migration):
# # #
# # #     dependencies = [
# # #         ('people', '0006_person_alter_patient_patient_delete_profile_and_more'),
# # #     ]
# # #
# # #     operations = [
# # #         migrations.AlterField(
# # #             model_name='company',
# # #             name='profile_com',
# # #             field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='people.person'),
# # #         ),
# # #         migrations.AlterField(
# # #             model_name='patient',
# # #             name='patient',
# # #             field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='people.company'),
# # #         ),
# # #         migrations.AlterField(
# # #             model_name='patient',
# # #             name='profile',
# # #             field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='people.person'),
# # #         ),
# # #         migrations.AlterField(
# # #             model_name='specialist',
# # #             name='profile_spec',
# # #             field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='people.person'),
# # #         ),
# # #     ]
# #
# #
# # migrations 0006
# # # Generated by Django 4.1.3 on 2022-12-07 11:10
# #
# # from django.db import migrations, models
# # import django.db.models.deletion
# # import uuid
# #
# #
# # class Migration(migrations.Migration):
# #
# #     dependencies = [
# #         ('people', '0005_remove_profile_id_user_alter_profile_id'),
# #     ]
# #
# #     operations = [
# #         migrations.CreateModel(
# #             name='Person',
# #             fields=[
# #                 ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
# #                 ('first_name', models.CharField(max_length=128)),
# #                 ('last_name', models.CharField(max_length=128)),
# #             ],
# #         ),
# #         migrations.AlterField(
# #             model_name='patient',
# #             name='patient',
# #             field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='people.company'),
# #         ),
# #         migrations.DeleteModel(
# #             name='Profile',
# #         ),
# #         migrations.AddField(
# #             model_name='company',
# #             name='profile_com',
# #             field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='people.person'),
# #         ),
# #         migrations.AddField(
# #             model_name='patient',
# #             name='profile',
# #             field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='people.person'),
# #         ),
# #         migrations.AddField(
# #             model_name='specialist',
# #             name='profile_spec',
# #             field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='people.person'),
# #         ),
# #     ]
# #
# #
# # migracja 0005
# # # Generated by Django 4.1.3 on 2022-12-06 15:12
# #
# # from django.db import migrations, models
# # import uuid
# #
# #
# # class Migration(migrations.Migration):
# #
# #     dependencies = [
# #         ('people', '0004_remove_company_profile_com_remove_patient_profile_and_more'),
# #     ]
# #
# #     operations = [
# #         migrations.RemoveField(
# #             model_name='profile',
# #             name='id_user',
# #         ),
# #         migrations.AlterField(
# #             model_name='profile',
# #             name='id',
# #             field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
# #         ),
# #     ]
# #
# #
# # migracja 0004
# # # Generated by Django 4.1.3 on 2022-12-06 15:06
# #
# # from django.db import migrations, models
# # import django.db.models.deletion
# #
# #
# # class Migration(migrations.Migration):
# #
# #     dependencies = [
# #         ('people', '0003_remove_company_employee_remove_profile_password_and_more'),
# #     ]
# #
# #     operations = [
# #         migrations.RemoveField(
# #             model_name='company',
# #             name='profile_com',
# #         ),
# #         migrations.RemoveField(
# #             model_name='patient',
# #             name='profile',
# #         ),
# #         migrations.RemoveField(
# #             model_name='specialist',
# #             name='profile_spec',
# #         ),
# #         migrations.AddField(
# #             model_name='profile',
# #             name='company',
# #             field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='people.company'),
# #             preserve_default=False,
# #         ),
# #         migrations.AddField(
# #             model_name='profile',
# #             name='patient',
# #             field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='people.patient'),
# #             preserve_default=False,
# #         ),
# #         migrations.AddField(
# #             model_name='profile',
# #             name='profile_spec',
# #             field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='people.specialist'),
# #             preserve_default=False,
# #         ),
# #     ]
#
#
# migracja 0003
# # Generated by Django 4.1.3 on 2022-12-05 21:20
#
# from django.db import migrations, models
#
#
# class Migration(migrations.Migration):
#
#     dependencies = [
#         ('people', '0002_rename_nemployee_company_employee'),
#     ]
#
#     operations = [
#         migrations.RemoveField(
#             model_name='company',
#             name='employee',
#         ),
#         migrations.RemoveField(
#             model_name='profile',
#             name='password',
#         ),
#         migrations.AddField(
#             model_name='company',
#             name='no_employee',
#             field=models.IntegerField(default=False),
#             preserve_default=False,
#         ),
#     ]
#
#
# migracja 0002
# # Generated by Django 4.1.3 on 2022-12-05 13:08
#
# from django.db import migrations
#
#
# class Migration(migrations.Migration):
#
#     dependencies = [
#         ('people', '0001_initial'),
#     ]
#
#     operations = [
#         migrations.RenameField(
#             model_name='company',
#             old_name='nemployee',
#             new_name='employee',
#         ),
#     ]


# class Profile(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     id_user = models.IntegerField()
#     bio = models.TextField(blank=True)
#     location = models.CharField(max_length=100, blank=True)
# class Person(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
#     first_name = models.CharField(max_length=128)
#     last_name = models.CharField(max_length=128)
#
#     def __str__(self):
#         return f"{self.id}"
#         # # def __str__(self):
#         #return self.user.username
#
# class Patient(models.Model):
#     first_name = models.CharField(max_length=128)
#     last_name = models.CharField(max_length=128)
#     learned_profession = models.CharField(max_length=128)
#     work_done = models.CharField(max_length=128)
#     company_name = models.ForeignKey('Company', on_delete=models.CASCADE, null=True, default = None)
#     email = models.CharField(max_length=128)
#     your_name = models.ForeignKey('Person', on_delete=models.CASCADE, null=True, default = None)
#
# class Company(models.Model):
#     name_company = models.CharField(max_length=256)
#     industry = models.CharField(max_length=128)
#     no_employee = models.IntegerField(blank=True, null =True)
#     profile_com = models.ForeignKey('Person', on_delete=models.CASCADE, null=True, default = None)
#
#
# class Specialist(models.Model):
#     full_name = models.CharField(max_length=128)
#     specialization = models.CharField(max_length=128)
#     description = models.CharField(max_length=256)
#     profile_spec = models.ForeignKey('Person', on_delete=models.CASCADE, null=True, default = None)


# formsy stare
# from django import forms
# from django.contrib.auth.models import User
# from wtforms import ValidationError
# import random as r
#
# from people.models import Specialist, Company, User, Person
# from people.models import Profile

# def random_number():
#     ph_no = []
#     ph_no.append(r.randint(6, 9))  # w zaleznosci kto kim jest
#
#     for i in range(1, 10):
#         ph_no.append(r.randint(0, 9))
#
#
# class ProfileAddForm(forms.Form):
#     user = forms.ModelChoiceField(queryset=User.objects.all(),widget=forms.RadioSelect)  # required=False nie bo bedziemy wybierac czy spec, czy firma
#     id_user = forms.IntegerField(validators=[random_number])
#     bio = forms.CharField(max_length=256)
#     location = forms.CharField(max_length=64)
#
#
# class PatientAddForm(forms.Form):
#     first_name = forms.CharField(max_length=128)
#     last_name = forms.CharField(max_length=128)
#     learned_profession = forms.CharField(max_length=128)
#     work_done = forms.CharField(max_length=128)
#     patient = forms.ModelChoiceField(queryset=Company.objects.all(), required=False)
#     email = forms.CharField(max_length=128)
#     person_patient = forms.ModelChoiceField(queryset=Person.objects.all(), required=False)
#     # profile = forms.ModelChoiceField(queryset=Profile.objects.all(), required=False)
#
# class CompanyAddForm(forms.Form):
#     name_company = forms.CharField(max_length=256)
#     industry = forms.CharField(max_length=128)
#     no_employee = forms.IntegerField()
#     person_company = forms.ModelChoiceField(queryset=Person.objects.all(), required=False)
#     # profile_com = forms.ModelChoiceField(queryset=Profile.objects.all(), required=False)
#
# class SpecialistAddForm(forms.Form):
#     full_name = forms.CharField(max_length=128)
#     specialization = forms.CharField(max_length=128)
#     description = forms.CharField(max_length=256)
#     person_specialist = forms.ModelChoiceField(queryset=Person.objects.all(), required=False)
#     # profile_spec = forms.ModelChoiceField(queryset=Profile.objects.all(), required=False)
#
# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=100, help_text=False)
#     password = forms.CharField(max_length=100, widget=forms.PasswordInput)
#
#
# class UserCreateForm(forms.ModelForm):
#     password = forms.CharField(max_length=120, widget=forms.PasswordInput)
#     password2 = forms.CharField(max_length=120, widget=forms.PasswordInput)
#     #profile = forms.ModelChoiceField(queryset=Profile.objects.all(), widget=forms.RadioSelect)
#
#     class Meta:
#         model = User
#         fields = ['username']
#
#     def clean(self):
#         cleaned_data = super().clean()
#         if cleaned_data['password'] != cleaned_data['password2']:
#             raise ValidationError('Hasła nie są takie same!!!')
#
#

#
# class AddReleaseView(PermissionRequiredMixin, View):
#     permission_required = ['media.add_release']
#
#     def post(self, request, Category_pk):
#         form = ReleaseAddForm(request.POST)
#         category = Category.objects.get(pk=Category_pk)
#         if form.is_valid():
#             release = form.save(commit=False)
#             release.category = category
#             release.author_specialist = request.user  #
#             release.save()
#             return redirect('detail_release', Category_pk)


# class SettingsView(LoginRequiredMixin, View):
#     login_url = '/signin/'
#     redirect_field_name = 'signin'
#
#     def get(self, request):
#         user_profile = Profile.objects.get(user=request.user)
#
#         if request.method == 'POST':
#
#             if request.FILES.get('image') is None:
#                 image = user_profile.profileimg
#                 location = request.POST['location']
#
#                 user_profile.profileimg = image
#                 user_profile.location = location
#                 user_profile.save()
#             if request.FILES.get('image') != None:
#                 image = request.FILES.get('image')
#                 location = request.POST['location']
#
#                 user_profile.profileimg = image
#                 user_profile.location = location
#                 user_profile.save()
#
#             return redirect('settings')
#         return render(request, 'settings.html', {'user_profile': user_profile})

# lisy2authors bylo wczesniej tak
# {% extends 'base.html' %}
# {% block content %}
#     <ul class="list-group">
#     {% for author in authors %}
#         <ul class="list-group-item"><a href="/authors/{{ author.id }}">
#             {{ author.title }}
#             {% for author in authors.all %}
#                 {{author.fullname}}
#             {% endfor %}
#         </a></ul>
#     {% endfor %}
#     </ul>
#
# {% endblock %}

# class AddBookView(UserPassesTestMixin, View):
#     def test_func(self):
#         return self.request.user.groups.filter(name='Specialist').exists()
#
#     def get(self, request):
#         form = BookAddForm()
#         return render(request, 'form.html', {'form': form})
#
#     def post(self, request):
#         form = BookAddForm(request.POST)
#         if form.is_valid():
#             title = form.cleaned_data['title']
#             year = form.cleaned_data['year']
#             authors = form.cleaned_data['authors']
#             categories = form.cleaned_data['categories']
#             Book.objects.create(title=title, year=year, authors=authors, categories=categories)
#             return redirect('/')
#         return render(request, 'form.html', {
#             'form': form})


#
# class BooksView(View):
#     def get(self, request, category=None):
#         choose_category = request.GET.get('category')
#         if choose_category != '':
#             ksiazki = Book.objects.filter(categories__id=choose_category).all()
#         else:
#
#             ksiazki = Book.objects.all()
#         categories = Category.objects.all()
#         return render(request, 'listy2books.html', {'books': ksiazki, 'categories': categories, 'choose_category': int(choose_category)if choose_category else None})


#             <!--            {% if request.user.is_specialist %}-->
# { % if request.user.is_specialist %}
# { % if perms.Portal.create_book
# ' %}-->


# {% if perms.media.view_book %}
#                         <div>
#                             <a class="nav-link" href="{% url 'view_audiobooks' %}">Audiobooks</a>
#                         </div>
#                         <div class="nav-item">
#                             <a class="nav-link" href="{% url 'view_release' %}">Posts</a>
#                         </div>
#                         <div class="nav-item">
#                             <a class="nav-link" href="{% url 'view_books' %}">Books</a>
#                         </div>
#
#                         <div class="nav-item">
#                             <a class="nav-link" href="{% url 'view_author' %}">Authors</a>
#                         </div>
#                         <div class="nav-item">
#                             <a class="nav-link" href="{% url 'view_specialist' %}">Specialist</a>
#                         </div>
#                         <div class="nav-item">
#                             <a class="nav-link" href="{% url 'make_appointment' %}">Make Appointment</a>
#                         </div>
#                         <div class="nav-item">
#                             <a class="nav-link" href="{% url 'detail_appointment' 1 %}">List Appointment</a>
#                         </div>
#                     {% endif %}

#
# < ul
# id = "pagi-slide"
# style = "padding-top: 80px; margin-top: -80px;"
#
#
# class ="toggle-view list" >
#
# < li >
# < div
#
#
# class ="product-container" >
#
# < div
#
#
# class ="product-image" style="position: relative;" > < / div >
#
# < div
#
#
# class ="product-main" >
#
# < div
#
#
# class ="product-main-top" > < / div >
#
# < div
#
#
# class ="product-main-bottom" > < / div >
#
# < / div >
# < / div >
# < / li >
# < / ul >

#
# from django.contrib.auth.models import User
# from django.db import models
# from django.contrib.auth import get_user_model
# from datetime import datetime
#
# # User = get_user_model()
#
# from django.contrib.auth.models import AbstractUser
#
#
# class User(AbstractUser):
#     company = models.ForeignKey('Company', related_name='Employees', null=True, on_delete=models.SET_NULL)
#
#     def is_specialist(self):
#         return self.groups.filter(name='Specialist').exists()
#     def is_company(self):
#         return self.groups.filter(name='Company').exists()
#
#
# class Company(models.Model):
#     name_company = models.CharField(max_length=256)
#     industry = models.CharField(max_length=64)
#     employees = models.ManyToManyField(User)
#
#     def __str__(self):
#         return self.name_company
#
#
# class Visit(models.Model):
#     what_time = models.DateTimeField()
#     location = models.CharField(max_length=128)
#     specialist = models.ForeignKey(User, related_name='Specialist', null=True, on_delete=models.SET_NULL)
#     patient = models.ForeignKey(User, related_name='Patient', null=True, on_delete=models.SET_NULL)
#
#     def __str__(self):
#         return f"{self.location, self.what_time.strftime('%Y-%m-%d %H:%M:%S')}"


class ContractAddForm(forms.Form):
    title = forms.CharField(max_length=458)
    contractor = forms.ModelChoiceField(queryset=TheContractor.objects.all(), widget=forms.RadioSelect)
    type = forms.ModelChoiceField(queryset=TypeProcurement.objects, widget=forms.RadioSelect)
    value_contract = forms.IntegerField()
    start_date = forms.DateField()
    end_date = forms.DateField()

    def clean(self):
        cleaned_data = super().clean()  ## wykorzystuje metody z min-year czy movieadd
        return cleaned_data


class Contract(models.Model):
    title = models.CharField(max_length=458)
    contractor = models.ManyToManyField('TheContractor', related_name="contract")
    value_contract = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    type = models.ForeignKey('TypeProcurement', on_delete=models.CASCADE)

    def __str__(self):
        return {self.title}

    @property
    def get_absolute_url(self):
        return reverse('detail_contract', args=(self.id))


class AddContractView(View):
    def get(self, request):
        form = ContractAddForm()

        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = ContractAddForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            contractor = form.cleaned_data['contractor']
            type = form.cleaned_data['type']
            value_contract = form.cleaned_data['value_contract']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            con = Contract.objects.create(title=title, type=type, value_contract=value_contract,
                                          start_date=start_date, end_date=end_date)
            con.contractor.set(contractor)
            return redirect('list_contract')
        return render(request, 'form.html', {'form': form})
