from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # either knave or knight
    Or(AKnave, AKnight),

    # not both
    Not(And(AKnight, AKnave)),

    # if A is knave -- he is not both (
    Implication(AKnave, Not(And(AKnight, AKnave))),
    
    # if A is knight then he saying true
    Implication(AKnight, And(AKnave, AKnight))
    
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    
    # base cases for A 
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # base case for B
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # if A is Knave they both are not knave
    Implication(AKnave, Not(And(AKnave, BKnave))),
    Implication(AKnight, And(AKnave, BKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."

# now i will try to make it reusable 
same_type = Or(And(AKnave, BKnave), And(AKnight, BKnight))

knowledge2 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    
    Biconditional(AKnave, Not(same_type)),
    Biconditional(BKnave, same_type)
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
AStatementKnight = Symbol("A said 'I am a knight'")
AStatementKnave = Symbol("A said 'I am a knave'")
knowledge3 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),

    Or(AStatementKnight, AStatementKnave),
    Not(And(AStatementKnight, AStatementKnave)),

    # if A is Knight, Astatements is I am knight, else he is knave
    Implication(AKnight, Biconditional(AStatementKnight, AKnight)),
    Implication(AKnight, Biconditional(AStatementKnave, AKnave)),

    # if A is knave
    Implication(AKnave, Biconditional(AStatementKnight, Not(AKnight))),
    Implication(AKnave, Biconditional(AStatementKnave, Not(AKnave))),
    # B says A said he is knave
    Biconditional(AStatementKnave, BKnight),
    Biconditional(BKnave, Not(AStatementKnave)),

    # B says C is A knave
    Biconditional(BKnight, CKnave),
    Biconditional(BKnave, Not(CKnave)),

    # C says A is Knight
    Biconditional(CKnight, AKnight),
    Biconditional(CKnave, Not(AKnight))

)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
