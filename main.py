from Display import display
from keypad import get_input
from Fingerprint import register_finger
from Register import s_data
ch = 0
display(ch)
ch = get_input()
print(type(ch))
if ch == "1":
    sid = get_input("Type Your ID: ")
    fid = register_finger()
    s_data(sid,fid)



