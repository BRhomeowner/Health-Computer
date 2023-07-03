def get_bmi(height, weight):
    height /= 100
    bmi = weight / (height ** 2)
    bmi = round(bmi, 1)
    return bmi
def get_bmr(sex, height, weight, age):
    if sex == "男":
        bmr = 66 + (13.7 * weight + 5 * height - 6.8 * age)
    elif sex == "女":
        bmr = 655 + (9.6 * weight + 1.8 * height - 4.7 * age)
    bmr = round(bmr, 2)
    return bmr
def get_tdee(sex, height, weight, age, times):
        bmr = get_bmr(sex, height, weight, age)
        tdee = bmr * times
        tdee = round(tdee, 2)
        return tdee
print("歡迎使用綜合健康計算機")
print("(1)計算bmi")
print("(2)計算bmr")
print("(3)計算tdee")
mode = input("請選擇要計算的項目(輸入1 or 2 or 3):")
if mode == "1":
    height = float(input("請輸入您的身高(公分):"))
    weight = float(input("請輸入您的體重(公斤):"))
    bmi = get_bmi(height, weight)
    print(f"您的bmi為{bmi}")
elif mode == "2":
    sex = input("請輸入您的性別(輸入男or女):")
    height = float(input("請輸入您的身高(公分):"))
    weight = float(input("請輸入您的體重(公斤):"))
    age = int(input("請輸入您的年齡:"))
    bmr = get_bmr(sex, height, weight, age)
    print(f"您的基礎代謝率(bmr)為{bmr}")
elif mode == "3":
    sex = input("請輸入您的性別(輸入男or女):")
    height = float(input("請輸入您的身高(公分):"))
    weight = float(input("請輸入您的體重(公斤):"))
    age = int(input("請輸入您的年齡:"))
    print("(1)久坐，幾乎沒運動\n"+"(2)每周低強度運動1~3天\n"+"(3)每周中強度運動3~5天\n"+"(4)每周高強度運動6~7天\n"+"(5)每天高強度訓練")
    exer = input("請選擇您的運動量(輸入1~5)")
    times = 0
    if exer == "1":
        times = 1.2
    elif exer == "2":
        times = 1.375
    elif exer == "3":
        times = 1.55
    elif exer == "4":
        times = 1.725
    elif exer == "5":
        times = 1.9
    tdee = get_tdee(sex, height, weight, age, times)
    print(f"您的總熱量消耗(tdee)為{tdee}")