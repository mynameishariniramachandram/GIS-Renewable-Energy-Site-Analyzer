def renewable_score(solar, wind, temp):

    # weighted score
    solar_score = solar * 0.6
    wind_score = wind * 0.25
    temp_score = temp * 0.15

    total_score = solar_score + wind_score + temp_score

    # classification
    if total_score > 8:
        status = "Excellent Renewable Zone"
    elif total_score > 6:
        status = "Excellent Solar Farm"
    elif total_score > 4:
        status = "Hybrid Solar + Wind"
    else:
        status = "Wind Recommended"

    return total_score, status


# Example usage
solar = 6
wind = 5
temp = 30

score, label = renewable_score(solar, wind, temp)

print("Renewable Score:", score)
print("Recommendation:", label)