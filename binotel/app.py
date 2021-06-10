import requests


class Binotel:
    HOST = "https://api.binotel.com/api/4.0/"

    def __init__(self, key: str, secret: str):
        self.key = key
        self.secret = secret

    def prepare_body(self, body: dict) -> dict:
        body.update({"key": self.key, "secret": self.secret})
        return body

    def post(self, path: str, body: dict, **kw):
        body.update(kw)
        req = requests.post(self.HOST + path, json=self.prepare_body(body))
        return req.json()

    def all_incoming_calls_since(self, timestamp: int):
        return self.post("stats/all-incoming-calls-since.json", {"timestamp": timestamp})

    def call_internal_number_to_external_number(self, internal_number: str, external_number: str,  **kw):
        return self.post("calls/internal-number-to-external-number.json",
                         {"internalNumber": internal_number, "externalNumber": external_number}, **kw)

    def call_external_number_to_external_number(self, external_number1: str, external_number2: str,
                                                pbx_number: str, **kw):
        return self.post("calls/external-number-to-external-number.json", {"externalNumber1": external_number1,
                                                                           "externalNumber2": external_number2,
                                                                           "pbxNumber": pbx_number}, **kw)

    def external_number_to_incoming_call(self, external_number: str, pbx_number: str, **kw):
        return self.post("calls/external-number-to-incoming-call.json", {"externalNumber": external_number,
                                                                         "pbxNumber": pbx_number}, **kw)

    def online_calls(self):
        return self.post("stats/online-calls.json", {})

    def list_of_lost_calls_for_today(self):
        return self.post("stats/list-of-lost-calls-for-today.json", {})

    def list_of_calls_for_period(self, start_time: int, stop_time: int):
        return self.post("stats/list-of-calls-for-period.json", {"startTime": start_time, "stopTime": stop_time})

    def attended_call_transfer(self, general_call_id: str, external_number: str):
        return self.post("calls/attended-call-transfer.json", {"generalCallID": general_call_id,
                                                               "externalNumber": external_number})
