# 17413 단어 뒤집기 2
"""
문자열 S가 주어졌을 때, 이 문자열에서 단어만 뒤집으려고 한다.

먼저, 문자열 S는 아래와과 같은 규칙을 지킨다.

알파벳 소문자('a'-'z'), 숫자('0'-'9'), 공백(' '), 특수 문자('<', '>')로만 이루어져 있다.
문자열의 시작과 끝은 공백이 아니다.
'<'와 '>'가 문자열에 있는 경우 번갈아가면서 등장하며, '<'이 먼저 등장한다. 또, 두 문자의 개수는 같다.
태그는 '<'로 시작해서 '>'로 끝나는 길이가 3 이상인 부분 문자열이고, '<'와 '>' 사이에는 알파벳 소문자와 공백만 있다.
단어는 알파벳 소문자와 숫자로 이루어진 부분 문자열이고, 연속하는 두 단어는 공백 하나로 구분한다. 
태그는 단어가 아니며, 태그와 단어 사이에는 공백이 없다.

--------------
단어 뒤집는 문제
규칙이 존재한다
1. 알파벳 소문자, 숫자, 공백, 특수문자(< , >)
2. 시작과 끝에는 공백 아님
3. < > 번갈아가면서 등장 ( 갯수 차이는 없음)
4. < > 조합은 길이가 3이상임(사이에는 알파벳 소문자와 공백만존재)
5. 단어는 알파벳 소문자 + 숫자(단어는 공백으로 구분)
6. 태그는 단어가 아님(태그와 단어사이는 공백이없음)
"""

_string = input()
result = ""
is_tag = False
is_data = False
word = ""
count = 0
for w in _string:

    if w =="<":
        is_tag = True
        is_data = False
    elif w ==">":
        result += w 
        is_tag = False
        is_data = False
    elif w ==" ":
        if not is_tag:
            is_tag = False
    else:    
        is_data = True

    if is_tag:
        if word:
            result += word[-1::-1]
        result += w
        word =""
    elif is_data:
        if w == " ":
            result += word[-1::-1]+" "
            word =""
        elif len(_string)-1 == count:
            word += w
            result += word[-1::-1]
        else:
            word += w
    count+=1 
print(result)