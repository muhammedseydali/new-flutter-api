from rest_framework import fields, serializers
from .models import account

    
    
class UserRegister(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    profile_picture = serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model = account
        fields = ['id','full_name','phone_number','email','dob','profile_picture','password','password2']
        extra_kwargs = {
            'password' : {'write_only':True}
        }
    
    # def create(self,validated_data):
    #     password = validated_data.pop('password',None)
    #     instance = self.Meta.model(**validated_data)
    #     if password is not None:
    #         instance.set_password(password)
    #     instance.save()
    #     return instance
    
    
    def save(self):
        reg = account(
            email=self.validated_data['email'],
            phone_number=self.validated_data['phone_number'],
            dob=self.validated_data['dob'],
            full_name=self.validated_data['full_name'],
            profile_picture=self.validated_data['profile_picture'],
        )
        if account.objects.filter(phone_number=self.validated_data['phone_number']).exists():
            raise serializers.ValidationError({'error':'phone number already registered!!'})
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'error':'password does not match!!'})
        reg.set_password(password)
        reg.save()
        return reg
 
 
    
class UserDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=account
        fields=['id','full_name','phone_number','email','dob','profile_picture']