pushups = {
    "exercise": "push-up",
    "sets": 3,
    "reps": 10,
    "notes": "tough"
}

# iterating dict gives keys
[print(x) for x in pushups]

# accessing keys
pushups["sets"] = 12
del pushups["notes"]
pushups["workout_notes"] = "tough"


# ================ Nested Dictionaries
workout_plan = {
    "Push-ups": {
        "sets": 3,
        "reps": 15,
        "notes": "Keep your back straight, hands shoulder-width apart."
    },
    "Squats": {
        "sets": 4,
        "reps": 12,
        "notes": "Go as low as you can while maintaining proper form."
    },
    "Plank": {
        "sets": 3,
        "reps": "Hold for 60 seconds",
        "notes": "Engage your core and keep your body in a straight line."
    },
    "Lunges": {
        "sets": 3,
        "reps": 10,
        "notes": "Each leg. Step forward and lower your body until your front knee is at a 90-degree angle."
    },
    "Bicep Curls": {
        "sets": 3,
        "reps": 12,
        "notes": "Use dumbbells, keep your elbows close to your body."
    }
}

lunge_notes = workout_plan["Lunges"]["notes"]
print(lunge_notes)

# Iterating over a dictionary
# The .items() method converts the dictionary into an iterable collection of key-value pairs (tuples).
# Each tuple contains the key as the first element and the value as the second.
# We can use a for loop to access both the key and value.

for key, value in pushups.items():
    print(f"{key.upper()}: {value}")

# can do list comprehension as shown earlier too
# -- Fairly sure that print statement INSIDE list comprehension is code smell
[print(f"{x.upper()}: {pushups[x]}") for x in pushups]

# can put in variable first to avoid that
outputs = [f"{x.upper()}: {pushups[x]}" for x in pushups]
print(outputs)