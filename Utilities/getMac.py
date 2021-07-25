import psutil
import re

eth_list = []
ipv4_list = []
ipv6_list = []
eth_id_list = []
mac_list = []

onlyActive = True

eth_dict = psutil.net_if_addrs()
# get active interfaces
stats = psutil.net_if_stats()
available_networks = []
for intface, addr_list in eth_dict.items():
    if any(getattr(addr, 'address').startswith("169.254") for addr in addr_list):
        continue
    elif intface in stats and getattr(stats[intface], "isup"):
        available_networks.append(intface)
# -----------------------

# collect informations
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

if onlyActive is True:
    filteredResult = {}
    # filter out inactive Adresses
    for i, k in enumerate(result):
        item = result[i]
        for i2, k2 in enumerate(available_networks):
            item2 = available_networks[i2]
            if item['name'] in item2:
                filteredResult[i] = item
    print(filteredResult)
else:
    for i, k in enumerate(result):
        item = result[i]
        print("---------")
        print("%s, %s, %s " % (item['name'], item['mac'], item['ip4']))
