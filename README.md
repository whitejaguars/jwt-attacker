# JWT security testing tool
This is a simple tool for testing JSON Web Tokens (JWT) looking for known weak secrets.

The script is going to brute force the JWT with a list of known default secrets.

# Install
Clone the repository:
``` bash
git clone https://github.com/whitejaguars/jwt-attacker.git
cd jwt-attacker
```

Create a virtual environment (recommended):
``` bash
python -m venv venv
venv/bin/pip install -r requirements.txt
```

Run the script for getting help:
``` bash
venv/bin/python jwt-attacker.py -h
```

Test a JWT:
``` bash
venv/bin/python jwt-attacker.py --jwt <token-here>
```
