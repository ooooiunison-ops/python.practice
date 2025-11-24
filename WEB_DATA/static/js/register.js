$(function () {

    let error_name = false;
    let error_password = false;
    let error_check_password = false;
    let error_first_name = false;
    let error_email = false;
    let error_send_code = false;
    let error_check = false;


    $('#user_name').blur(function () {
        check_user_name();
    });

    $('#pwd').blur(function () {
        check_pwd();
    });

    $('#cpwd').blur(function () {
        check_cpwd();
    });

    $('#first_name').blur(function () {
        check_first_name();
    });
    $('#email').blur(function () {
        check_email();
    });

    $('#allow').click(function () {
        if ($(this).is(':checked')) {
            error_check = false;
            $(this).siblings('span').hide();
        } else {
            error_check = false;
            $(this).siblings('span').html('会員規約・個人情報保護方針に同意してください。');
            $(this).siblings('span').show();
        }
    });

    function check_user_name() {
        const len = $('#user_name').val().length;
        if (len < 2 || len > 20) {
            $('#user_name').next().html('名前を入力してください')
            $('#user_name').next().show();
            error_name = true;
        } else {
            $('#user_name').next().hide();
            error_name = false;
        }
    }

    function check_pwd() {
        const len = $('#pwd').val().length;
        if (len < 8 || len > 20) {
            $('#pwd').next().html('最低8文字、最長20文字が必要です')
            $('#pwd').next().show();
            error_password = true;
        } else {
            $('#pwd').next().hide();
            error_password = false;
        }
    }


    function check_cpwd() {
        const pass = $('#pwd').val();
        const cpass = $('#cpwd').val();

        if (pass !== cpass) {
            $('#cpwd').next().html('パスワードが一致しません')
            $('#cpwd').next().show();
            error_check_password = true;
        } else {
            $('#cpwd').next().hide();
            error_check_password = false;
        }

    }
    function check_first_name() {
        $('#check_first_name').next().hide();
        error_first_name = false;
    }
    function check_email() {
        $('#email').next().hide();
        error_email = false;
    }
    $("#send_code").click(function(){
            const email = $("#email").val();
            if(email===""){
                $("#tip").text('* メールアドレスを入力してください！');
                return false;
            }

            // 发送验证码
            $.ajax({
                url: '/send_verification_code',
                type: "GET",
                data: {
                    'user_email': email,
                    'send_for': 'register_code'
                },
                cache: false,
                success: function(data){
                    if(data['status']==='ERROR1'){
                        alert(data['status']);
                    }
                }
            });
            console.log(email)
            console.log($("#email"))

            // 把按钮变灰
            $(this).addClass('disabled');
            $(this).attr('disabled', true);
        let time = 0;
        $(this).text(time + 's');
        const interval = setInterval(() => {
            if (time <= 0) {
                clearInterval(interval);
                $(this).removeClass('disabled');
                $(this).attr('disabled', false);
                $(this).text('検証コードを発送！');
                $(this).display = 'block'
                return false;
            }

            time--;
            $(this).text(time + 's');
        }, 1000);
    });

    $('#reg_form').submit(function () {
        check_user_name();
        check_pwd();
        check_cpwd();
        check_email();
        check_first_name();
        console.log(error_check_password)
        console.log(error_email )
        console.log(error_name )
        console.log(error_password)
        console.log(error_first_name)
        console.log(error_check)



        if (error_name === false && error_password === false && error_check_password === false && error_email === false && error_first_name === false && error_check === false) {
            console.log($('#reg_form').serialize())
            console.log('test')
            $.ajax(
                {
                    url: '/register',
                    type: 'POST',
                    data: $('#reg_form').serialize(),
                    dataType: 'JSON',
                    success: function (data) {
                        console.log(data)
                        if (data.status) {
                            window.location = '/login'
                        } else {
                            $('.error_tip2').html(data.error_tips).show()
                        }
                    }
                }
            );
            return false;
        } else {
            return false;
        }

    });


})