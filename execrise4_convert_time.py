from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo

def main():
    time_now = datetime.now()
    print("Hiện tại ở địa phương: ", time_now.strftime("%Y-%m-%d %H:%M:%S"))

    time_utc = time_now.astimezone(timezone.utc)
    print("Hiện tại ở chuẩn quốc tế: ", time_utc.strftime("%Y-%m-%d %H:%M:%S %Z%z"))

    time_japan = time_now.astimezone(ZoneInfo("Asia/Tokyo"))
    print("Hiện tại ở nhật bản: ", time_japan.strftime("%Y-%m-%d %H:%M:%S %Z%z"))

    #các format ngày tháng
    print("Định dạng IOS", time_now.isoformat())
    print("Định dạng dd/mm/yyyy", time_now.strftime("%d/%m/%Y"))
    print("Định dạng mm/dd/yyyy", time_now.strftime("%m/%d/%Y"))
    print("Định dạng yyyy-mm-dd", time_now.strftime("%Y-%m-%d"))

    future_7day = time_now + timedelta(days=7)
    print(f"Thời gian 7 ngày sau: ", future_7day.strftime("%Y-%m-%d %H:%M:%S %Z%z"))

    last_7day = time_now - timedelta(days=7)
    print(f"Thời gian 7 ngày trước: ", last_7day.strftime("%Y-%m-%d %H:%M:%S %Z%z"))


if __name__ == "__main__":
    main()