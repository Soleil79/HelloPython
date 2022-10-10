# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE

# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ

# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q



path = input('Введите имя файла для записи строки буквенных символов (text_words): ')

def fillString(init_path):
    with open(init_path, 'a', encoding='utf-8') as my_file: 
        text = str(input(f'Введите строку буквенных символов: '))      
        my_file.write(text)

fillString(path)

def coding(init_path, coding_path):
    
    with open(init_path, 'r', encoding='utf-8') as init_file,\
        open(coding_path, 'a', encoding='utf-8') as code_file:
        text = init_file.readline()
        count = 1
        res = ''
        for i in range(len(text)-1):
            if text[i] == text[i+1]:
                count += 1
            else:
                res = res + str(count) + text[i]
                count = 1
        if count > 1 or (text[len(text)-2] != text[-1]): # Если последний элемент отличен от предпоследнего
            res = res + str(count) + text[-1]
        code_file.write(res)

code_path = input('Введите имя файла для кодирования строки (text_code_words): ')
coding(path, code_path)



def decoding(coding_path, decoding_path):
    with open(coding_path, 'r', encoding='utf-8') as code_file,\
        open(decoding_path, 'a', encoding='utf-8') as decode_file:
        code_text = code_file.readline()
        count = ''
        res = ''
        for i in range(len(code_text)):
            if not code_text[i].isalpha():
                count += code_text[i]
            else:
                res = res + code_text[i] * int(count)
                count = ''
        decode_file.write(res)     


decode_path = input('Введите имя файла для декодирования строки (text_decode_words): ')
decoding(code_path, decode_path)


