from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from rest_framework import viewsets, permissions

from api.serializers import AdSerializer, ExchangeProposalSerializer

from barter.models import Ad, ExchangeProposal


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer = AdSerializer
    serializer_class = AdSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ExchangeProposalViewSet(viewsets.ModelViewSet):
    queryset = ExchangeProposal.objects.all()
    serializer = ExchangeProposalSerializer
    serializer_class = ExchangeProposalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)