print("""
<!DOCTYPE html>
<html>
<body>
    <form action="入力データ02.py" method='post'>
    <p>生年月日:<br><input type="date" name="indate" value="2024/04/01"></p>
    <p>好きな数字(1-10):<br><input type="number" name="innumber" min="1" max="10"></p>
    <p>名前(英字のみ20字以内):<br><input type="text" name="inname" minlength="1" maxlength="20" required></p>
    <p>パスワード(最小4桁):<br><input type="password" name="inpassword" minlength="4" required></p>
    <p><input type="submit" value="確定"></p>
    </form>
</body>
</html>
"""
)
    
