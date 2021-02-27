import shodan

word = 'vulns'

def ip_check(ip):
        api = shodan.Shodan('ZJUHwZkpzTKxZdzcRQ6RYpGEQF4LlPUt')

        ip_check.info = api.host(ip)

        ip_check.vuln = word in ip_check.info
