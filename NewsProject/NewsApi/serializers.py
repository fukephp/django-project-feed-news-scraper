from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Article, Symbol

class ArticleSerializer(serializers.ModelSerializer):
    symbol = serializers.StringRelatedField(many=False)
    
    class Meta:
        model = Article
        fields = '__all__'

class SymbolSerializer(serializers.ModelSerializer):
    articles = serializers.StringRelatedField(many=True)

    class Meta:
        model = Symbol
        fields = '__all__'