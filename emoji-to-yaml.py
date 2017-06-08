from slackclient import SlackClient
import io, json, os, urllib

def start(cred):
	return SlackClient(cred)

def getSlackCreds(r, creds=None):
	with open(os.path.join(r,"env","slack.json")) as slackCreds:
		creds = json.load(slackCreds)
	return creds["token"]

def getAvailableEmoji(client):
	response = client.api_call("emoji.list")
	emojiJson = response["emoji"]
	aliasArray = []
	for key,val in emojiJson.items():
		emojiJson[key] = val.replace("\/","/")
		if val.startswith("alias:"):
			original = val[6:]
			aliasArray.append({"original":original, "alias": key})
			del emojiJson[key]
	return emojiJson, aliasArray

def createYaml(emojiJson, aliasArray):
	with open("emoji.yaml", "w") as outfile:
		outfile.write("title: all\nemojis:")
		for key,val in emojiJson.items():
			nameLine = "\n  - name: " + key
			srcLine = "\n    src: " + val
			aliasText = ""
			needsAliasHeading = True
			for aliasRow in aliasArray:
				if key == aliasRow["original"]:
					if needsAliasHeading:
						aliasText = "\n    aliases:"
						needsAliasHeading = False
					aliasText += "\n    - %s" % aliasRow["alias"]
					aliasArray.remove(aliasRow)
			outfile.write(nameLine)
			outfile.write(aliasText)
			outfile.write(srcLine)

ROOT = os.path.abspath(os.path.dirname(__file__))
slackConnection = start(getSlackCreds(ROOT))
emojiJson, aliasArray = getAvailableEmoji(slackConnection)
createYaml(emojiJson, aliasArray)
