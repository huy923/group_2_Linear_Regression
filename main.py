import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from sklearn.linear_model import LinearRegression
import glob

def main():
    filer = glob.glob("*.csv")
    if len(filer) == 0:
        print("Không tìm thấy file")
        exit()
    for file in filer:
        print(file)
        df = pd.read_csv(file)

        print(df.head())
        df["time"] = pd.to_datetime(df["time"], format="%Y/%m/%d")

        df["time_numeric"] = df["time"].dt.year + df["time"].dt.month / 100 + df["time"].dt.day / 10000

        X = df["time_numeric"].values.reshape(-1, 1)
        Y = df["money"].values

        model = LinearRegression()
        model.fit(X, Y)

        Y_pred = model.predict(X)

        plt.figure(figsize=(10, 2))
        plt.scatter(df["time"], df["money"], color="blue", label="Dữ liệu gốc")
        plt.plot(df["time"], Y_pred, color="red", linewidth=2, label="Hồi quy tuyến tính")

        ax = plt.gca()
        ax.xaxis.set_major_locator(mdates.MonthLocator())  
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%M"))
        

        plt.xlabel("Thời gian")
        plt.ylabel("Giá cả")
        plt.title("Hồi quy tuyến tính")
        plt.legend()
        name = file.replace(".csv", "") + ".png"
        plt.savefig(name)
        plt.show()

if __name__ == "__main__":
    main()