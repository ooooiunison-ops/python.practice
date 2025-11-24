a = 10
b = 0

try:
    print('演算開始')
    c = a / b
    print(c)
except:
    print('0による除算エラーです')


x = '20'
y = 5

try:
    print('演算開始')
    z = x + y
    print(z)
except:
    print('異なるデータ型での演算によるエラー')

a = '20'
b = '5'

try:
    print('演算開始')
    c = a + b
    print(c)
except:
    print('異なるデータ型での演算によるエラー')
else:
    print('演算完了')


x = 'beutiful'
y = 'dream'
try:
    print('演算スタート')
    z = x + y
    print(z)
except:
    print('異なるデータ型どうしで演算しています')
else:
    print('正常に演算が完了しました')

x = '20'
y = '24'

try:
    print('文字列の演算スタート')
    z = x + y
    print(z)
except:
    print('文字列以外で演算しています')
else:
    print('正常に演算完了')
finally:
    print('コードの処理を終了します。')

x = {'name':'Mike','age':18}
try:
    print(x['name'])
except:
    print('キーが辞書に存在しません')
else:
    print('キーにアクセス完了')
finally:
    print('------')

x = [1,2,3]
try:
    print(a[2])
except IndexError:
    print('リストのインデックスが範囲外です')
except NameError:
    print('定義されていない変数を使用しています')
finally:
    print('コードの処理を終了します')

x = 6
y = 0

try:
    z = x /y
    print(z)
except ZeroDivisionError:
    print('0による除算エラーです')
except TypeError:
    print('異なるデータ型どうしによる演算してます')
finally:
    print('コードの処理を終了します')

a = '15'
b = 5
try:
    c = a/b
    print(c)
except ZeroDivisionError:
    print('0による除算エラーです')
except Exception as e:
    print(f'予期せぬエラー:{e}')
finally:
    print('finish')

x = 100
y = 0
try:
    print('演算スタート')
    z = x / y
    print(z)
except TypeError:
    print('数値以外で演算しています')
except Exception as e:
    print(f'予期せぬエラー:{e}')
finally:
    print('finish')

a = 'Score'
b = 90
try:
    c = a + b
    print(c)
except:
    print('異なるデータ型同士で計算しています')

x = [4,5,6]
try:
    print(x[1])
except:
    print('リストのインデックスが範囲外です')
else:
    print('取得完了')

a = 8
b = 0
try:
    print('演算開始')
    c = a / b
    print(c)
except:
    print('0による除算エラーです')
else:
    print('正常に演算完了')
finally:
    print('コードの処理を終了します')

x = 20
y = '25'
try:
    print('演算スタート')
    z = a + y
    print(z)
except TypeError:
    print('異なるデータ型どうしで演算しています')
except NameError:
    print('定義されていない変数を使用しています')
finally:
    print('コード処理ここまで')

a = [7,8,9]
try:
    print(a[3])
except NameError:
    print('定義されていない変数を使用しています')
except Exception as e:
    print(f'想定外のエラー:{e}')
finally:
    print('コードの処理を終了します')
    