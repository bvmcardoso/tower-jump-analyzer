import pandas as pd
from datetime import timedelta

def analyze_intervals(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    valid_df = df[df["Valid"]].copy()

    # Identifica mudança de estado para criar grupos
    valid_df["StateChanged"] = valid_df["State"] != valid_df["State"].shift()
    valid_df["Group"] = valid_df["StateChanged"].cumsum()

    # Agrupamento por blocos consecutivos de mesmo estado
    grouped = valid_df.groupby("Group")
    interval_data = []

    previous_end = None

    for group_id, group in grouped:
        start = group["LocalDateTime"].min()
        end = group["LocalDateTime"].max()
        duration_min = (end - start).total_seconds() / 60
        state = group["State"].iloc[0]

        # Confiança
        confidence = 50
        if duration_min >= 15:
            confidence = 80
        if duration_min > 30:
            confidence = 100

        # Tower jump (gap com grupo anterior <= 15 min)
        tower_jump = False
        if previous_end is not None and (start - previous_end) <= timedelta(minutes=15):
            tower_jump = True

        previous_end = end

        # Aplica para cada linha do grupo
        for _, row in group.iterrows():
            interval_data.append({
                "LocalDateTime": row["LocalDateTime"],
                "State": row["State"],
                "TowerJump": "Yes" if tower_jump else "No",
                "Confidence": confidence,
                "Valid": True
            })

    # Linhas inválidas
    invalid_df = df[~df["Valid"]]
    for _, row in invalid_df.iterrows():
        interval_data.append({
            "LocalDateTime": row.get("LocalDateTime"),
            "State": row.get("State"),
            "TowerJump": "N/A",
            "Confidence": 0,
            "Valid": False
        })

    final_df = pd.DataFrame(interval_data)
    final_df = final_df.sort_values(by="LocalDateTime").reset_index(drop=True)
    return final_df
