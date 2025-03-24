import ntplib
import datetime

def get_specific_time():
    try:
        ntp_client = ntplib.NTPClient()
        response = ntp_client.request("ntp.pagasa.dost.gov.ph", version=3)
        # Use the transmit time from the NTP server directly.
        ntp_timestamp = int(response.tx_time)
        # Optionally, convert to a datetime object (the timestamp is already correct)
        ntp_datetime = datetime.datetime.fromtimestamp(ntp_timestamp)
        print("Datetime from NTP server:", ntp_datetime)
        return ntp_timestamp
    except Exception as e:
        print("Error retrieving time:", e)
        return None

print("Time:", get_specific_time())
