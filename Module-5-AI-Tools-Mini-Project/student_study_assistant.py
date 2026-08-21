import random

STUDY_TOPICS = {
    "python": {
        "description": "Python is a programming language widely used in AI and Data Science.",
        "steps": [
            "Learn variables and data types",
            "Practice if-else statements",
            "Learn loops",
            "Learn functions",
            "Practice lists and dictionaries"
        ]
    },

    "machine learning": {
        "description": "Machine Learning allows computers to learn patterns from data.",
        "steps": [
            "Understand supervised and unsupervised learning",
            "Learn training and testing data",
            "Study classification and regression",
            "Learn Scikit-learn",
            "Build a beginner ML project"
        ]
    },

    "artificial intelligence": {
        "description": "Artificial Intelligence focuses on building systems that perform intelligent tasks.",
        "steps": [
            "Understand AI basics",
            "Learn Machine Learning",
            "Explore Deep Learning",
            "Study real-world AI applications",
            "Build a simple AI project"
        ]
    },

    "data science": {
        "description": "Data Science involves collecting, cleaning, analyzing and interpreting data.",
        "steps": [
            "Learn Python",
            "Learn NumPy",
            "Learn Pandas",
            "Learn data visualization",
            "Build a data analysis project"
        ]
    }
}


def study_assistant(topic):

    topic = topic.lower().strip()

    if topic in STUDY_TOPICS:

        information = STUDY_TOPICS[topic]

        print("\n" + "=" * 50)
        print(f"STUDY GUIDANCE: {topic.title()}")
        print("=" * 50)

        print("\nOverview:")
        print(information["description"])

        print("\nRecommended Study Plan:")

        for number, step in enumerate(information["steps"], start=1):
            print(f"{number}. {step}")

    else:

        print("\nTopic not found.")

        print("\nAvailable topics:")

        for available_topic in STUDY_TOPICS:
            print("-", available_topic.title())


def study_time_recommendation(hours):

    if hours <= 1:
        return "Focus on one important concept and complete a short practice session."

    elif hours <= 3:
        return "Divide your time between learning, practice and revision."

    else:
        return "Use a structured schedule with learning, practice, revision and breaks."


def productivity_tip():

    tips = [
        "Break large tasks into smaller tasks.",
        "Set a clear study goal before starting.",
        "Practice what you learn instead of only reading.",
        "Take short breaks during long study sessions.",
        "Review difficult topics regularly."
    ]

    return random.choice(tips)


def run_study_assistant():

    print("\n==========================================")
    print("   AI-POWERED STUDENT STUDY ASSISTANT")
    print("==========================================")

    print("\nAvailable topics:")

    for topic in STUDY_TOPICS:
        print("-", topic.title())

    topic = input("\nEnter the topic you want to study: ")

    study_assistant(topic)

    try:

        hours = float(input("\nHow many hours can you study today? "))

        if hours > 0:
            print("\nStudy Recommendation:")
            print(study_time_recommendation(hours))
        else:
            print("Please enter a positive number.")

    except ValueError:
        print("Please enter a valid number.")

    print("\nProductivity Tip:")
    print(productivity_tip())

    print("\nThank you for using the Student Study Assistant!")


run_study_assistant()
