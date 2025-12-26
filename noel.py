import time
import random
import os
import sys

# Các mã màu ANSI để làm đẹp trong terminal
colors = [
    '\033[91m', # Đỏ
    '\033[92m', # Xanh lá
    '\033[93m', # Vàng
    '\033[94m', # Xanh dương
    '\033[95m', # Tím
    '\033[96m', # Xanh cyan
    '\033[37m'  # Trắng
]
RESET = '\033[0m'
GREEN_BG = '\033[42m'
BROWN = '\033[33m' # Dùng tạm màu vàng tối cho thân cây

def clear_screen():
    # Hàm xóa màn hình để tạo hiệu ứng động
    os.system('cls' if os.name == 'nt' else 'clear')

def get_random_color():
    return random.choice(colors)

def draw_tree(height):
    clear_screen()
    print("\n" * 2) # Khoảng trống phía trên

    # Vẽ ngôi sao trên đỉnh
    print(" " * (height + 1) + get_random_color() + "🌟" + RESET)

    # Vẽ tán cây
    for i in range(height):
        spaces = " " * (height - i)
        # Phần lá cây màu xanh
        leaves = '\033[92m' + "*" * (2 * i + 1) + RESET
        
        # Chèn ngẫu nhiên các quả châu (ornaments)
        Decoration_chars = ["o", "+", "*", "@", "♥"]
        temp_list = list(leaves)
        if i > 1: # Chỉ trang trí từ tầng thứ 2 trở đi
            for _ in range(i): # Số lượng đồ trang trí tăng theo tầng
                pos = random.randint(len(temp_list)//3, len(temp_list) - len(temp_list)//3)
                if temp_list[pos] == "*": # Chỉ thay thế vị trí là lá cây
                     temp_list[pos] = get_random_color() + random.choice(Decoration_chars) + '\033[92m'
        
        print(spaces + "".join(temp_list))

    # Vẽ thân cây
    trunk_height = height // 3
    trunk_width = height // 3
    if trunk_width % 2 == 0: trunk_width += 1 # Đảm bảo chiều rộng lẻ để căn giữa
    
    trunk_spaces = " " * (height + 1 - trunk_width // 2 - 1)
    for _ in range(trunk_height):
        print(trunk_spaces + BROWN + "#" * trunk_width + RESET)

    # Vẽ lời chúc
    print("\n")
    message = " MERRY CHRISTMAS! "
    colored_message = ""
    for char in message:
        colored_message += get_random_color() + char
    
    print(" " * (height - len(message)//2 + 2) + colored_message + RESET)
    print("\n" + " " * (height - 5) + "Nhấn Ctrl+C để thoát")


# Vòng lặp chính để tạo hiệu ứng động
if __name__ == "__main__":
    try:
        while True:
            draw_tree(height=15) # Bạn có thể thay đổi chiều cao cây ở đây
            time.sleep(0.5) # Dừng 0.5 giây trước khi vẽ lại
    except KeyboardInterrupt:
        # Thoát nhẹ nhàng khi nhấn Ctrl+C
        print("\n" + RESET + "Giáng sinh vui vẻ! Tạm biệt.")
        sys.exit(0)