# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
from app.user.models import User


def jwt_identity(payload):
    return User.get_by_id(payload)


def identity_loader(user):
    return user.id
