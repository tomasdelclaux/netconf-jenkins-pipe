from ncclient import manager

with open("./netconf/configs/rollback.xml", 'r') as f:
    configuration= f.read()

with manager.connect(host="192.168.33.56", port=830, username="admin", hostkey_verify=False, password="cisco", device_params={'name':'csr'}) as m:
    load_config_general = m.edit_config(target='candidate',
                                            config=configuration,
                                            default_operation="replace",
                                            error_option='rollback-on-error')
    print("validating router configuration")
    validate_result = m.validate(source='candidate')
    print("committing configuration")
    commit_config = m.commit(confirmed=False, timeout='300')
