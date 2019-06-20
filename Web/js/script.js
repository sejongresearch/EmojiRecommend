function password_same(){ //비밀번호가 일치하지 않을때 .innerHTML처리
	if(document.getElementById("pw_input").value != document.getElementById("pwcheck_input").value){
		document.getElementById("pw_same").innerHTML="비밀번호 불일치";
		document.getElementById("pw_same").style.color="red";
		}
	else if(document.getElementById("pw_input").value == ""){
		document.getElementById("pw_same").innerHTML="비밀번호를 입력해주세요";
		document.getElementById("pw_same").style.color="red";
	}
	else
			document.getElementById("pw_same").innerHTML="";
}
function input_check(){	//if value == "" alert;
	var all_input = ["name_input", "id_input", "pw_input", "pwcheck_input", "email_input1", "email_input2", "phone_input1", "phone_input2", "phone_input3", "person_number1", "person_number2"];
	var input_name = ["이름을", "아이디를", "비밀번호를" , "비밀번호 확인을", "이메일을", "이메일을", "휴대폰 앞 세자리를", "휴대폰 중간 네자리를", "휴대폰 마지막 네자리를", "주민등록번호 앞자리를", "주민등록번호 뒤자리를"];
	var count = 0;
	for(var i=0; i < all_input.length; i++){
		if(document.getElementById(all_input[i]).value==""){
			alert(input_name[i]+"입력해 주세요.");
			document.getElementById(all_input[i]).focus();
			break;
		}
		else if(!(document.getElementById(all_input[i]).value=="")){
				count++;
				if(count == 11)
					document.getElementById("register_clear_form").submit();
		}
	}
}
//if 비밀번호가 일치하지 않을시 alert;