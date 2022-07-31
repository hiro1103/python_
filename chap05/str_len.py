import unicodedata

title = "WINGSプロジェクト"
print("文字数：", len(title))

data = "WINGSプロジェクト２０２０"
count = 0
for ch in data:
    if unicodedata.east_asian_width(ch) in "FWA":
        count = count+2
    else:
        count = count+1
print("バイト数：", count)

data1 = "Wings Project"
data2 = "self learn python"
data3 = "Fußball"

print(data1.lower())
print(data1.upper())
print(data1.swapcase())
print(data2.capitalize())
print(data2.title())
print(data3.lower())
print(data3.casefold())
