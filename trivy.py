import requests

headers = {
    'accept': 'application/json',
    # requests won't add a boundary if this header is set when you pass files=
    # 'Content-Type': 'multipart/form-data',
    'Authorization': 'Token da8af64aa09849f011a977d1950d230cb7b23963',
}

files = {
    'minimum_severity': (None, 'Low'),
    'active': (None, 'true'),
    'verified': (None, 'true'),
    'scan_type': (None, 'Trivy Scan'),
    'close_old_findings': (None, 'true'),
    'push_to_jira': (None, 'false'),
    'file': open('trivy.json', 'rb'),
    'product_name': (None, 'Testphp vulnweb'),
    'scan_date': (None, '2022-06-14'),
    'engagement_name': (None, 'Triv'),
}

response = requests.post('http://161.97.136.120:8080/api/v2/import-scan/', headers=headers, files=files)
