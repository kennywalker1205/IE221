#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IE221 - Data Type Operator Examples
Sinh viên: Phan Trung Kiên
MSSV: 23520805

Tài liệu này chứa các ví dụ cụ thể về toán tử với từng kiểu dữ liệu
"""

print("=" * 80)
print("NHÓM 1: TOÁN TỬ SỐ HỌC".center(80))
print("=" * 80)

# PHÉP CỘNG (+)
print("\n### PHÉP CỘNG (+) ###")
print("Số:", 10 + 5, "=", 15)
print("Số thập phân:", 10.5 + 2.5, "=", 13.0)
print("Chuỗi:", "Hello" + " " + "World", "=", "Hello World")
print("List:", [1, 2] + [3, 4], "=", [1, 2, 3, 4])
print("Tuple:", (1, 2) + (3, 4), "=", (1, 2, 3, 4))
# Dict + Dict không được hỗ trợ trực tiếp (cần merge)
# Set + Set không được hỗ trợ (dùng | thay vào)

# PHÉP TRỪ (-)
print("\n### PHÉP TRỪ (-) ###")
print("Số:", 10 - 3, "=", 7)
print("Số âm:", -10 - 3, "=", -13)
print("Set:", {1, 2, 3} - {2}, "=", {1, 3})
# Chuỗi, List, Tuple không hỗ trợ phép trừ

# PHÉP NHÂN (*)
print("\n### PHÉP NHÂN (*) ###")
print("Số:", 5 * 3, "=", 15)
print("Chuỗi:", "ab" * 3, "=", "ababab")
print("List:", [1, 2] * 2, "=", [1, 2, 1, 2])
print("Tuple:", (1, 2) * 2, "=", (1, 2, 1, 2))
print("Chuỗi với số 0:", "ab" * 0, "=", "")
print("List với số âm:", [1, 2] * -1, "=", [])

# PHÉP CHIA (/)
print("\n### PHÉP CHIA (/) ###")
print("Số:", 10 / 3, "=", 3.3333333333333335)
print("Số nguyên chia:", 10 / 2, "=", 5.0)
# Lưu ý: Luôn trả về float
# Chia cho 0 gây ZeroDivisionError

# PHÉP CHIA LẤY PHẦN NGUYÊN (//)
print("\n### PHÉP CHIA LẤY PHẦN NGUYÊN (//) ###")
print("Số dương:", 10 // 3, "=", 3)
print("Số âm:", -10 // 3, "=", -4)  # Làm tròn về phía âm vô cùng
print("Cùng dấu:", 10 // 2, "=", 5)

# PHÉP CHIA LẤY DƯ (%)
print("\n### PHÉP CHIA LẤY DƯ (%) ###")
print("Số dương:", 10 % 3, "=", 1)
print("Số âm:", -10 % 3, "=", 2)  # Dấu tuân theo số chia
print("String formatting:", "Hello %s" % "World", "=", "Hello World")
print("String formatting số:", "Age: %d" % 25, "=", "Age: 25")
print("String formatting float:", "Pi: %.2f" % 3.14159, "=", "Pi: 3.14")

# PHÉP LŨY THỪA (**)
print("\n### PHÉP LŨY THỪA (**) ###")
print("Cơ bản:", 2 ** 3, "=", 8)
print("Mũ âm:", 2 ** -1, "=", 0.5)
print("Căn bậc 2:", 4 ** 0.5, "=", 2.0)
print("0 mũ 0:", 0 ** 0, "=", 1)

print("\n" + "=" * 80)
print("NHÓM 2: TOÁN TỬ SO SÁNH".center(80))
print("=" * 80)

# BẰNG (==) và KHÔNG BẰNG (!=)
print("\n### BẰNG (==) và KHÔNG BẰNG (!=) ###")
print("Số:", 5 == 5, "→", True)
print("Số:", 5 != 3, "→", True)
print("Chuỗi:", "abc" == "abc", "→", True)
print("List:", [1, 2] == [1, 2], "→", True)
print("Set:", {1, 2} == {2, 1}, "→", True, "(thứ tự không quan trọng)")
print("Dict:", {'a': 1} == {'a': 1}, "→", True)

# SO SÁNH LỚN HƠN, NHỎ HƠN
print("\n### SO SÁNH LỚN HƠN (>), NHỎ HƠN (<) ###")
print("Số:", 10 > 5, "→", True)
print("Số:", 10 >= 10, "→", True)
print("Số:", 3 < 5, "→", True)
print("Chuỗi:", "apple" < "banana", "→", True, "(so sánh từ điển)")
print("Chuỗi:", "apple" > "app", "→", True)
print("Chuỗi:", "A" < "a", "→", True, "(chữ hoa < chữ thường)")
# List, Tuple, Dict, Set không hỗ trợ > < >= <=

print("\n" + "=" * 80)
print("NHÓM 3: TOÁN TỬ LOGIC".center(80))
print("=" * 80)

# AND
print("\n### TOÁN TỬ AND ###")
print("5 and 3 →", 5 and 3, "(trả về giá trị thứ hai nếu giá trị đầu truthy)")
print("0 and 5 →", 0 and 5, "(trả về giá trị đầu nếu nó falsy)")
print("'hello' and 'world' →", 'hello' and 'world')
print("'' and 'world' →", '' and 'world', "(chuỗi rỗng là falsy)")
print("[1, 2] and [3, 4] →", [1, 2] and [3, 4])
print("[] and [3, 4] →", [] and [3, 4], "(danh sách rỗng là falsy)")

# OR
print("\n### TOÁN TỬ OR ###")
print("0 or 5 →", 0 or 5, "(trả về giá trị thứ hai nếu giá trị đầu falsy)")
print("3 or 5 →", 3 or 5, "(trả về giá trị đầu nếu nó truthy)")
print("'' or 'default' →", '' or 'default')
print("[1, 2] or [] →", [1, 2] or [])

# NOT
print("\n### TOÁN TỬ NOT ###")
print("not 0 →", not 0, "(0 là falsy)")
print("not 5 →", not 5, "(5 là truthy)")
print("not '' →", not '', "(chuỗi rỗng là falsy)")
print("not 'hello' →", not 'hello', "(chuỗi không rỗng là truthy)")
print("not [] →", not [], "(danh sách rỗng là falsy)")
print("not [1, 2] →", not [1, 2], "(danh sách không rỗng là truthy)")

print("\n### GIẢI THÍCH FALSY vs TRUTHY ###")
print("Falsy (coi như False):")
print("  - 0, 0.0")
print("  - '' (chuỗi rỗng)")
print("  - [] (danh sách rỗng)")
print("  - () (tuple rỗng)")
print("  - {} (dict rỗng)")
print("  - set() (set rỗng)")
print("  - None")
print("  - False")

print("\n" + "=" * 80)
print("NHÓM 4: TOÁN TỬ GÁN".center(80))
print("=" * 80)

# GÁN CƠ BẢN
print("\n### GÁN CƠ BẢN (=) ###")
a = 10
print(f"a = 10 → a = {a}")

# GÁN CỘNG (+=)
print("\n### GÁN CỘNG (+=) ###")
a = 5
a += 3
print(f"a = 5; a += 3 → a = {a}")

s = "Hello"
s += " World"
print(f"s = 'Hello'; s += ' World' → s = '{s}'")

lst = [1, 2]
lst += [3, 4]
print(f"lst = [1, 2]; lst += [3, 4] → lst = {lst}")
print("⚠️ Lưu ý: += với list sửa đổi list gốc (in-place)")

t = (1, 2)
t += (3, 4)
print(f"t = (1, 2); t += (3, 4) → t = {t}")
print("⚠️ Lưu ý: += với tuple tạo tuple mới (immutable)")

# GÁN TRỪ (-=)
print("\n### GÁN TRỪ (-=) ###")
a = 10
a -= 3
print(f"a = 10; a -= 3 → a = {a}")

s = {1, 2, 3}
s -= {2}
print(f"s = {{1, 2, 3}}; s -= {{2}} → s = {s}")

# GÁN NHÂN (*=)
print("\n### GÁN NHÂN (*=) ###")
a = 5
a *= 3
print(f"a = 5; a *= 3 → a = {a}")

s = "ab"
s *= 3
print(f"s = 'ab'; s *= 3 → s = '{s}'")

lst = [1, 2]
lst *= 2
print(f"lst = [1, 2]; lst *= 2 → lst = {lst}")

# GÁN CHIA (/, //, %)
print("\n### GÁN CHIA (/=, //=, %=) ###")
a = 10
a /= 2
print(f"a = 10; a /= 2 → a = {a} (luôn trả về float)")

b = 10
b //= 3
print(f"b = 10; b //= 3 → b = {b}")

c = 10
c %= 3
print(f"c = 10; c %= 3 → c = {c}")

# GÁN LŨY THỪA
print("\n### GÁN LŨY THỪA (**=) ###")
d = 2
d **= 3
print(f"d = 2; d **= 3 → d = {d}")

print("\n" + "=" * 80)
print("NHÓM 5: MEMBERSHIP OPERATORS (in, not in)".center(80))
print("=" * 80)

# IN - CHUỖI
print("\n### IN - CHUỖI ###")
print("'h' in 'hello' →", 'h' in "hello")
print("'x' in 'hello' →", 'x' in "hello")
print("'ell' in 'hello' →", 'ell' in "hello", "(tìm kiếm chuỗi con)")

# IN - LIST
print("\n### IN - LIST ###")
print("2 in [1, 2, 3] →", 2 in [1, 2, 3])
print("4 in [1, 2, 3] →", 4 in [1, 2, 3])
print("[1, 2] in [1, 2, 3] →", [1, 2] in [1, 2, 3], "(kiểm tra phần tử, không phải danh sách)")

# IN - DICT
print("\n### IN - DICT ###")
d = {'name': 'John', 'age': 30}
print(f"'name' in {d} →", 'name' in d, "(kiểm tra key)")
print(f"'John' in {d} →", 'John' in d, "(KHÔNG kiểm tra value)")
print(f"'John' in {d}.values() →", 'John' in d.values(), "(để kiểm tra value)")

# IN - SET
print("\n### IN - SET ###")
print("2 in {1, 2, 3} →", 2 in {1, 2, 3})

# NOT IN
print("\n### NOT IN ###")
print("'x' not in 'hello' →", 'x' not in "hello")
print("4 not in [1, 2, 3] →", 4 not in [1, 2, 3])

print("\n" + "=" * 80)
print("NHÓM 6: IDENTITY OPERATORS (is, is not)".center(80))
print("=" * 80)

# IS - SỐ
print("\n### IS - SỐ ###")
a = 5
b = 5
print(f"a = 5; b = 5; a is b →", a is b, "(Python cache số từ -5 đến 256)")

a = 300
b = 300
print(f"a = 300; b = 300; a is b →", a is b, "(số lớn không được cache)")

print("⚠️ Lưu ý: KHÔNG nên dùng 'is' so sánh giá trị số, dùng '==' thay vào")

# IS - CHUỖI
print("\n### IS - CHUỖI ###")
s1 = "hello"
s2 = "hello"
print(f"s1 = 'hello'; s2 = 'hello'; s1 is s2 →", s1 is s2, "(Python cache chuỗi nhỏ)")

# IS - LIST
print("\n### IS - LIST ###")
lst1 = [1, 2]
lst2 = [1, 2]
print(f"lst1 = [1, 2]; lst2 = [1, 2]; lst1 is lst2 →", lst1 is lst2, "(hai danh sách khác nhau)")

lst3 = lst1
print(f"lst3 = lst1; lst1 is lst3 →", lst1 is lst3, "(cùng một danh sách)")

print("\nSo sánh 'is' vs '==':")
print(f"lst1 == lst2 →", lst1 == lst2, "(so sánh giá trị)")
print(f"lst1 is lst2 →", lst1 is lst2, "(so sánh danh tính/địa chỉ bộ nhớ)")

# IS - NONE
print("\n### IS - NONE ###")
x = None
print(f"x = None; x is None →", x is None, "(None là singleton)")
print("⚠️ Luôn dùng 'is None' thay vì '== None'")

# IS - BOOL
print("\n### IS - BOOL ###")
a = True
b = True
print(f"a = True; b = True; a is b →", a is b, "(True là singleton)")

# IS NOT
print("\n### IS NOT ###")
lst1 = [1, 2]
lst2 = [1, 2]
print(f"lst1 is not lst2 →", lst1 is not lst2)

x = 5
print(f"x = 5; x is not None →", x is not None)

print("\n" + "=" * 80)
print("CÁC LƯU Ý ĐẶC BIỆT".center(80))
print("=" * 80)

# IMMUTABLE vs MUTABLE
print("\n### IMMUTABLE vs MUTABLE ###")
print("Immutable (bất biến):")
print("  - số, chuỗi, tuple, frozenset, bool")
print("  - += tạo đối tượng mới")

s = "hello"
id_before = id(s)
s += " world"
id_after = id(s)
print(f"\nVí dụ chuỗi:")
print(f"  s = 'hello'; id(s) = {id_before}")
print(f"  s += ' world'; id(s) = {id_after}")
print(f"  Khác nhau? {id_before != id_after} (tạo chuỗi mới)")

print("\nMutable (có thể thay đổi):")
print("  - list, dict, set")
print("  - += sửa đổi đối tượng gốc")

lst = [1, 2]
id_before = id(lst)
lst += [3, 4]
id_after = id(lst)
print(f"\nVí dụ list:")
print(f"  lst = [1, 2]; id(lst) = {id_before}")
print(f"  lst += [3, 4]; id(lst) = {id_after}")
print(f"  Giống nhau? {id_before == id_after} (sửa đổi list gốc)")

# CHIA LẤY DƯ VỚI SỐ ÂM
print("\n### CHIA LẤY DƯ VỚI SỐ ÂM ###")
print("10 % 3 =", 10 % 3)
print("-10 % 3 =", -10 % 3, "(dấu tuân theo số chia)")
print("10 % -3 =", 10 % -3)
print("-10 % -3 =", -10 % -3)
print("\nCông thức: a = (a // b) * b + (a % b)")
print(f"Kiểm tra: 10 = (10 // 3) * 3 + (10 % 3) = {(10 // 3) * 3} + {10 % 3} = {(10 // 3) * 3 + 10 % 3}")

# TUPLE
print("\n### LƯU Ý VỀ TUPLE ###")
print("(1, 2) + (3, 4) =", (1, 2) + (3, 4))
print("(10) + (5) = (10) + (5) =", (10) + (5), "(không phải tuple, là số)")
print("(10,) + (5,) =", (10,) + (5,), "(đây là tuple, dùng dấu phẩy)")

print("\n" + "=" * 80)
print("KẾT LUẬN".center(80))
print("=" * 80)
print("""
✓ Số học: chỉ dùng với số (trừ + với chuỗi/list/tuple, * với chuỗi/list/tuple)
✓ So sánh: == != dùng được với tất cả, >, <, >=, <= chỉ dùng với số và chuỗi
✓ Logic: and, or, not dùng được với tất cả, nhưng không phải luôn trả về True/False
✓ Gán: = luôn được, +=, *=, /= tùy kiểu dữ liệu, -= với set
✓ Membership: in, not in với chuỗi, list, tuple, dict (kiểm tra key), set
✓ Identity: is, is not so sánh địa chỉ, không phải giá trị (dùng với None, True, False)
""")