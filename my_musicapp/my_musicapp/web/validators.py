from django.core import exceptions


def validate_name_chatracters(value):
    for ch in value:
        if not ch.isdigit() and not ch.isalpha() and not ch == "_":
        # if not ch.isalnum() and ch != '_':

            raise exceptions.ValidationError('Ensure this value contains only letters, numbers, and underscore.')