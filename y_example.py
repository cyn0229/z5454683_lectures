import pandas as pd


def predict_next_day_price(df):
    last_5_days = df.tail(5)
    mean_adj_close = last_5_days['Adj Close'].mean()
    mean_adj_close = round(mean_adj_close, 4)
    return mean_adj_close

def main():
    df = pd.read_csv("Equity.csv")
    predicted_price = predict_next_day_price(df)
    print(f"The predicted next day's Adj Close price is: {predicted_price}")


if __name__ == '__main__':
    main()