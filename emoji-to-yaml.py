from slackclient import SlackClient
import io, json, os, urllib

def start(cred):
	return SlackClient(cred)

def getSlackCreds(r, creds=None):
	with open(os.path.join(r,"slack-creds.json")) as slackCreds:
		creds = json.load(slackCreds)
	return creds["token"]

def getAvailableEmoji(client):
	response = client.api_call("emoji.list")
	emojiJson = response["emoji"]
	for key,val in emojiJson.items():
		emojiJson[key] = val.replace("\/","/")
		if "alias:" in val:
			del emojiJson[key]
	return emojiJson

def createYaml(emojiJson):
	with open("emoji.yaml", "w") as outfile:
		outfile.write("title: all\nemojis:")
		for key,val in emojiJson.items():
			nameLine = "\n  - name: " + key
			srcLine = "\n    src: " + val
			outfile.write(nameLine)
			outfile.write(srcLine)

ROOT = os.path.abspath(os.path.dirname(__file__))
slackConnection = start(getSlackCreds(ROOT))
emojiJson = getAvailableEmoji(slackConnection)
createYaml(emojiJson)