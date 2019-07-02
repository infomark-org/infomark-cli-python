#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Simple Infomark library to query endpoints.

See https://infomark.org/swagger/ for more information about available
endpoints.
"""

import requests
import sys


class Infomark(object):
  """docstring for Infomark"""

  def __init__(self, endpoint):
    super(Infomark, self).__init__()
    assert endpoint != ""
    self.endpoint = endpoint
    self.token = None
    self.headers = None

    self.ping()

  def _url(self, url):
    return self.endpoint + url

  def ping(self):
    if requests.get(self._url("/api/v1/ping")).status_code != 200:
      print("End point cannot be reached, are you online?")
      sys.exit(1)

  def login(self, email, password):
    self.email = email
    self.password = password

    rsl = self.post("/api/v1/auth/token",
                    {
                        "email": email,
                        "plain_password": password
                    }).json()
    self.token = rsl['access']['token']
    self.headers = {"Authorization": "Bearer %s" % self.token}

  def post(self, url, json={}):
    return requests.post(self._url(url), json=json, headers=self.headers)

  def put(self, url, json={}):
    return requests.put(self._url(url), json=json, headers=self.headers)

  def patch(self, url, json={}):
    return requests.patch(self._url(url), json=json, headers=self.headers)

  def delete(self, url):
    return requests.delete(self._url(url), headers=self.headers)

  def get(self, url):
    return requests.get(self._url(url), headers=self.headers)
