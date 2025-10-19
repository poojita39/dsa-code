import requests
import pandas as pd
import matplotlib.pyplot as plt

def fetch_covid_data():
    try:
        response = requests.get("https://api.covid19api.com/summary", timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None

def visualize_top_countries(data, top_n=10):
    countries = [c["Country"] for c in data["Countries"]]
    cases = [c["TotalConfirmed"] for c in data["Countries"]]

    df = pd.DataFrame({"Country": countries, "Total Cases": cases})
    top_countries = df.sort_values(by="Total Cases", ascending=False).head(top_n)

    plt.figure(figsize=(10, 6))
    plt.bar(top_countries["Country"], top_countries["Total Cases"], color="#6A5ACD")
    plt.title(f"Top {top_n} Countries by COVID-19 Confirmed Cases", fontsize=14, fontweight='bold')
    plt.xlabel("Country", fontsize=12)
    plt.ylabel("Total Confirmed Cases", fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def main():
    data = fetch_covid_data()
    if data and "Countries" in data:
        visualize_top_countries(data)
    else:
        print("No valid data available to visualize.")

if __name__ == "__main__":
    main()
