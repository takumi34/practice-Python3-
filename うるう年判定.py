#与えられた自然数がうるう年か判定します

a = int(input())

if a % 400 == 0:
    print("うるう年です")
elif a % 100 == 0:
    print("うるう年ではありません")
elif a % 4 == 0:
    print("うるう年です")
else:
    print("うるう年ではありません")
