import re


def check_character(string):
    rule = re.compile(r'[^a-zA-z0-9]')
    string = rule.search(string)
    return not bool(string)


print(check_character("adasdasredasdsadASDASDFASRSAFASD181394371843791"))
print(check_character("#%¨&$*"))
