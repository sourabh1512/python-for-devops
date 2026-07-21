import json

import requests

url = "https://chartink.com/screener/process"

headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "content-type": "application/json",
    "origin": "https://chartink.com",
    "priority": "u=1, i",
    "referer": "https://chartink.com/screener/copy-rsi-above-55-and-breakout-615",
    "sec-ch-ua": '"Not;A=Brand";v="8", "Chromium";v="150", "Google Chrome";v="150"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
    "x-xsrf-token": "eyJpdiI6Ikt2alpTV25KblVsUFVKYlZNckZiZWc9PSIsInZhbHVlIjoiNG9kWXpEUnZIY3YxNm1hVnlremVvNkVVSktkU1RNbmxidFdMZTlMQ3o4YUFITXBVOGUrUExIb0dNRHNwaHBzWXZrOEVnZ3NiMkMyamorMzIwSzljbzhyUWQwVkVLWjlEK3RPb2E5U1RaRUh5N1lMdnd2RjZOcVpWRHFEdXRrb1EiLCJtYWMiOiJjNzBjNjdiN2M1MzE2OWMyZjQ2NDRjZTE3NGEwZjBjMjYxNDJiYmFiYjYwY2IxMGJhMjI2ZWQ5ZGQ2NzJhYTFlIiwidGFnIjoiIn0=",
}

cookie_header = (
    "remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d="
    "eyJpdiI6IkhDd05qM2pTT1JVZW0vdGVHOWNQYlE9PSIsInZhbHVlIjoiNWpJVlIzdW8vRnpWemJGWW80ZWVKelBQUmJqSUZiNy9MWW1HbXk5UEFTa2RWaEJFekNxY0F2bHRpc3M0S2hOR0JGQU5pbzZYNityTURhTGJrT25RcHVNQjR3N2dnNTNWRnhwV1o5QlNnT1ZVYlh4UWgrMWNuYlprM2VMR0tTZmoxczdRRXNFMnIzMndsaUp4MWp1bU00d0tKK3FyNnlhdDgyaytXdmZhUm91NGtLa25JcDYwYkIzTCs5M0Y0VDZnUk92ZWdVQytya0JIdkx1RGlsS1hZdzlUMEJ5RGJXSjZqb0Y3YytwK2V3VT0iLCJtYWMiOiJhOGZiOGY1ZDFiYmExNDRhNmVhMjRmZmExN2FmOGI1Y2VjMDYwZDNkNzZkOGMyOGIzYmM0OWU3M2VkZGEzZWY3IiwidGFnIjoiIn0%3D; "
    "_gid=GA1.2.1835299030.1784555416; "
    "_cc_id=ddd4893ce0c7883fd0816bb00b1dd02a; "
    "panoramaId_expiry=1784641817964; "
    "panoramaId=29b17ab660a39c0eba0bea427d07a9fb927a6e7c21f7005df6d60ced08258c76; "
    "panoramaIdType=panoDevice; "
    "FCCDCF=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5B32%2C%22%5B%5C%226f1b27a0-7d11-4a14-98ae-03a35fed3e2a%5C%22%2C%5B1784555417%2C262000000%5D%5D%22%5D%5D%5D; "
    "FCNEC=%5B%5B%22AKsRol-TAHbJACJY4lTrE5ZSlvrKAxjPJXn5e-ns2BOn-gqwuibhr6NbHGZUaZzRF80Ca7kNMBb7QAhsRqSehMMwoudMOCcEK5KcwrhEfRWcCXflfJ6qWQ5mePeAXNlA69Fav4cxcIwmIYxtne0C09Q3gSkT2v11bg%3D%3D%22%5D%5D; "
    "_ga=GA1.1.1968319544.1784554512; "
    "_ga_7P3KPC3ZPP=GS2.1.s1784598208$o3$g1$t1784598228$j40$l0$h0; "
    "__gads=ID=a475dc11d13edfcf:T=1784555440:RT=1784598228:S=ALNI_MYui5MgqrqdpMh-ReKIEte6_hI-uA; "
    "__gpi=UID=000014cd24fad536:T=1784555440:RT=1784598228:S=ALNI_MZGgCFV-utYaaRCbqopFGIu-JkQow; "
    "__eoi=ID=262f680056f8b3e7:T=1784555440:RT=1784598228:S=AA-Afja56EFTSdPZv4hb308AWKUH; "
    "XSRF-TOKEN=eyJpdiI6Ikt2alpTV25KblVsUFVKYlZNckZiZWc9PSIsInZhbHVlIjoiNG9kWXpEUnZIY3YxNm1hVnlremVvNkVVSktkU1RNbmxidFdMZTlMQ3o4YUFITXBVOGUrUExIb0dNRHNwaHBzWXZrOEVnZ3NiMkMyamorMzIwSzljbzhyUWQwVkVLWjlEK3RPb2E5U1RaRUh5N1lMdnd2RjZOcVpWRHFEdXRrb1EiLCJtYWMiOiJjNzBjNjdiN2M1MzE2OWMyZjQ2NDRjZTE3NGEwZjBjMjYxNDJiYmFiYjYwY2IxMGJhMjI2ZWQ5ZGQ2NzJhYTFlIiwidGFnIjoiIn0%3D; "
    "ci_session=eyJpdiI6IjFST0k3V0svdkZHdzNEZTBMWDVrbHc9PSIsInZhbHVlIjoiMGZZMjIyNFpjMlhLTTFKYlNmVG9CWUJlaStWbzZmb3BUOEhpTmVTTFM4TGhhVlJTZlZqV2IzV0xveExwUFVKWEZuWW5PU240NmR0Vzc2NFhXNmpyMmFuR1EzMjFZL2dXNFQ3TjJxL3JJTk9CMXh2MjlLL0RIKytFVFBVaW83bS8iLCJtYWMiOiI2ZjYyMWQ2ZGQ5YmE3Y2MzZGI2YjYzNmI2NDdhNjg3MjdmMmRhOGM1NmM2NGE2MmYzODE0NTcyNjY2ZDhmMTk3IiwidGFnIjoiIn0%3D"
)

cookies = {}
for raw_cookie in cookie_header.split(";"):
    if "=" in raw_cookie:
        key, value = raw_cookie.split("=", 1)
        cookies[key.strip()] = value.strip()

payload = {
    "scan_clause": "( {cash} (  weekly close >=  52 and  daily ema( close,5 ) >  daily ema( close,26 ) and  daily ema( close,13 ) >  daily ema( close,26 ) and  daily close >  1 day ago close *  1.03 and  daily volume >  daily sma( volume,20 ) *  1.0 and  daily ema( close,5 ) >  daily ema( close,13 ) and  daily high =  daily max( 260 ,  daily high ) *  1 and  1 day ago close >  2 days ago close *  0.98 and  daily rsi( 14 ) >  50 ) )",
    "debug_clause": "groupcount( 1 where  weekly close >=  52),groupcount( 1 where  daily ema( close,5 ) >  daily ema( close,26 )),groupcount( 1 where  daily ema( close,13 ) >  daily ema( close,26 )),groupcount( 1 where  daily close >  1 day ago close *  1.03),groupcount( 1 where  daily volume >  daily sma( volume,20 ) *  1.0),groupcount( 1 where  daily ema( close,5 ) >  daily ema( close,13 )),groupcount( 1 where  daily high =  daily max( 260 ,  daily high ) *  1),groupcount( 1 where  1 day ago close >  2 days ago close *  0.98),groupcount( 1 where  daily rsi( 14 ) >  50)",
    "column_clause": " Daily Close as 'scan-column-default-close',  Daily \"close - 1 candle ago close / 1 candle ago close * 100\" as 'scan-column-default-percent-change', filternumber( daily close >  1 day ago close,1) as 'default-percent-change-conditional-filters-color',  Daily Volume as 'scan-column-default-volume'",
}

response = requests.post(url, headers=headers, cookies=cookies, json=payload, timeout=30)

print(f"Status code: {response.status_code}")
print("Response headers:")
for key, value in response.headers.items():
    if key.lower() in {"content-type", "set-cookie", "cache-control", "server"}:
        print(f"{key}: {value}")
print("\n SCRIPT: RSI ABOVE 50 AND BREAKOUT")
print("\nFormatted table:")
try:
    data = response.json()
    rows = data.get("data", [])
    if not rows:
        print("No matching records found.")
    else:
        headers = ["CODE", "NAME", "CLOSE", "CHANGE %", "VOLUME"]
        rows_display = [
            [
                item.get("nsecode", ""),
                item.get("name", ""),
                item.get("scan-column-default-close", ""),
                item.get("scan-column-default-percent-change", ""),
                item.get("scan-column-default-volume", ""),
            ]
            for item in rows
        ]

        col_widths = [max(len(str(row[i])) for row in [headers] + rows_display) for i in range(len(headers))]
        print(" | ".join(header.ljust(col_widths[i]) for i, header in enumerate(headers)))
        print("-+-".join("-" * width for width in col_widths))
        for row in rows_display:
            print(" | ".join(str(value).ljust(col_widths[i]) for i, value in enumerate(row)))
except ValueError:
    print(response.text[:4000])
