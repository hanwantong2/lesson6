# 创建字典
capitals = {
    "China": "Beijing",
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "Russia": "Moscow",
    "Brazil": "Brasília"
}

# a) 打印所有键值对
for country, capital in capitals.items():
    print(f"{country}: {capital}")

# b) 显示特定国家的首都
country = input("请输入一个国家名：")
if country in capitals:
    print(f"{country}的首都是{capitals[country]}")
else:
    print("该国家不在列表中。")

# c) 按国名字母顺序对词典内容进行排序和显示
sorted_capitals = sorted(capitals.items())
print("按国名排序后的首都列表：")
for country, capital in sorted_capitals:
    print(f"{country}: {capital}")
# 定义字母分数
scores = {
    'A': 1, 'B': 3, 'C': 5, 'D': 2, 'E': 1,
    'F': 10, 'G': 3, 'H': 5, 'I': 1, 'J': 8,
    'K': 2, 'L': 3, 'M': 2, 'N': 1, 'O': 1,
    'P': 2, 'Q': 8, 'R': 1, 'S': 1, 'T': 1,
    'U': 2, 'V': 4, 'W': 5, 'X': 5, 'Y': 4,
    'Z': 10
}

# 计算单词分数
word = input("请输入一个单词：").upper()
score = sum(scores.get(letter, 0) for letter in word)

print(f"{word} 的分数是：{score} 分")
# 创建学生和他们的语言技能列表
students_languages = {
    "Alice": ["English", "Chinese"],
    "Bob": ["Spanish", "French"],
    "Charlie": ["English", "German"],
    "David": ["Chinese"],
    "Eve": ["Spanish", "Chinese"]
}

# 确定学生掌握的不同语言
all_languages = set(language for languages in students_languages.values() for language in languages)
sorted_languages = sorted(all_languages)
print("学生掌握的语言：", sorted_languages)

# 打印懂中文的学生名单
chinese_speakers = [name for name, languages in students_languages.items() if "Chinese" in languages]
print("懂中文的学生名单：", chinese_speakers)