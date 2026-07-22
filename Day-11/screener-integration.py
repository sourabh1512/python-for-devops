import json

import requests

try:
    import brotli
except ImportError:  # pragma: no cover - optional dependency
    brotli = None

URL = "https://chartink.com/screener/process"

HEADERS = {
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
    "x-xsrf-token": "eyJpdiI6InptcjdMOFQyNUorZ2pCS1EvZE53MHc9PSIsInZhbHVlIjoidDNjUjNla2NkOFY2N2NKZEliNjQvTHp1MzRINnZVSUtDTEhCdDB4TnBtVlkwajNtT1RUVVVQOUx3RGUzYklVSWNITTVQVkk3RTc3ZVNNTy9HL1hEVzFNSUs3SXpWOFhvRVYwamM3MEwrM1l0SUFDdllRRHl4MzVkejZRMzM2U1QiLCJtYWMiOiJmMjExY2UzMmY0Mjk3NjNlMTQ5ZjYyYzgyMjc1NTkyZmY1NzU3ZGFhOTBhMWJjNjkyMTU3ZTk0NDVhMGE0ZTEyIiwidGFnIjoiIn0=",
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
    "XSRF-TOKEN=eyJpdiI6Ikhpdmp3UytoVTFFM3JrNjJXUitISEE9PSIsInZhbHVlIjoiZkR0YllPK2dlRmtpUURSdStnZ0h0NXdjaHpabzlFM3dQT1B3S3RTbjh5eVVJS1hGV0M3dEhWSml1WU91ckRzTE4wSGFtQmhCelJjVVRUdmJqMWtjd3FnOVkxZXRtMXV6ZHJaWWNONjZtVk9aWDdWVkQrWG5FdlJZZ204VnJzakwiLCJtYWMiOiJkZDQzNWFkYmRhZmRlYmE1Njg3MGU1N2Y1MzAxMTFiYTUzZjdkNzNlYjlkMGEwY2ZhOGVlMzRkZGZhNzlhMzEyIiwidGFnIjoiIn0%3D; "
    "ci_session=eyJpdiI6InA0S1dNdCs1ZjN5VVdqQUNtNFcxaXc9PSIsInZhbHVlIjoianJZRnJuR0RpS04rQ1VBZ3M2T0FibWJRd09ETm12aC84Vjc0OVRWMkNJcGpScVdYWVM2S3lPYnEwNlZjZjRHby9uekRrUGl0N0grenN2dmtkK3RaYk1icUxTN05zMnlvR0JhcVVhS2NuTWFRY3ZaWTBaQjhSV2xaT3p3bDNtZUciLCJtYWMiOiI1ZjZlNTJkZDY3ZmEyNjA3ZGQ0OTBkYjRkODkyOWFmMjlmNmI1YThjM2VlMWViNjRlOWU5MTgzY2Q5ZDViYzBhIiwidGFnIjoiIn0%3D"
)

COOKIES = {}
for raw_cookie in cookie_header.split(";"):
    if "=" in raw_cookie:
        key, value = raw_cookie.split("=", 1)
        COOKIES[key.strip()] = value.strip()

PAYLOADS = {
    "RSIAbove50": {
        "scan_clause": "( {cash} (  weekly close >=  52 and  daily ema( close,5 ) >  daily ema( close,26 ) and  daily ema( close,13 ) >  daily ema( close,26 ) and  daily close >  1 day ago close *  1.03 and  daily volume >  daily sma( volume,20 ) *  1.0 and  daily ema( close,5 ) >  daily ema( close,13 ) and  daily high =  daily max( 260 ,  daily high ) *  1 and  1 day ago close >  2 days ago close *  0.98 and  daily rsi( 14 ) >  55 ) )",
        "debug_clause": "groupcount( 1 where  weekly close >=  52),groupcount( 1 where  daily ema( close,5 ) >  daily ema( close,26 )),groupcount( 1 where  daily ema( close,13 ) >  daily ema( close,26 )),groupcount( 1 where  daily close >  1 day ago close *  1.03),groupcount( 1 where  daily volume >  daily sma( volume,20 ) *  1.0),groupcount( 1 where  daily ema( close,5 ) >  daily ema( close,13 )),groupcount( 1 where  daily high =  daily max( 260 ,  daily high ) *  1),groupcount( 1 where  1 day ago close >  2 days ago close *  0.98),groupcount( 1 where  daily rsi( 14 ) >  55)",
        "column_clause": " Daily Close as 'scan-column-default-close',  Daily \"close - 1 candle ago close / 1 candle ago close * 100\" as 'scan-column-default-percent-change', filternumber( daily close >  1 day ago close,1) as 'default-percent-change-conditional-filters-color',  Daily Volume as 'scan-column-default-volume'",
    },
    "ShortTermBreakouts": {
        "scan_clause": "( {cash} (  daily max( 5 ,  daily close ) >  6 days ago max( 120 ,  daily close ) *  1.05 and  daily volume >  daily sma( volume,5 ) and  daily close >  1 day ago close ) )",
        "debug_clause": "groupcount( 1 where  daily max( 5 ,  daily close ) >  6 days ago max( 120 ,  daily close ) *  1.05),groupcount( 1 where  daily volume >  daily sma( volume,5 )),groupcount( 1 where  daily close >  1 day ago close)",
        "column_clause": " Daily Close as 'scan-column-default-close',  Daily \"close - 1 candle ago close / 1 candle ago close * 100\" as 'scan-column-default-percent-change', filternumber( daily \"close - 1 candle ago close / 1 candle ago close * 100\" >  0,1) as 'default-percent-change-conditional-filters-color',  Daily Volume as 'scan-column-default-volume'",
    },
    "52wHighBreakouts": {
        "scan_clause":"( {cash} (  daily close >  1 day ago max( 240 ,  daily high ) ) )","debug_clause":"groupcount( 1 where  daily close >  1 day ago max( 240 ,  daily high ))","column_clause":" Daily Close as 'scan-column-default-close',  Daily \"close - 1 candle ago close / 1 candle ago close * 100\" as 'scan-column-default-percent-change', filternumber( daily close >  1 day ago close,1) as 'default-percent-change-conditional-filters-color',  Daily Volume as 'scan-column-default-volume'"}
}

aggregated_rows = {}

for tag, payload in PAYLOADS.items():
    response = requests.post(URL, headers=HEADERS, cookies=COOKIES, json=payload, timeout=30)
    print(f"\nTag: {tag} | Status code: {response.status_code}")

    try:
        content_encoding = response.headers.get("content-encoding", "").lower()
        decoded_body = response.text or ""

        if not decoded_body and brotli is not None and "br" in content_encoding:
            decoded_body = brotli.decompress(response.content).decode("utf-8", errors="replace")
        elif not decoded_body:
            decoded_body = response.content.decode("utf-8", errors="replace")

        data = json.loads(decoded_body)
        rows = data.get("data", [])
        if not rows:
            print(f"No matching records found for {tag}.")
            continue

        for item in rows:
            code = item.get("nsecode", "")
            name = item.get("name", "")
            key = (code, name)

            if key not in aggregated_rows:
                aggregated_rows[key] = {
                    "code": code,
                    "name": name,
                    "close": item.get("scan-column-default-close", ""),
                    "change": item.get("scan-column-default-percent-change", ""),
                    "volume": item.get("scan-column-default-volume", ""),
                    "tags": [tag],
                }
            elif tag not in aggregated_rows[key]["tags"]:
                aggregated_rows[key]["tags"].append(tag)
    except (ValueError, json.JSONDecodeError, AttributeError) as exc:
        print(f"Unable to parse response for {tag}: {exc}")
        print(decoded_body[:4000] if "decoded_body" in locals() else response.text[:4000])

print("\n SCRIPT: MULTI-PAYLOAD SCREENER RESULTS")
print("\nFormatted table:")
if not aggregated_rows:
    print("No matching records found.")
else:
    headers = ["CODE", "NAME", "TAGS", "CLOSE", "CHANGE %", "VOLUME"]
    rows_display = [
        [
            row["code"],
            row["name"],
            ", ".join(row["tags"]),
            row["close"],
            row["change"],
            row["volume"],
        ]
        for row in sorted(
            aggregated_rows.values(),
            key=lambda item: (-len(item["tags"]), item["code"], item["name"]),
        )
    ]

    col_widths = [max(len(str(row[i])) for row in [headers] + rows_display) for i in range(len(headers))]
    print(" | ".join(header.ljust(col_widths[i]) for i, header in enumerate(headers)))
    print("-+-".join("-" * width for width in col_widths))
    for row in rows_display:
        print(" | ".join(str(value).ljust(col_widths[i]) for i, value in enumerate(row)))
