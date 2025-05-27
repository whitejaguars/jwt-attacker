# JWT security testing tool
This is a simple tool for testing JSON Web Tokens (JWT) looking for known weak secrets.

The script is going to brute force the JWT with a list of known default secrets.

# Install
Clone the repository:
``` bash
git clone https://github.com/whitejaguars/jwt-attacker.git
cd jwt-attacker
```

Create a virtual environment:
``` bash
python3 -m venv venv
```
![image](https://github.com/user-attachments/assets/ff45928d-f578-4afe-83db-dbdc06def1a6)

Install the requirements:
``` bash
venv/bin/pip install -r requirements.txt
```

Run the script for getting help:
``` bash
venv/bin/python jwt-attacker.py -h
```
![image](https://github.com/user-attachments/assets/dff4af9f-fdb3-408f-9486-1c3bebc3a5ef)


Test a JWT:
``` bash
venv/bin/python jwt-attacker.py --jwt <token-here>
```

![image](https://github.com/user-attachments/assets/04651fd9-0478-4be5-ba8d-dfbf7aaa576d)

