def main():
    print("Welcome to the Career Path Expert System!")
    interests = input("Enter your interests separated by commas (e.g., Maths, Physics, Programming): ")
    interests = [i.strip().lower() for i in interests.split(',')]

    # Convert list to set for easier checking
    interest_set = set(interests)

    if 'maths' in interest_set and 'physics' in interest_set and 'chemistry' in interest_set:
        print("Suggested Career Path: Engineering Science")
    elif 'programming' in interest_set and 'maths' in interest_set:
        print("Suggested Career Path: Computer Engineering")
    elif 'maths' in interest_set and 'graphics' in interest_set:
        print("Suggested Career Path: Mechanical Engineering")
    else:
        print("No matching career path found. Please consult a career counselor for more options.")

if __name__ == "__main__":
    main()
sss
