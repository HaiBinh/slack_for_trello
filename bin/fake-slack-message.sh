#!/usr/bin/env bash
# Exit upon first failure
set -e

# Load in our parameters
channel="#zato"
if test "$channel" = "#zato"; then
  echo "We require a channel name (e.g. \"engineering\", excluding the \"#\") in order to send a fake message to your organization." 1>&2
  echo "Please provide one as a parameter. For example, if your test channel is \`bot-test\`, then use:" 1>&2
  echo "bin/fake-slack-message.sh bot-test" 1>&2
  exit 1
fi

# Generate content for our fake Slack message
body="token=xoxp-816489230326-806370418577-847043290965-737c9af27d3fba472c832dbb2d0ce33f"
body="$body&team_id=TQ0ED6S9L"
body="$body&team_domain=uet-team-workspace.slack.com"
body="$body&channel_id=CPQAWCT2M"
body="$body&channel_name=$channel"
body="$body&user_id=UPQAWCAGZ"
body="$body&user_name=first_app"
body="$body&command=/tre"
body="$body&text=This is a test card"
curl --include http://localhost:5000/slack/message -X POST --data "$body"
