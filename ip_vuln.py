import shodan


word = 'vulns'
def ip_check(ip, api_key):
        api = shodan.Shodan(api_key)

        ip_check.info = api.host(ip)

        ip_check.vuln = word in ip_check.info
