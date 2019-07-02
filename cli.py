#! /usr/bin/env python
# -*- coding: utf-8 -*-

from infomark.infomark import Infomark


cli = Infomark('http://localhost:3000')

# will not work (401 error as we are not logged in)
print(cli.get("/api/v1/account"))

# login
cli.login('test@uni-tuebingen.de', 'test')

# will print the information from the login identity
response = cli.get("/api/v1/account")
print(response.status_code)
print(response.json())

query = 'iet'
users = cli.get("/api/v1/users/find?query=%s" % query).json()
for user in users:
  print(user['first_name'], user['last_name'], user['email'])
