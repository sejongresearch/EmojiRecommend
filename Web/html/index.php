<html>
	<head>
		<meta charset="utf-8">
	</head>
	<body>
		<?php
			session_start();
			include("php/dbcon.php");
			
			if(!isset($_SESSION['user_name'])){
				echo("<script>location.href='login.html';</script>");
				exit;
			}
			echo("<script>location.href='mypage.php';</script>");				
		?>		
	</body>