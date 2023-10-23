import json
result_set = {
    'json_01': {'Result': 'FAIL',
                'Expected': {'error': {'code': 0, 'message': 'Successfully Registered'}, 'id': 1, 'jsonrpc': '2.0'},
                'Actual': {'error': {'code': 0, 'message': 'Successfully Registered'}, 'id': 1, 'jsonrpc': '2.0'}},
    'json_02': {'Result': 'PASS',
                'Expected': {'ids': ['6acc25e3a982265407efdcd3db5894764bd31aa91a443cc91164af2693aa0205']},
                'Actual': {'result': {'totalCount': 1, 'lookupTag': '6acc25e3a982265407efdcd3db5894764bd31aa91a443cc91164af2693aa0205', 'ids': ['6acc25e3a982265407efdcd3db5894764bd31aa91a443cc91164af2693aa0205']}, 'id': 2, 'jsonrpc': '2.0'}},
    'json_03': {'Result': 'PASS',
                'Expected': {'ids': ['6acc25e3a982265407efdcd3db5894764bd31aa91a443cc91164af2693aa0205']},
                'Actual': {'result': {'totalCount': 1, 'lookupTag': '6acc25e3a982265407efdcd3db5894764bd31aa91a443cc91164af2693aa0205', 'ids': ['6acc25e3a982265407efdcd3db5894764bd31aa91a443cc91164af2693aa0205']}, 'id': 3, 'jsonrpc': '2.0'}},
    'json_04': {'Result': 'PASS',
                'Expected': {'ids': ['6acc25e3a982265407efdcd3db5894764bd31aa91a443cc91164af2693aa0205']},
                'Actual': {'result': {'totalCount': 1, 'lookupTag': '6acc25e3a982265407efdcd3db5894764bd31aa91a443cc91164af2693aa0205', 'ids': ['6acc25e3a982265407efdcd3db5894764bd31aa91a443cc91164af2693aa0205']}, 'id': 4, 'jsonrpc': '2.0'}},
    'json_05': {'Result': 'PASS',
                'Expected': {'ids': ['6acc25e3a982265407efdcd3db5894764bd31aa91a443cc91164af2693aa0205']},
                'Actual': {'result': {'totalCount': 1, 'lookupTag': '6acc25e3a982265407efdcd3db5894764bd31aa91a443cc91164af2693aa0205', 'ids': ['6acc25e3a982265407efdcd3db5894764bd31aa91a443cc91164af2693aa0205']}, 'id': 5, 'jsonrpc': '2.0'}},
    'json_06': {'Result': 'PASS',
                'Expected': {'workerType': 13, 'organizationId': 'ccd3f227435cdeac99776e019b76ef5858b5f660dd0308fc34f0168d30ec672f', 'applicationTypeId': 'd9da17ef4a63c2b8f85791a62e17b58623bc7caff7e33d3fb26bd74ac2e87027'},
                'Actual': {'result': {'workerType': 13, 'organizationId': 'ccd3f227435cdeac99776e019b76ef5858b5f660dd0308fc34f0168d30ec672f', 'applicationTypeId': 'd9da17ef4a63c2b8f85791a62e17b58623bc7caff7e33d3fb26bd74ac2e87027', 'details': {'hashingAlgorithm': 'SHA-256', 'signingAlgorithm': 'SECP256K1', 'keyEncryptionAlgorithm': 'RSA-OAEP-3072', 'dataEncryptionAlgorithm': 'AES-GCM-256', 'workerTypeData': {'verificationKey': '0xA', 'encryptionKey': 'ekey', 'encryptionKeyNonce': 'enounce', 'encryptionKeySignature': 'esig', 'enclaveCertificate': 'ecert'}}, 'status': 1}, 'id': 11, 'jsonrpc': '2.0'}}}

def flatten_dict(input, result):
    keys = input.keys()
    for k in keys:
        details = input[k]
        if type(details) == dict:
            flatten_dict(details, result)
        else:
            result[k] = details

# -----------------------------------------------------------------------------
def verify_results(file_name, response):
    result = []
    status = "PASS"
    # f_name = file_name.decode("utf-8").replace(".json", "")
    f_name = file_name
    f = open("./input_results.json", "r")
    test_data = json.loads(f.read())
    expected = test_data[f_name]
    # m_name = input_json["method"]
    result_data = {}
    flatten_dict(response, result_data)
    for key, value in expected.items():
        result.append(value == result_data.get(key))
    f.close()
    if not result:
        status = "NOT VERIFIED"
    elif not all(result):
        status = "FAIL"
    print(status)
        # LOGGER.error("File: %s verification failed: Response is %s.\n\n", f_name, response)
    # result_set[f_name] = {"Result": status, "Expected": expected, "Actual": response}

for key, value in result_set.items():
    verify_results(key, value["Expected"])