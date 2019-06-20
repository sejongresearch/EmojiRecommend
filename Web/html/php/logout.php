<html>
	<head>
		<meta charset="utf-8">
	</head>
	<body>
		<?php
			session_start();
			session_destroy();
			echo("<script>alert('사용자의 요청으로 인해 로그아웃 됩니다.');</script>");
			echo("<script>location.href='../login.html';</script>");
		?>
	</body>