from experta import *
class StudentFacts(Fact):
    pass
class CareerExpertSystem(KnowledgeEngine):
    @Rule(StudentFacts(likes='Maths'), StudentFacts(likes='Physics'),StudentFacts(likes='Chemistry'))
    def enginering_science(self):
        print("Suggested Career Path: Engineering Science")
    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Maths'))
    def computer_enginering(self):
        print("Suggested Career Path: Computer Engineering")
    @Rule(StudentFacts(likes='maths'), StudentFacts(likes='graphics'))
    def mechanical_enginering(self):
        print("Suggested Career Path: Mechanical Engineering")
    
def main():
    engine = CareerExpertSystem()
    engine.reset()
    print("Welcome to the Career Path Expert System!")
    interests = input("Enter your interests separated by commas (e.g., Maths, Physics, Programming): ").split(',')
    for interest in interests:
        engine.declare(StudentFacts(likes=interest.strip()))
    engine.run()
if __name__ == "__main__":
    main()
