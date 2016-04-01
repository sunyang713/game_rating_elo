


import glicko2
import timeit

def exampleCase():

    P1 = glicko2.Player()
    P2 = glicko2.Player()

    P1_R = input("P1 rating:")
    P1_D = input("P1 dev: ")
    P1_V = input("P1 vola: ")

    P2_R = input("P2 rating:")
    P2_D = input("P2 dev:")
    P2_V = input("P2 vola: ")

    winner = input("Who won? P1 or P2? :: ")

    if winner == 1:
        a = 1;
        b = 0;
    else:
        a = 0;
        b = 1;

    P1 = glicko2.Player(P1_R, P1_D, P1_V)
    P2 = glicko2.Player(P2_R, P2_D, P1_V)


    P1c = P1

    # Following the example at:
    # http://math.bu.edu/people/mg/glicko/glicko2.doc/example.html
    # Pretend Ryan (of rating 1500 and rating deviation 350)
    # plays players of ratings 1400, 1550 and 1700
    # and rating deviations 30, 100 and 300 respectively
    # with outcomes 1, 0 and 0.


    P1.update_player([x for x in [P2.rating]],
            [x for x in [P2.rd]], [a])
    
    print("P1 New Rating: " + str(P1.rating))
    print("P1 New Dev: " + str(P1.rd))
    print("P1 New Vol: " + str(P1.vol))


    P2.update_player([x for x in [P1c.rating]],
            [x for x in [P1c.rd]], [b])

    print("P2 New Rating: " + str(P2.rating))
    print("P2 New Dev: " + str(P2.rd))
    print("P2 New Vol: " + str(P2.vol))





if __name__ == "__main__":
    exampleCase()
