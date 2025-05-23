from datetime import datetime, timedelta

start_date = datetime(2021, 1, 4)  # Bắt đầu từ thứ Hai đầu tiên của 2021
end_date = datetime(2025, 12, 29)  # Kết thúc vào thứ Hai cuối cùng của 2025
current_date = start_date

# Mở file để ghi
with open("dates_2021_2025_weekly.txt", "w") as f:
    while current_date <= end_date:
        year = current_date.year
        month = current_date.month
        day = current_date.day  # Lấy số tuần trong năm
        formatted_date = f"{year}.{month:02d}{day:02d}"
        f.write(formatted_date + "\n")
        current_date += timedelta(weeks=1)
