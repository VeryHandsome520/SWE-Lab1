def calculate_grade(scores):
    # ตรวจสอบเพื่อป้องกัน Bug กรณีลิสต์ว่าง (ZeroDivisionError)
    if not scores:
        return "F", 0.0  # หรืออาจคืนค่าเป็น None, 0 ตามความเหมาะสมของระบบ
    
    # ใช้ฟังก์ชัน sum() เพื่อหาผลรวมแทนการใช้ loop
    total = sum(scores)
    average = total / len(scores)
    
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"
        
    return grade, average

# ทดสอบการใช้งานด้วยข้อมูลปกติ
scores = [85, 92, 78, 88, 95]
print("ผลลัพธ์ปกติ:", calculate_grade(scores))

# ทดสอบกรณีลิสต์ว่าง
empty_scores = []
print("ผลลัพธ์กรณีลิสต์ว่าง:", calculate_grade(empty_scores))
