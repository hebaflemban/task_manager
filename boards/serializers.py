from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	class Meta:
		model = User
		fields = ['username', 'password']

	def create(self, validated_data):
        new_user = User(**validated_data)
		new_user.set_password(new_user.password)
		new_user.save()
		return validated_data


class BoardCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class BoardSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['title']
