# https://stepik.org/lesson/13229/step/5?after_pass_reset=true&auth=login&unit=3415
# Решается по алгоритму Эвклида
def gcd(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    else:
        return gcd(max(a, b) % min(a, b), min(a, b))


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()