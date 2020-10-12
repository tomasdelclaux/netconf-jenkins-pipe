from ncclient import manager

with manager.connect(host="192.168.33.56", port=830, username="admin", hostkey_verify=False, password="cisco", device_params={'name':'csr'}) as m:
    c = m.get_config(source='running').data_xml
    print(c)