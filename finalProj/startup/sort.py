from collections import OrderedDict
import re

regex = {
    "google_api": r"AIza[0-9A-Za-z-_]{35}",
    "firebase": r"AAAA[A-Za-z0-9_-]{7}:[A-Za-z0-9_-]{140}",
    "google_captcha": r"6L[0-9A-Za-z-_]{38}|^6[0-9a-zA-Z_-]{39}$",
    "google_oauth": r"ya29\.[0-9A-Za-z\-_]+",
    "amazon_aws_access_key_id": r"A[SK]IA[0-9A-Z]{16}",
    "amazon_mws_auth_toke": r"amzn\\.mws\\.[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
    "amazon_aws_url": r"s3\.amazonaws.com[/]+|[a-zA-Z0-9_-]*\.s3\.amazonaws.com",
    "amazon_aws_url2": r"("
    r"[a-zA-Z0-9-\.\_]+\.s3\.amazonaws\.com"
    r"|s3://[a-zA-Z0-9-\.\_]+"
    r"|s3-[a-zA-Z0-9-\.\_\/]+"
    r"|s3.amazonaws.com/[a-zA-Z0-9-\.\_]+"
    r"|s3.console.aws.amazon.com/s3/buckets/[a-zA-Z0-9-\.\_]+)",
    "facebook_access_token": r"EAACEdEose0cBA[0-9A-Za-z]+",
    "authorization_basic": r"basic [a-zA-Z0-9=:_\+\/-]{5,100}",
    "authorization_bearer": r"bearer [a-zA-Z0-9_\-\.=:_\+\/]{5,100}",
    "authorization_api": r"api[key|_key|\s+]+[a-zA-Z0-9_\-]{5,100}",
    "mailgun_api_key": r"key-[0-9a-zA-Z]{32}",
    "twilio_api_key": r"SK[0-9a-fA-F]{32}",
    "twilio_account_sid": r"AC[a-zA-Z0-9_\-]{32}",
    "twilio_app_sid": r"AP[a-zA-Z0-9_\-]{32}",
    "paypal_braintree_access_token": r"access_token\$production\$[0-9a-z]{16}\$[0-9a-f]{32}",
    "square_oauth_secret": r"sq0csp-[ 0-9A-Za-z\-_]{43}|sq0[a-z]{3}-[0-9A-Za-z\-_]{22,43}",
    "square_access_token": r"sqOatp-[0-9A-Za-z\-_]{22}|EAAA[a-zA-Z0-9]{60}",
    "stripe_standard_api": r"sk_live_[0-9a-zA-Z]{24}",
    "stripe_restricted_api": r"rk_live_[0-9a-zA-Z]{24}",
    "github_access_token": r"[a-zA-Z0-9_-]*:[a-zA-Z0-9_\-]+@github\.com*",
    "rsa_private_key": r"-----BEGIN RSA PRIVATE KEY-----",
    "ssh_dsa_private_key": r"-----BEGIN DSA PRIVATE KEY-----",
    "ssh_dc_private_key": r"-----BEGIN EC PRIVATE KEY-----",
    "pgp_private_block": r"-----BEGIN PGP PRIVATE KEY BLOCK-----",
    "json_web_token": r"ey[A-Za-z0-9-_=]+\.[A-Za-z0-9-_=]+\.?[A-Za-z0-9-_.+/=]*$",
    "slack_token": r"\"api_token\":\"(xox[a-zA-Z]-[a-zA-Z0-9-]+)\"",
    "SSH_privKey": r"([-]+BEGIN [^\s]+ PRIVATE KEY[-]+[\s]*[^-]*[-]+END [^\s]+ PRIVATE KEY[-]+)",
    "Heroku API KEY": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
    "possible_Creds": r"(?i)("
    r"password\s*[`=:\"]+\s*[^\s]+|"
    r"password is\s*[`=:\"]*\s*[^\s]+|"
    r"pwd\s*[`=:\"]*\s*[^\s]+|"
    r"passwd\s*[`=:\"]+\s*[^\s]+)",
}


new = dict(sorted(regex.items(), key=lambda i: i[0].lower()))

new = dict((k.lower(), v) for k, v in new.items())

print(re.search(regex["ssh_dsa_private_key"], "-----BEGIN DSA PRIVATE KEY-----"))


sorted = {
    "amazon_aws_access_key_id": "A[SK]IA[0-9A-Z]{16}",
    "amazon_aws_url": "s3\\\\.amazonaws.com[/]+|[a-zA-Z0-9_-]*\\\\.s3\\\\.amazonaws.com",
    "amazon_aws_url2": "([a-zA-Z0-9-\\\\.\\\\_]+\\\\.s3\\\\.amazonaws\\\\.com|s3://[a-zA-Z0-9-\\\\.\\\\_]+|s3-[a-zA-Z0-9-\\\\.\\\\_\\\\/]+|s3.amazonaws.com/[a-zA-Z0-9-\\\\.\\\\_]+|s3.console.aws.amazon.com/s3/buckets/[a-zA-Z0-9-\\\\.\\\\_]+)",
    "amazon_mws_auth_toke": "amzn\\\\.mws\\\\.[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
    "authorization_api": "api[key|_key|\\\\s+]+[a-zA-Z0-9_\\\\-]{5,100}",
    "authorization_basic": "basic [a-zA-Z0-9=:_\\\\+\\\\/-]{5,100}",
    "authorization_bearer": "bearer [a-zA-Z0-9_\\\\-\\\\.=:_\\\\+\\\\/]{5,100}",
    "aws api key": "AKIA[0-9A-Z]{16}",
    "aws_access_key": "((access[-_]?key[-_]?id)|(ACCESS[-_]?KEY[-_]?ID)|([Aa]ccessKeyId)|(access[_-]?id)).{0,20}AKIA[a-zA-Z0-9+/]{16}[^a-zA-Z0-9+/]",
    "aws_credentials_context": "access_key_id|secret_access_key|AssetSync.configure",
    "aws_secret_key": "((secret[-_]?access[-_]?key)|(SECRET[-_]?ACCESS[-_]?KEY|(private[-_]?key))|([Ss]ecretAccessKey)).{0,20}[^a-zA-Z0-9+/][a-zA-Z0-9+/]{40}\\b",
    "facebook access token": "EAACEdEose0cBA[0-9A-Za-z]+",
    "facebook oauth": "[f|F][a|A][c|C][e|E][b|B][o|O][o|O][k|K].*['|\\\"][0-9a-f]{32}['|\\\"]",
    "facebook_access_token": "EAACEdEose0cBA[0-9A-Za-z]+",
    "facebook_secret": "(facebook_secret|FACEBOOK_SECRET|facebook_app_secret|FACEBOOK_APP_SECRET)[a-z_=\\s\\\"'\\:]{0,5}[^a-zA-Z0-9][a-f0-9]{32}[^a-zA-Z0-9]",
    "firebase": "AAAA[A-Za-z0-9_-]{7}:[A-Za-z0-9_-]{140}",
    "firebase url": ".*firebaseio\\\\.com",
    "generic api key": "[a|A][p|P][i|I][_]?[k|K][e|E][y|Y].*['|\\\"][0-9a-zA-Z]{32,45}['|\\\"]",
    "generic secret": "[s|S][e|E][c|C][r|R][e|E][t|T].*['|\\\"][0-9a-zA-Z]{32,45}['|\\\"]",
    "github": "[g|G][i|I][t|T][h|H][u|U][b|B].*['|\\\"][0-9a-zA-Z]{35,40}['|\\\"]",
    "github_access_token": "[a-zA-Z0-9_-]*:[a-zA-Z0-9_\\\\-]+@github\\\\.com*",
    "github_key": "(GITHUB_SECRET|GITHUB_KEY|github_secret|github_key|github_token|GITHUB_TOKEN|github_api_key|GITHUB_API_KEY)[a-z_=\\s\\\"\\':]{0,10}[^a-zA-Z0-9][a-zA-Z0-9]{40}[^a-zA-Z0-9]",
    "google cloud platform api key": "AIza[0-9A-Za-z\\\\-_]{35}",
    "google cloud platform oauth": "[0-9]+-[0-9A-Za-z_]{32}\\\\.apps\\\\.googleusercontent\\\\.com",
    "google drive api key": "AIza[0-9A-Za-z\\\\-_]{35}",
    "google drive oauth": "[0-9]+-[0-9A-Za-z_]{32}\\\\.apps\\\\.googleusercontent\\\\.com",
    "google gmail api key": "AIza[0-9A-Za-z\\\\-_]{35}",
    "google gmail oauth": "[0-9]+-[0-9A-Za-z_]{32}\\\\.apps\\\\.googleusercontent\\\\.com",
    "google oauth access token": "ya29\\\\.[0-9A-Za-z\\\\-_]+",
    "google youtube api key": "AIza[0-9A-Za-z\\\\-_]{35}",
    "google youtube oauth": "[0-9]+-[0-9A-Za-z_]{32}\\\\.apps\\\\.googleusercontent\\\\.com",
    "google_api": "AIza[0-9A-Za-z-_]{35}",
    "google_captcha": "6L[0-9A-Za-z-_]{38}|^6[0-9a-zA-Z_-]{39}$",
    "google_oauth": "ya29\\\\.[0-9A-Za-z\\\\-_]+",
    "heroku api key": "[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
    "json_web_token": "ey[A-Za-z0-9-_=]+\\\\.[A-Za-z0-9-_=]+\\\\.?[A-Za-z0-9-_.+/=]*$",
    "mailchimp api key": "[0-9a-f]{32}-us[0-9]{1,2}",
    "mailgun_api_key": "key-[0-9a-zA-Z]{32}",
    "paypal_braintree_access_token": "access_token\\\\$production\\\\$[0-9a-z]{16}\\\\$[0-9a-f]{32}",
    "pgp_private_block": "-----BEGIN PGP PRIVATE KEY BLOCK-----",
    "pgsql connection information": "(?:postgres|pgsql)\\:\\/\\/",
    "possible_creds": '(?i)(password\\\\s*[`=:"]+\\\\s*[^\\\\s]+|password is\\\\s*[`=:"]*\\\\s*[^\\\\s]+|pwd\\\\s*[`=:"]*\\\\s*[^\\\\s]+|passwd\\\\s*[`=:"]+\\\\s*[^\\\\s]+)',
    "rsa_private_key": "-----BEGIN RSA PRIVATE KEY-----",
    "slack webhook": "https://hooks.slack.com/services/T[a-zA-Z0-9_]{8}/B[a-zA-Z0-9_]{8}/[a-zA-Z0-9_]{24}",
    "slack_token": "(xox[a-zA-Z]-[a-zA-Z0-9-]+)",
    "square_access_token": "sqOatp-[0-9A-Za-z\\\\-_]{22}|EAAA[a-zA-Z0-9]{60}",
    "square_oauth_secret": "sq0csp-[ 0-9A-Za-z\\\\-_]{43}|sq0[a-z]{3}-[0-9A-Za-z\\\\-_]{22,43}",
    "ssh_dc_private_key": "-----BEGIN EC PRIVATE KEY-----",
    "ssh_dsa_private_key": "-----BEGIN DSA PRIVATE KEY-----",
    "ssh_privkey": "([-]+BEGIN [^\\\\s]+ PRIVATE KEY[-]+[\\\\s]*[^-]*[-]+END [^\\\\s]+ PRIVATE KEY[-]+)",
    "stripe_restricted_api": "rk_live_[0-9a-zA-Z]{24}",
    "stripe_standard_api": "sk_live_[0-9a-zA-Z]{24}",
    "twilio_account_sid": "AC[a-zA-Z0-9_\\\\-]{32}",
    "twilio_api_key": "SK[0-9a-fA-F]{32}",
    "twilio_app_sid": "AP[a-zA-Z0-9_\\\\-]{32}",
    "twitter access token": "[t|T][w|W][i|I][t|T][t|T][e|E][r|R].*[1-9][0-9]+-[0-9a-zA-Z]{40}",
    "twitter oauth": "[t|T][w|W][i|I][t|T][t|T][e|E][r|R].*['|\\\"][0-9a-zA-Z]{35,44}['|\\\"]",
}
