
def calculate_sign_difference(s: str) -> int:
    return s.count("+") - s.count("-")

S: str = input()
print(S.count("+")-S.count("-"))