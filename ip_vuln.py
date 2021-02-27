import shodan
import os

word = 'vulns'
api = os.getenv("shodan")
def ip_check(ip):
        api = shodan.Shodan(api)

        ip_check.info = api.host(ip)

        ip_check.vuln = word in ip_check.info
