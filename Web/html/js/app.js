var express= require('express')
var session = require('express-session');
// mysql 세션스토어 설정
var MySQLStore = require('express-mysql-session')(session);
var mysql = require('mysql');
var conn = mysql.createConnection({
    host : 'localhost',
    user : 'root',
    password : 'root',
    database : 'o2'
})
var md5 = require('md5')

const bodyParser = require('body-parser');
var app = express();
//세션 스토어를 사용하기위한 디비 셋팅
app.use(session({
    secret: '1$!%!%13513',
    resave: false,
    saveUninitialized: true,
    store:new MySQLStore({
        host:'localhost',
        port:3306,
        user:'root',
        password:'root',
        database:'o2'
    })
}))  
app.use(bodyParser.urlencoded({extended: false}))
app.use(express.static('publi'));
app.locals.pretty = true;

app.set('view engine','jade');
app.set('views','./views_my');

app.get('/', function (req, res) {
  //res.send('Hello World!');
  //res.sendFile(__dirname +'/html/index.html');
  res.send('hello')

});
app.get('/jade_test', function (req, res) {
    //res.send('Hello World!');
    //res.sendFile(__dirname +'/html/index.html');
    res.render('main')
  
  });

app.get('/admin',function(req,res) {
    var sql = `SELECT * FROM manargetic`
    conn.query(sql,function(err,rows,fields) {
        var su = rows.length;
        res.render('admin',{members:rows,su:su})
        // var msg_members = `매너제틱 의 회원수는[${members}]명 입니다.
        
        // `
        // for(var i =0; i<members ; i++)
        //     {
        //         var output = `
        //         ${i}번째 회원의 정보입니다.
        //         이름 : ${rows[i].name}
        //         아이디 : ${rows[i].id}
        //         비밀번호 : ${rows[i].password}
        //         <br>
        //         `
        //     }

    })
})

app.get('/welcome', function (req, res) {
    //res.send('Hello World!');
    //res.sendFile(__dirname +'/html/index.html');
    res.send('welcome 로그인이 성공됬을시 접근되는 페이지입니다.')
  
  });


app.post('/login',function(req,res) {
    var input_id = req.body.id
    var input_pw = req.body.pw
    var sql = `SELECT * FROM manargetic`
    conn.query(sql,function(err,rows,fields) {
        if(err){
            console.log(err);
            res.status(500).send('서버 내부 오류가 있습니다.');
        }
        else
        {
            var max = rows.length      
            for(i=0; i<max ; i++)
                {
                    if(rows[i].id == input_id && rows[i].password == input_pw)
                        {           // 로그인성공
                          //res.redirect('/welcome')d                         
                          req.session.name = rows[i].name
                          return req.session.save(function() {
                              res.redirect('/welcome')
                          })
                        }
                }
                res.send('오류입니다.')
    }
    })
    
})

app.post('/register',function(req,res) {
    var input_id = req.body.id
    var input_pw = req.body.pw
    var input_name = req.body.name
    //회원가입시 id 중복검사
    var sql = `SELECT id FROM manargetic`
    conn.query(sql,function(err,rows,fields) {
        if(err){ƒ
            res.status(500).send('서버 내부 오류가 있습니다.');
        }
        else{
            var max = rows.length
            for(var i = 0; i<max ; i++)
                {
                    if(rows[i].id == input_id ) // 중복일때
                        {
                            return res.send('이미 존재하는 ID 입니다.')
                        }                           
                }
            var sql = `INSERT INTO manargetic (name,id,password) VALUES(?,?,?)`
            var p = [input_name,input_id,input_pw];
            conn.query(sql,p,function(err,rows,fields) {
                if(err){
                    console.log(err);
                    res.status(500).send('서버 내부 오류가 있습니다.');
                }
                else{
                    res.redirect('/');
                }
            })
        }
    })

})

app.listen(3000,function(req,res) {
    console.log("3000번 포트에서 서버가 작동합니다.");
})