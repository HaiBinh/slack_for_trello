# Load in our dependencies
import json
from unittest import TestCase

import mock

from slack_to_trello import app


# Define our tests
class SlackToTrelloTestCase(TestCase):
    def setUp(self):
        """Start a server to test on"""
        self.app = app.test_client()

    def test_root(self):
        """
        A request to /
            receives a response from the server
        """
        res = self.app.get('/')
        self.assertEqual(res.status_code, 200)

    @mock.patch('slack_to_trello.model.List')
    @mock.patch('httplib2.Http.request')
    def test_slack_message(self, request_mock, trello_list_mock):
        """
        A POST request to /slack/message
            triggers a Trello card creation
            triggers a Slack message to a channel
            replies but with no content
        """
        # Define our mocks
        add_card_mock = trello_list_mock().add_card
        add_card_mock().url = 'https://trello.com/b/ffhORib2/demo-zato'

        # Make our request
        res = self.app.post('/slack/message', data={
            'token': 'xoxp-816489230326-806370418577-847043290965-737c9af27d3fba472c832dbb2d0ce33f',
            'team_id': 'TQ0ED6S9L',
            'team_domain': 'uet-team-workspace.slack.com',
            'channel_id': 'CPQAWCT2M',
            'channel_name': '#zato',
            'user_id': 'UPQAWCAGZ',
            'user_name': 'first_app',
            'command': '/tre',
            'text': 'This is a test card',
        })
        self.assertEqual(res.status_code, 200)

        # Assert mock data
        # DEV: If HTTP data gets too complex to test, consider using httpretty-fixtures
        # DEV: 1 count for our initial setup, 1 for actual invocation
        self.assertEqual(add_card_mock.call_count, 2)
        self.assertEqual(add_card_mock.call_args[1]['name'], 'This is a test card (twolfson)')

        self.assertEqual(request_mock.call_count, 1)
        self.assertEqual(request_mock.call_args[0][1], 'POST')
        self.assertEqual(json.loads(request_mock.call_args[1]['body']), {
            'channel': '#zato',
            'text': 'Trello card "<http://trello.url/|This is a test card>" created by "twolfson"',
        })
