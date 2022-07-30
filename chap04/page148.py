sum = 0
for i in range(100, 201):
    if i % 2 != 0:
        sum = sum + i
print("合計値：", sum)

lang = "Python"
language = ["Python", "Perl", "Ruby"]
language1 = ["C#", "C++", "Java"]

if lang in language:
    print("インタプリター言語")
elif lang in language1:
    print("コンパイル言語")
else:
    print("不明")
