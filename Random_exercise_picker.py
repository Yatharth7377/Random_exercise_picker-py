import random

exercises = [
    "Burpees",
    "Jumping Jacks",
    "Mountain Climbers",
    "High Knees",
    "Push-ups",
    "Squats",
    "Lunges",
    "Planks",
    "Bicycle Crunches",
    "Sprints",
    "Skipping Rope",
]

def generate_workout():
    workout_time = random.randint(20, 30)  
    print(f"Workout Time: {workout_time} minutes\n")

    total_time = 0
    while total_time < workout_time:
        exercise = random.choice(exercises)
        exercise_time = random.randint(1, 5)  
        print(f"{exercise}: {exercise_time} minutes")
        total_time += exercise_time

        if total_time > workout_time:
            break

    print("\nWorkout Complete!")

if __name__ == "__main__":
    generate_workout()
