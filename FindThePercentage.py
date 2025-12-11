if __name__ == '__main__':
    n = int(input())   # Nhập số lượng sinh viên
    student_marks = {} # Tạo dictionary rỗng để lưu điểm trung bình của từng sinh viên
    
    for _ in range(n): # Lặp n lần để nhập dữ liệu cho từng sinh viên
        name, *line = input().split()   # Nhập tên và các điểm, tách thành list
        scores = list(map(float, line)) # Chuyển các điểm từ string sang float
        student_marks[name] = sum(scores) / len(scores) # Tính điểm trung bình và lưu vào dict
    
    query_name = input() # Nhập tên sinh viên cần truy vấn
    
    for name, scores in student_marks.items(): # Duyệt qua từng cặp (key, value) trong dict
        if name == query_name:                 # Nếu tên trùng với tên cần tìm
            print(f"{scores:.2f}")             # In ra điểm trung bình với 2 chữ số thập phân
