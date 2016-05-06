import re

from django import forms
from django.conf import settings
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from django_countries import countries
from django_countries.fields import LazyTypedChoiceField

RE_PUBLIC_ID = re.compile(r'^[cbdefghijklnrtuv]{12}$')
RE_TOKEN = re.compile(r'^[cbdefghijklnrtuv]{32,64}$')

# Multi mode (default = False)
YUBICO_MULTI_MODE = getattr(settings, 'YUBICO_MULTI_MODE', False)

# How many OTPs user needs to enter when multi mode is enabled
YUBICO_MULTI_NUMBER = getattr(settings, 'YUBICO_MULTI_NUMBER', 3)

STYLE = ''''background:url("/site_media/images/yubiright_16x16.gif") no-repeat
scroll 2px 2px white; padding-left:20px;'''
PASSWORD_INPUT_WIDGET_ATTRS = {'style': STYLE}


class RegisterForm(forms.Form):
    email = forms.EmailField(label=_('Email'),
                             widget=forms.EmailInput(),
                             required=True)
    username = forms.CharField(label=_('Username'),
                               required=True)
    firstname = forms.CharField(label=_('Firstname'),
                                required=True)
    lastname = forms.CharField(label=_('Lastname'),
                               required=True)
    password = forms.CharField(label=_('Password'),
                               widget=forms.PasswordInput(),
                               required=True)
    address = forms.CharField(label=_('Address'),
                              required=True)
    additional_info = forms.CharField(label=_('Additional Info'))
    country = LazyTypedChoiceField(label=_('Country'),
                                   choices=countries)
    citizen = LazyTypedChoiceField(label=_('Citizenship'),
                                   choices=countries)

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.email = None
        self.username = None
        self.password = None
        self.firstname = None
        self.lastname = None
        self.address = None
        self.additional_info = None

    def clean(self):
        return self.cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(label=_('Username'))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user = None

        min_length = 34
        max_length = 64

        if not YUBICO_MULTI_MODE:
            widget = forms.PasswordInput(attrs=PASSWORD_INPUT_WIDGET_ATTRS)
            self.fields['otp'] = forms.RegexField(label=_('OTP'),
                                                  widget=widget,
                                                  regex=RE_TOKEN,
                                                  min_length=min_length,
                                                  max_length=max_length)
        else:
            for index in range(0, YUBICO_MULTI_NUMBER):
                label = _('OTP %d' % (index + 1))
                widget = forms.PasswordInput(attrs=PASSWORD_INPUT_WIDGET_ATTRS)

                field = forms.RegexField(label=label, widget=widget,
                                         regex=RE_TOKEN,
                                         min_lengtCh=min_length,
                                         max_length=max_length)
                self.fields['otp_%d' % index] = field

    def clean(self):
        username = self.cleaned_data.get('username')

        otp_list = []
        if not YUBICO_MULTI_MODE:
            otp = self.cleaned_data.get('otp')
            otp_list.append(otp)
        else:
            for index in range(0, YUBICO_MULTI_NUMBER):
                otp = self.cleaned_data.get('otp_%d' % index)
                otp_list.append(otp)

        if username and otp_list:
            self.user = authenticate(username=username, otp=otp_list)

        if self.user is None:
            raise forms.ValidationError(_('The provided OTP is invalid.'))

        return self.cleaned_data


class PasswordForm(forms.Form):
    password = forms.CharField(label=_('Password'),
                               widget=forms.PasswordInput(),
                               required=True)

    def __init__(self, *args, **kwargs):
        self.user = kwargs['user']
        del(kwargs['user'])
        super(PasswordForm, self).__init__(*args, **kwargs)

    def clean_password(self):
        password = self.cleaned_data['password']

        if not self.user.check_password(password):
            msg = _('The provided password is incorrect')
            raise forms.ValidationError(msg)
