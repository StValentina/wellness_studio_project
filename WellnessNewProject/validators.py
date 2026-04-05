from django.core.validators import BaseValidator


class MaxFileSizeValidator(BaseValidator):
    message = "File size should be less than %(limit_value)s MB"
    code = "file_too_large"

    def clean(self, file):
        return file.size

    def compare(self, cleaned, limit_value):
        return cleaned > limit_value