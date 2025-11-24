print("""
<!DOCTYPE html>
<html>
<body>
    <form action="01_pra2_ans.py" method='post'>
    <p>ID(4~12字以内、必須項目):<br><input type="text" name="inid" minlength="4" maxlength="12" required></p>
    <p>パスワード(8桁以上、必須項目):<br><input type="password" name="inpassword" minlength="8" required></p>
    <p>血液型（任意）:<br>
    <select name = 'blood'>
        <option value ="A">A型</option>
        <option value ="B">B型</option>
        <option value ="O">O型</option>
        <option value ="AB">AB型</option>
    </select></p>
    <p><input type="submit" value="確定"></p>
    </form>
</body>
</html>
"""
)
    
