<html>
	<head>
		<meta charset="utf-8">
		<style>
			table{border: 1px solid gray;}
			td,th{border:1px solid gray; padding: 4px;}
			h2{margin-left: 230px;}
		</style>
	</head>
	<body>
		<h2>회원정보</h2>
		<?php
			
			include("dbcon.php");			

			$result = mysqli_query($mysqli, "SELECT * FROM user");

			echo "<table><tr><th>이름</th><th>아이디</th><th>비밀번호</th><th>이메일</th><th>전화번호</th>";
			while($rows = mysqli_fetch_array($result)){
				echo "<tr>";
				echo "<td>".iconv('EUCKR', 'UTF8', $rows['name'])."</td>";
				echo "<td>".iconv('EUCKR', 'UTF8', $rows['id'])."</td>";
				echo "<td>".iconv('EUCKR', 'UTF8', $rows['pw'])."</td>";
				echo "<td>".iconv('EUCKR', 'UTF8', $rows['email'])."</td>";
				echo "<td>".iconv('EUCKR', 'UTF8', $rows['phoneNumber'])."</td>";
				echo "</tr>";
			}
			echo "</table>";
			mysqli_close($mysqli);
			?>
	</body>
