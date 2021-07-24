import psutil
import re

eth_list = []
ipv4_list = []
ipv6_list = []
eth_id_list = []
mac_list = []

eth_dict = psutil.net_if_addrs()
for eth in eth_dict:
    eth_list.append(eth)
    eth_id_list.append(eth)
    snic_list = eth_dict[eth]
    for snic in snic_list:
        if snic.family == psutil.AF_LINK:
            mac_list.append(snic.address)
        elif snic.family.name == 'AF_INET':
            ipv4_list.append(snic.address)
        elif snic.family.name == 'AF_INET6':
            ipv6_list.append(re.sub('%.*$', '', snic.address))

# build it together
result = {}
for i, k in enumerate(eth_list):
    try:
        data = {}
        data['name'] = eth_list[i]
        data['id'] = eth_id_list[i]
        data['ip4'] = ipv4_list[i]
        data['ip6'] = ipv6_list[i]
        data['mac'] = mac_list[i]

        result[i] = data
    except Exception:
        pass

for i, k in enumerate(result):
    item = result[i]
    print("---------")
    print("%s, %s, %s " % (item['name'], item['mac'], item['ip4']))
