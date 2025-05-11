from rest_framework import serializers
from barter.models import Ad, ExchangeProposal
from django.contrib.auth.models import User


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"


class ExchangeProposalSerializer(serializers.ModelSerializer):
    # ad_receiver_id = AdSerializer(read_only=True)
    # ad_sender_id = AdSerializer(read_only=True)

    def get_matchingKey(self, obj):
        breakpoint()
        return obj.matchingKey

    class Meta:
        model = ExchangeProposal
        fields = "__all__"