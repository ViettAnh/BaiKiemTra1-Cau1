# Chương trình máy tính đơn giản
# Dành cho học sinh lớp 9-12

def main():
    print("===== CHƯƠNG TRÌNH MÁY TÍNH ĐƠN GIẢN =====\n")
    
    try:
        # Nhập hai số từ người dùng
        so_thu_nhat = float(input("Nhập số thứ nhất: "))
        so_thu_hai = float(input("Nhập số thứ hai: "))
        
        # Hiển thị menu các phép tính
        print("\nCác phép tính:")
        print("1. Cộng")
        print("2. Trừ")
        print("3. Nhân")
        print("4. Chia")
        
        # Nhập lựa chọn từ người dùng
        lua_chon = int(input("\nNhập lựa chọn của bạn (1-4): "))
        
        # Thực hiện phép tính dựa trên lựa chọn
        if lua_chon == 1:
            ket_qua = so_thu_nhat + so_thu_hai
            phep_tinh = "+"
        elif lua_chon == 2:
            ket_qua = so_thu_nhat - so_thu_hai
            phep_tinh = "-"
        elif lua_chon == 3:
            ket_qua = so_thu_nhat * so_thu_hai
            phep_tinh = "*"
        elif lua_chon == 4:
            # Kiểm tra chia cho 0
            if so_thu_hai == 0:
                print("\nLỗi: Không thể chia cho 0!")
                return
            ket_qua = so_thu_nhat / so_thu_hai
            phep_tinh = "/"
        else:
            print("\nLỗi: Lựa chọn không hợp lệ! Vui lòng chọn từ 1 đến 4.")
            return
        
        # Hiển thị kết quả
        print(f"\nKết quả: {so_thu_nhat} {phep_tinh} {so_thu_hai} = {ket_qua}")
        
    except ValueError:
        # Xử lý lỗi khi người dùng nhập không phải số
        print("\nLỗi: Vui lòng chỉ nhập số!")
    except Exception as e:
        # Xử lý các lỗi khác
        print(f"\nĐã xảy ra lỗi: {e}")

# Chạy chương trình khi file được thực thi trực tiếp
if __name__ == "__main__":
    main()
    
    # Hỏi người dùng có muốn tiếp tục không
    while True:
        tiep_tuc = input("\nBạn có muốn tiếp tục không? (y/n): ").lower()
        if tiep_tuc == 'y':
            main()
        elif tiep_tuc == 'n':
            print("\nCảm ơn bạn đã sử dụng chương trình!")
            break
        else:
            print("Vui lòng nhập 'y' hoặc 'n'.")