nhan_vien = [
    {
        "Name": "Huy",
        "Salary per hour": 25,
        "Hour": 30
    },
    {
        "Name": "Quan",
        "Salary per hour": 25,
        "Hour": 20
    },
    {
        "Name": "Duc",
        "Salary per hour": 30,
        "Hour": 40
    },
]
print(nhan_vien)
total = 0
for index in range(len(nhan_vien)):
    print(nhan_vien[index]["Name"],end=': ')
    print(nhan_vien[index]["Salary per hour"] * nhan_vien[index]["Hour"])
    total += (nhan_vien[index]["Salary per hour"] * nhan_vien[index]["Hour"])
print("Tong luong:",total)