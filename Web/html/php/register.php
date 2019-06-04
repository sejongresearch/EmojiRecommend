<html>
  <head>
    <meta charset="UTF-8">
  </head>

  <body>
    <?php

	include("dbcon.php");

    //login parameter
    $name = $_POST['name'];
    $id = $_POST['id'];
    $pw = $_POST['password'];
    $email_1 = $_POST['email_1'];
    $email_2 = $_POST['email_2'];
    $phone_1 = $_POST['phone_number_1'];
    $phone_2 = $_POST['phone_number_2'];
    $phone_3 = $_POST['phone_number_3'];
    $person_1 = $_POST['person_number1'];
    $person_2 = $_POST['person_number2'];

    //table row
    mysqli_query($mysqli, "set session character_set_connection=utf8;");
    mysqli_query($mysqli, "set session character_set_results=utf8;");
    mysqli_query($mysqli, "set session character_set_client=utf8;");

		$sql = "insert into `user` (`name`, `id`, `pw`, `email`, `phoneNumber`, `personNumber`)";
		$sql = $sql."values ('$name', '$id', '$pw', '$email_1@$email_2', '$phone_1-$phone_2-$phone_3', '$person_1-$person_2');";
    if($mysqli->query($sql)){
    	echo("<script language = javascript>alert('".$name."님 회원가입이 완료되었습니다.');</script>");
    	echo("<script language = javascript>location.href='../login.html';</script>");
    }else{
    	echo "회원가입 실패";
    }
    mysqli_close($mysqli);
    ?>
  </body>
</html>
