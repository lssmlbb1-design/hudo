def calculate_volume(sets, repetitions, weight_kg):
    return sets * repetitions * weight_kg


def calculate_pace(distance_km, duration_minutes):
    return duration_minutes / distance_km


def get_recent_workouts(workouts, limit=5):
    sorted_workouts = sorted(
        workouts,
        key=lambda workout: workout["created_at"],
        reverse=True,
    )
    return sorted_workouts[:limit]


def get_max_weight(workouts, exercise):
    weights = [
        workout["weight_kg"]
        for workout in workouts
        if workout["exercise"] == exercise
        and workout["weight_kg"] is not None
    ]

    return max(weights, default=0)
