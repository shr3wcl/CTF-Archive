# Description
Bat Problems
On a chilly Halloween night, the town of Hollowville was shrouded in a veil of mystery. The infamous "Haunted Hollow House", known for its supernatural tales, concealed a cryptic document. Whispers in the town suggested that the one who could solve its riddle would reveal a beacon of hope. As an investigator, your mission is to decipher the script's enigmatic sorcery, break the curse, and unveil the flag to become Hollowville's savior.
# Source

- [Source](./src/)
- [Zip](./forensics_bat_problems.zip)

# Solve

- File bat được cung cấp là một payload mã độc mà attack đã viết và nó đã bị mã hóa để anti anti-virus @@ 😱
- Để xem payload gốc là gì thì chỉ cần in ra payload thay vì thực thi nó. Đây là file được viết để in ra [decodePayload.bat](./decodePayload.bat) (Không có virus, yên tâm 😁). (Kết quả nằm trong file [decodeFlag.py](./decodeFlag.py))
- Chạy file bat thì được một mã base64.
- Giải mã và thu được flag. [decodeFlag.py](./decodeFlag.py)

`🚩Flag: HTB{0bfusc4t3d_b4t_f1l3s_c4n_b3_4_m3ss}`