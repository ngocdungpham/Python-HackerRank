if __name__ == '__main__':
    """
    ASCII Art Hat Generator
    This module generates an ASCII art representation of a hat using the character 'H'.
    The hat consists of five main components:
    1. Top Cone (Hình chóp trên): A cone-shaped section that narrows from bottom to top
    2. Top Pillars (Hai cột trụ trên): Two vertical pillars supporting the top of the hat
    3. Middle Belt (Dây đai ở giữa): A horizontal band connecting the pillars
    4. Bottom Pillars (Hai cột trụ dưới): Two vertical pillars supporting the bottom of the hat
    5. Bottom Cone (Hình chóp ngược dưới): An inverted cone-shaped section that widens from top to bottom
    Args:
        thickness (int): An integer input that determines the size/thickness of all hat components.
                         Larger values create a larger hat with proportionally scaled dimensions.
    Output:
        Prints an ASCII art hat pattern to the console with centered and right-justified alignment
        based on the specified thickness parameter.
    Note:
        - The character 'H' is used to draw all components of the hat
        - Spacing and alignment are calculated based on the thickness value
        - Uses Python's string methods (center, rjust, ljust) for proper formatting
    """

    thickness = int(input())
    c = 'H'
    # 1. Top Cone (Hình chóp trên)
    for i in range(thickness):
        # Sửa: (i*2)+1 để bắt đầu từ 1 chữ H
        # Sửa: rjust/ljust dễ kiểm soát hơn center trong trường hợp này
        print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

    # 2. Top Pillars (Hai cột trụ trên)
    for i in range(thickness+1):
        # Sửa: Dùng dấu + thay vì dấu ,
        # Căn giữa cột 1 trong khoảng thickness*2
        # Căn giữa cột 2 trong khoảng thickness*6
        print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

    # 3. Middle Belt (Dây đai ở giữa)
    # Độ dài là (thickness+1) / 2
    for i in range((thickness+1)//2):
        print((c*thickness*5).center(thickness*6))

    # 4. Bottom Pillars (Hai cột trụ dưới)
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

    # 5. Bottom Cone (Hình chóp ngược dưới)
    for i in range(thickness):
        # Logic: Tạo hình chóp như phần 1, nhưng đẩy hết sang phải (rjust)
        # width tổng là thickness*6
        print(((c*(thickness-i-1)).rjust(thickness) + c + (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))