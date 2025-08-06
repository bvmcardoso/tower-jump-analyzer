import pandas as pd

from analyzer import analyze_intervals

def test_analyze_intervals_tower_jump_detection():
    df = pd.DataFrame({
        "LocalDateTime": pd.to_datetime([
            "2022-02-08 10:00",
            "2022-02-08 10:02",
            "2022-02-08 10:05",
            "2022-02-08 10:07"
        ]),
        "State": ["NY", "CT", "NY", "CT"],
        "Latitude": [40.1, 40.2, 40.3, 40.4],
        "Longitude": [-73.1, -73.2, -73.3, -73.4],
        "Valid": [True, True, True, True]
    })

    result = analyze_intervals(df)

    assert len(result) == 4, "Should return 4 records"
    assert "TowerJump" in result.columns
    assert "Confidence" in result.columns
    assert result["Confidence"].min() >= 50
    assert "Yes" in result["TowerJump"].values
