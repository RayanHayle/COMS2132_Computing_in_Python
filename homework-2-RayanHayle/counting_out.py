# TODO: Implement the "Counting Out" game for problem 1.2
'''
Josephus Problem 
1. You have n players and a fixed number k.
2. They are numbered from 1 to n. The players are counted proceeding in a clockwise direction.
3. The first k - 1 players are skipped. The k-th player is "counted out" and leaves the circle.
4. Then the next k - 1 players are skipped, etc.
5. The single player who remains in the end is the winner.
6. Data structure: basic list '''

def josephus(n, k):
    people = [i for i in range(1, n + 1)]  # List of players
    k = k-1  # Adjust k for zero-based indexing
    index = 0  # Start index

    while len(people) > 1:
        # Print skipped players before elimination. main issue: fized
        for _ in range(k):
            print(people[index])
            index = (index + 1) % len(people)
        
        eliminated_player = people.pop(index)
        print(f"{eliminated_player} is out.")
        
        # remainder: when out of bound 
        if index >= len(people):
            index = 0  
    #winner
    print(f"{people[0]} wins.")

if __name__ == "__main__":
    n = int(input("What is n? ")) 
    k = int(input("What is k? "))  
    josephus(n, k)
