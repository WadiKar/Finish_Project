
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View


class IndexView(View):

    def get(self, request):
        return render(request, 'klu')





















#i diodać image do modelsów żeby ozna było wstaawić zdjecie ksiązki i audiobooka

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
#                 bio = request.POST['bio']
#                 location = request.POST['location']
#
#                 user_profile.profileimg = image
#                 user_profile.bio = bio
#                 user_profile.location = location
#                 user_profile.save()
#             if request.FILES.get('image') != None:
#                 image = request.FILES.get('image')
#                 bio = request.POST['bio']
#                 location = request.POST['location']
#
#                 user_profile.profileimg = image
#                 user_profile.bio = bio
#                 user_profile.location = location
#                 user_profile.save()
#
#             return redirect('settings')
#         return render(request, 'settings.html', {'user_profile': user_profile})
