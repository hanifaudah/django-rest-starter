from rest_framework import serializers
from .models import Account
from django.contrib.auth.hashers import make_password

# utils
from etc.utils import validate_password

class AccountSerializer(serializers.ModelSerializer):
  class Meta:
    model = Account
    fields = [
      'id',
      'username',
      'email',
      'password',
      'date_joined',
      'last_login',
      'is_staff',
    ]

    read_only_fields = [
      'id',
      'date_joined', 
      'last_login',
      'is_staff'
    ]

    extra_kwargs = {
      'password': {
        'write_only': True
      }
    }

  def create(self, validated_data):
      validated_data['password'] = make_password(validated_data.get('password'))
      return super(AccountSerializer, self).create(validated_data)

  def validate(self, data):
      # validate password
      password_str = data['password']
      password_is_valid = validate_password(password_str)
      if not password_is_valid:
          raise serializers.ValidationError("password does not meet requirements")
      return data