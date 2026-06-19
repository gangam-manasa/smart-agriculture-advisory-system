import pandas as pd

df = pd.read_excel("SensorHistory.xlsx")

df.columns = [
    "time",
    "temperature",
    "pressure",
    "humidity",
    "wind_speed",
    "wind_direction",
    "rainfall",
    "light_intensity"
]

def irrigation(temp, hum, rain):

    if rain > 2:
        return "No"

    elif temp > 32 and hum < 60:
        return "Yes"

    else:
        return "No"

df["irrigation"] = df.apply(
    lambda row: irrigation(
        row["temperature"],
        row["humidity"],
        row["rainfall"]
    ),
    axis=1
)

def heat_stress(temp, hum):

    if temp >= 38 and hum < 40:
        return "Severe"

    elif temp >= 34:
        return "High"

    elif temp >= 30:
        return "Moderate"

    else:
        return "Low"

df["heat_stress"] = df.apply(
    lambda row: heat_stress(
        row["temperature"],
        row["humidity"]
    ),
    axis=1
)

def water_requirement(temp, hum, rain):

    score = temp - (hum / 10) - rain

    if score >= 20:
        return "Very High"

    elif score >= 15:
        return "High"

    elif score >= 10:
        return "Medium"

    else:
        return "Low"

df["water_requirement"] = df.apply(
    lambda row: water_requirement(
        row["temperature"],
        row["humidity"],
        row["rainfall"]
    ),
    axis=1
)

def evaporation_risk(temp, hum, wind):

    if temp > 35 and hum < 50 and wind > 2:
        return "High"

    elif temp > 30:
        return "Medium"

    else:
        return "Low"

df["evaporation_risk"] = df.apply(
    lambda row: evaporation_risk(
        row["temperature"],
        row["humidity"],
        row["wind_speed"]
    ),
    axis=1
)


print(df[[
    "temperature",
    "humidity",
    "rainfall",
    "irrigation",
    "heat_stress",
    "water_requirement",
    "evaporation_risk"
]].head(10))

df.to_csv("processed_agri_data.csv", index=False)

print("Dataset saved successfully!")