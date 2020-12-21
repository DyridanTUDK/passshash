import requests
import hashlib
import sys


def requests_api_data(query_char):    
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: response code ({res.status_code}), check the api and try again ')
    return res

def get_pass_leak_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            a = h
            return count
    return 0

def showcase(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    a = []
    for h, count in hashes:
        a.append(h)
        return a

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail  = sha1password[:5], sha1password[5:]
    response = requests_api_data(first5_char)
    return get_pass_leak_count(response, tail)


def gottem(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail  = sha1password[:5], sha1password[5:]
    response = requests_api_data(first5_char)
    # return get_pass_leak_count(response, tail)
    return showcase(response, tail)



def main(args):
    count =  pwned_api_check(args)
    if count:
        return (f'{args} was found the {count} time... You should change your password')
    else:
        return(f'{args} was NOT found. Carry on!')
    # return f'{args} was found the {count} time... You should change your password'

# main(sys.argv[1:])
