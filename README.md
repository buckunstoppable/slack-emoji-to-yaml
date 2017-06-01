# slack-emoji-to-yaml

Currently, Slack does not offer a way to port custom emoji from team to team, or to upload custom emoji via an exposed API endpoint. 

This script connect you to your team's Slack, retrieve a list of its custom emoji, and create a .yaml file that can be used by the EmojiPacks app (https://github.com/lambtron/emojipacks) to bulk upload these custom emoji to a new team.

## Requirements
You will need to retrieve the slackclient module via `pip install slackclient`.

Additionally, in the `\env\` subdirectory, you will need to create a file called `slack.json`. This file should contain your Slack token in the following format:

```json
{
  "token": {"TOKEN_STRING_HERE"}
}
```

## To run

Once you have the `slackclient` module and your `slack.json`, simply run emoji-to-yaml.py, and an `emoji.yaml` file will be created that you can use with EmojiPacks.
