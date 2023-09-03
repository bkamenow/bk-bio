from django.shortcuts import render
from django.views import View


class HomeView(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)


class AboutMeView(View):
    template_name = 'about_me.html'

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)


class MyJourneyView(View):
    template_name = 'my_journey.html'

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)


class SkillsView(View):
    template_name = 'skills.html'

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)


class WorkView(View):
    template_name = 'work.html'

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)


class ContactsView(View):
    template_name = 'contacts.html'

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)
