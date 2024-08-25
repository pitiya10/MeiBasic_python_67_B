# กำหนดช่วงเลข
start = 21
end = 40

# สร้างลิสต์สำหรับจำนวนคี่และจำนวนคู่
odd_numbers = []
even_numbers = []

# ตรวจสอบแต่ละหมายเลขในช่วงที่กำหนด
for number in range(start, end + 1):
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

# แสดงผลลัพธ์
print("จำนวนคี่:", odd_numbers)
print("จำนวนคู่:", even_numbers)
