import logging
import requests
import time
import yaml


def main():
    logging.basicConfig(level=logging.INFO)

    logging.info('Beginning dynamic dns service...')

    current_ip = ''
    old_ip = ''
    while True:
        try:
            old_ip = current_ip
            current_ip = get_ip()

            if old_ip != current_ip:
                logging.info(f'IP address found: {current_ip}')

                update_api(current_ip)

                logging.info('Updated all subdomains')

            time.sleep(60)

        except Exception as exc:
            logging.error(str(exc))


def get_ip():
    return requests.get('http://ip.42.pl/raw').text


def update_api(ip):
    config = open_yaml()
    domain = config[0]['website']['domain']
    password = config[0]['website']['password']
    for subdomain in config[0]['website']['hosts']:
        requests.get('https://dynamicdns.park-your-domain.com/update?'
                     f'host={subdomain}&domain={domain}'
                     f'&password={password}&ip={ip}')


def open_yaml():
    with open("config.yaml", 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            logging.error(str(exc))


if __name__ == '__main__':
    main()
