from urllib.request import Request, urlopen, URLError
from datetime import datetime


# Data source URLs, date required in format: YYYY-MM-DD (eg. "2024-02-22")
class DataSource:
    SEEKING_ALPHA = "https://seekingalpha.com/api/v3/earnings_calendar/tickers?filter[selected_date]={}&filter[currency]=USD"
    STOCK_TWITS = "https://api.stocktwits.com/api/2/discover/earnings_calendar?date={}"
    NASDAQ = (
        "https://api.nasdaq.com/api/calendar/earnings?date={}"  # (TODO), fetching hangs
    )


def fetch_data(source, date):
    url = getattr(DataSource, source)
    try:
        req = Request(url=url.format(date), headers={"User-Agent": "Mozilla/5.0"})
        return urlopen(req).read()
    except URLError as e:
        print(f"Error fetching {source} data: {e}")
        return None


if __name__ == "__main__":
    date = datetime.today().strftime("%Y-%m-%d")

    # Fetch Seeking Alpha data
    seeking_alpha_data = fetch_data("SEEKING_ALPHA", date)
    if seeking_alpha_data:
        print("Seeking Alpha data:", seeking_alpha_data)

    # Fetch StockTwits data
    stock_twits_data = fetch_data("STOCK_TWITS", date)
    if stock_twits_data:
        print("StockTwits data:", stock_twits_data)

    # Fetch NASDAQ data (TODO)
    # nasdaq_data = fetch_data("NASDAQ", date)
    # if nasdaq_data:
    #     print("NASDAQ data:", nasdaq_data)
