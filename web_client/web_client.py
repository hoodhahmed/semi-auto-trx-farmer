# imports
import re
import json
import requests


class WebClient:

    def __init__(self, url: str, ci_session: str = None, debug: bool = False):
        """
        Initialize a WebClient object.
        :param url: URL of the website to be automated. 
        # telegram https://t.me/hoodhahm for more info
        :param ci_session: ci_session cookie value.

        """
        self.url = url
        self.debug = debug
        self.remember_token = None

        if ci_session:
            self.cookies = {'ci_session': ci_session}
        else:
            self.cookies = {
                'ci_session': '6367991dd7278e0fa42f306a3ae13e7a6f5c4714',
            }
        self.headers = {
            'authority': self.url,
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': self.url,
            'referer': self.url,
            'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

    def _login(self, address: str, password: str = None, referal_id: str = ""):
        """
        Login to the website.
        :param address: trx address of the user.
        :param password: password of the user.
        :param referal_id: referal id of the user if any.
        :return: response object.
        """
        if password is None:
            password = 'pppp'

        data = {
            'username': address,
            'password': password,
            'reference_user_id': referal_id,
        }

        response = requests.post(f'{self.url}/ajax_auth',
                                 cookies=self.cookies, headers=self.headers, data=data, timeout=10)

        return response

    def logout(self):
        """
        Clear the cookies of website and logout
        """

        # Need to impliment debugiing
        #debug_print("Logging out...")

        try:
            # Resets the remember token
            self.remember_token = None
            # clear the `remember_code` from cookies
            self.cookies.pop("remember_code")

            # Need to impliment debugiing
            #debug_print("Logged out successfully")

        except:
            # Do nothing
            # Need to impliment debugiing
            #debug_print("Error while logging out")
            pass
