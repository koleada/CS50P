import re
import requests
from jsbeautifier import beautify

regex = {
    "Cloudinary": "cloudinary://.*",
    "db_query": r"(select * from|delete|update|db|connect\(|sql|mysql|postgresql|sqlite)",
    "Firebase URL": ".*firebaseio\.com",
    "Slack Token": "(xox[p|b|o|a]-[0-9]{12}-[0-9]{12}-[0-9]{12}-[a-z0-9]{32})",
    "RSA private key": "-----BEGIN RSA PRIVATE KEY-----",
    "SSH (DSA) private key": "-----BEGIN DSA PRIVATE KEY-----",
    "SSH (EC) private key": "-----BEGIN EC PRIVATE KEY-----",
    "PGP private key block": "-----BEGIN PGP PRIVATE KEY BLOCK-----",
    "Amazon AWS Access Key ID": r"AKIA[0-9A-Z]{16}",
    "Amazon MWS Auth Token": r"amzn\\.mws\\.[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
    "AWS API Key": r"AKIA[0-9A-Z]{16}",
    "amazon_aws_url2": r"("
    r"[a-zA-Z0-9-\.\_]+\.s3\.amazonaws\.com"
    r"|s3://[a-zA-Z0-9-\.\_]+"
    r"|s3-[a-zA-Z0-9-\.\_\/]+"
    r"|s3.amazonaws.com/[a-zA-Z0-9-\.\_]+"
    r"|s3.console.aws.amazon.com/s3/buckets/[a-zA-Z0-9-\.\_]+)",
    "Facebook Access Token": r"EAACEdEose0cBA[0-9A-Za-z]+",
    "Facebook OAuth": r"[f|F][a|A][c|C][e|E][b|B][o|O][o|O][k|K].*['|\"][0-9a-f]{32}['|\"]",
    "GitHub": r"[g|G][i|I][t|T][h|H][u|U][b|B].*['|\"][0-9a-zA-Z]{35,40}['|\"]",
    "github_secrets": r"(GITHUB_SECRET|GITHUB_KEY|github_secret|github_key|github_token|GITHUB_TOKEN|github_api_key|GITHUB_API_KEY)[a-z_=\s\"'\:]{0,10}[^a-zA-Z0-9][a-zA-Z0-9]{40}[^a-zA-Z0-9]",
    "github": r"(GITHUB_SECRET|GITHUB_KEY|github_secret|github_key|github_token|GITHUB_TOKEN|github_api_key|GITHUB_API_KEY)",
    "Generic API Key": r"[a|A][p|P][i|I][_]?[k|K][e|E][y|Y].*['|\"][0-9a-zA-Z]{32,45}['|\"]",
    "Generic Secret": r"[s|S][e|E][c|C][r|R][e|E][t|T].*['|\"][0-9a-zA-Z]{32,45}['|\"]",
    "Google API Key": r"AIza[0-9A-Za-z\\-_]{35}",
    "Google Cloud Platform API Key": r"AIza[0-9A-Za-z\\-_]{35}",
    "Google Cloud Platform OAuth": r"[0-9]+-[0-9A-Za-z_]{32}\\.apps\\.googleusercontent\\.com",
    "Google Drive API Key": r"AIza[0-9A-Za-z\\-_]{35}",
    "Google Drive OAuth": r"[0-9]+-[0-9A-Za-z_]{32}\\.apps\\.googleusercontent\\.com",
    "Google (GCP) Service-account": '"type": "service_account"',
    "Google Gmail API Key": r"AIza[0-9A-Za-z\\-_]{35}",
    "Google Gmail OAuth": r"[0-9]+-[0-9A-Za-z_]{32}\\.apps\\.googleusercontent\\.com",
    "Google OAuth Access Token": r"ya29\\.[0-9A-Za-z\\-_]+",
    "Google YouTube API Key": r"AIza[0-9A-Za-z\\-_]{35}",
    "Google YouTube OAuth": r"[0-9]+-[0-9A-Za-z_]{32}\\.apps\\.googleusercontent\\.com",
    "Heroku API Key": r"[h|H][e|E][r|R][o|O][k|K][u|U].*[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}",
    "MailChimp API Key": r"[0-9a-f]{32}-us[0-9]{1,2}",
    "Mailgun API Key": r"key-[0-9a-zA-Z]{32}",
    "Password in URL": r"[a-zA-Z]{3,10}://[^/\\s:@]{3,20}:[^/\\s:@]{3,20}@.{1,100}[\"'\\s]",
    "PayPal Braintree Access Token": r"access_token\\$production\\$[0-9a-z]{16}\\$[0-9a-f]{32}",
    "Picatic API Key": r"sk_live_[0-9a-z]{32}",
    "possible_Creds": r"(?i)("
    r"password\s*[`=:\"]+\s*[^\s]+|"
    r"password is\s*[`=:\"]*\s*[^\s]+|"
    r"pwd\s*[`=:\"]*\s*[^\s]+|"
    r"passwd\s*[`=:\"]+\s*[^\s]+)",
    "credentials": r"(pwd|passwd|credentials|username|password|user=|admin|root|administrator)",
    "Slack Webhook": r"https://hooks.slack.com/services/T[a-zA-Z0-9_]{8}/B[a-zA-Z0-9_]{8}/[a-zA-Z0-9_]{24}",
    "Stripe API Key": r"sk_live_[0-9a-zA-Z]{24}",
    "Stripe Restricted API Key": r"rk_live_[0-9a-zA-Z]{24}",
    "Square Access Token": r"sq0atp-[0-9A-Za-z\\-_]{22}",
    "Square OAuth Secret": r"sq0csp-[0-9A-Za-z\\-_]{43}",
    "Twilio API Key": r"SK[0-9a-fA-F]{32}",
    "Twitter Access Token": r"[t|T][w|W][i|I][t|T][t|T][e|E][r|R].*[1-9][0-9]+-[0-9a-zA-Z]{40}",
    "Twitter OAuth": r"[t|T][w|W][i|I][t|T][t|T][e|E][r|R].*['|\"][0-9a-zA-Z]{35,44}['|\"]",
    "Unknown_api": r"(aws-keys|api_key=|api=|apisecret|access_key_id=|secret_key=|secret|access_token|refresh_token|privateKey|publicKey|key)",
}

# make the get request
r = requests.get(
    "https://static.tradingview.com/static/bundles/27883.3d2e60e6d67d4467f4f5.js"
)

# get the actual JS
js = r.text

# make the JS look normal (typical line breaks not just a huge block of code)
js = beautify(js)


for line in js.splitlines():

    for key in regex.keys():
        words = line.split()
        for word in words:
            if matches := re.search(
                regex[key],
                word,
                re.IGNORECASE,
            ):
                print(f"Match found key:{key} line:{line} + word:{word}")
