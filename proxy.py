from proxy_checker import ProxyChecker


def check_proxy(proxy):
  checker = ProxyChecker()
  check_proxy.r = checker.check_proxy(proxy)
