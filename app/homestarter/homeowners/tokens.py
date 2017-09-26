from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six


# Create a unique token generator to confirm email addresses.
class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
	def _make_hash_value(self, user, timestamp):
		return (six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.homeowner.email_confirmed))

account_activation_token = AccountActivationTokenGenerator()
