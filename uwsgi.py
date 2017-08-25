#!/usr/bin/env python
# encoding: utf-8

"""
@author: wangyongxu
@software: PyCharm
@file: uwsgi.py
@time: 2017/8/25 下午5:06
"""

"""
WSGI config for kuosanyun project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BlogHugh.settings")

application = get_wsgi_application()
