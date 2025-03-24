import ntplib
import datetime
import socket
import time

def get_specific_time():
    try:
        # Force IPv4 resolution for the NTP server.
        addr_info = socket.getaddrinfo("ntp.pagasa.dost.gov.ph", 123, family=socket.AF_INET, type=socket.SOCK_DGRAM)
        ip_address = addr_info[0][4][0]
        ntp_client = ntplib.NTPClient()
        response = ntp_client.request(ip_address, port=123, version=3, timeout=10)
        
        # Get the Unix timestamp and convert to datetime
        ntp_timestamp = int(response.tx_time)
        ntp_datetime = datetime.datetime.fromtimestamp(ntp_timestamp)
        return ntp_datetime, ntp_timestamp
    except Exception as e:
        print("Error retrieving time:", e)
        return None, None

while True:
    dt, ts = get_specific_time()
    if dt:
        print("Datetime from NTP server:", dt, "Timestamp:", ts)
    else:
        print("Failed to retrieve time.")
    time.sleep(10)
