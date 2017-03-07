from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from slackclient import SlackClient
from slackbot.settings import SLACK_TOKEN


class ChatView(APIView):
    def post(self, request):
        data = request.DATA
        print(data)
        sc = SlackClient(SLACK_TOKEN)

        sc.api_call(
            'chat.postMessage',
            channel='',
            text=''
        )

        return Response(status=status.HTTP_202_ACCEPTED)
