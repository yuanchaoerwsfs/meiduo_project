// 我们采用的时ES6的语法
// 创建Vue对象 vm
let vm = new Vue({
    el: '#app', // 通过ID选择器找到绑定的HTML内容
    // 修改Vue读取变量的语法
    delimiters: ['[[', ']]'],
    data: { // 数据对象
        // v-model
        username: '',
        password: '',
        password2: '',
        mobile: '',
        allow: '',
        image_code_url: '',
        uuid: '',
        image_code:'',
        sending_flag:'',
        sms_code_tip: '获取短信验证码',

        // v-show
        error_name: false,
        error_password: false,
        error_password2: false,
        error_mobile: false,
        error_allow: false,
        error_image_code:false,
        error_sms_code:false,

        // error_message
        error_name_message: '',
        error_mobile_message: '',
        error_image_code_message:'',
    },
    mounted() { // 页面加载完会被调用的
        // 生成图形验证码
        this.generate_image_code();
    },
    methods: { // 定义和实现事件方法
        //获取短信验证码
        check_sms_code(){
            if (this.sms_code.length!=6){
                this.error_sms_code_message='请输入正确的验证码';
                this.error_sms_code = true;}
            else{
                this.error_sms_code=false;
                }
        },
        send_sms_code(){
            url='/SMSCodeView/'+this.mobile+'/?image_code=' + this.image_code+'&uuid='+ this.uuid;
            axios.get(url,{
                responseType: 'json'
            })
                .then(response => {
                        if (response.data=='0') {
                            // 倒计时为0后，重新激活发送验证码按钮
                            let num = 60;
                            const t = setInterval(() => {
                                if (num == 1) {
                                    clearInterval(t);
                                    this.sms_code_tip = '获取短信验证码';
                                    this.generate_image_code();
                                    this.sending_flag = false;
                                } else {
                                    num -= 1;
                                    this.sms_code_tip = num + '秒';
                                }
                            }, 1000, 60);
                        } else {
                            // 返回4XXX错误码处理：图形验证码输入有误
                            if(response.data.code=='4001'){
                                this.error_image_code_message=response.data.errmsg;
                                this.error_image_code=true;
                            }else {//返回4XXX错误码处理：短信验证码输入有误
                                this.error_sms_code_message=response.data.errmsg;
                                this.error_sms_code=true;
                            this.generate_image_code();
                            this.sending_flag = false;
                            }
                        }
                    })
                .catch(error=>{
                    console.log(error.response);
                    this.sending_flag=false;
                })

        },



        // 生成图形验证码的方法：封装的思想，代码复用
        generate_image_code() {
            this.uuid = generateUUID();
            this.image_code_url = '/image_codes/' + this.uuid + '/';
        },

        // 校验用户名
        check_username() {
            // 用户名是5-20个字符，[a-zA-Z0-9_-]
            // 定义正则
            let re = /^[a-zA-Z0-9_-]{5,20}$/;
            // 使用正则匹配用户名数据
            if (re.test(this.username)) {
                // 匹配成功，不展示错误提示信息
                this.error_name = false;
            } else {
                // 匹配失败，展示错误提示信息
                this.error_name_message = '请输入5-20个字符的用户名';
                this.error_name = true;
            }

            // 判断用户名是否重复注册
            if (this.error_name == false) { // 只有当用户输入的用户名满足条件时才回去判断
                let url = '/usernames/' + this.username + '/count/';
                axios.get(url, {
                    responseType: 'json'
                })
                    .then(response => {
                        if (response.data.count == 1) {
                            // 用户名已存在
                            this.error_name_message = '用户名已存在';
                            this.error_name = true;
                        } else {
                            // 用户名不存在
                            this.error_name = false;
                        }
                    })
                    .catch(error => {
                        console.log(error.response);
                    })
            }

        },


        // 校验密码
        check_password() {
            let re = /^[0-9A-Za-z]{8,20}$/;
            if (re.test(this.password)) {
                this.error_password = false;
            } else {
                this.error_password = true;
            }
        },
        // 校验确认密码
        check_password2() {
            if (this.password != this.password2) {
                this.error_password2 = true;
            } else {
                this.error_password2 = false;
            }
        },
        // 校验手机号
        check_mobile() {
            let re = /^1[3-9]\d{9}$/;
            if (re.test(this.mobile)) {
                this.error_mobile = false;
            } else {
                this.error_mobile_message = '您输入的手机号格式不正确';
                this.error_mobile = true;
            }
                        //判断手机号码是否重复
            if (this.error_mobile == false) { // 只有当用户输入的用户名满足条件时才回去判断
                let url = '/mobiles/' + this.mobile + '/count/';
                axios.get(url, {
                    responseType: 'json'
                })
                    .then(response => {
                        if (response.data.count == 1) {
                            // 手机号码已存在
                            this.error_mobile_message = '手机号码已存在';
                            this.error_mobile = true;
                        } else {
                            // 手机号码不存在
                            this.error_mobile = false;
                        }
                    })
                    .catch(error => {
                        console.log(error.response);
                    })
            }
        },



        //验证码校验
        check_image_code(){
            if(this.image_code.length!=4) {
                this.error_image_code_message = '请填写图片验证码';
                this.error_image_code = true;
        } else {
                this.error_image_code = false;
                }
        },

        // 校验是否勾选协议
        check_allow() {
            if (!this.allow) {
                this.error_allow = true;
            } else {
                this.error_allow = false;
            }
        },
        // 监听表单提交事件
        on_submit() {
            this.check_username();
            this.check_password();
            this.check_password2();
            this.check_mobile();
            this.check_allow();
            this.check_sms_code()

            // 在校验之后，注册数据中，只要有错误，就禁用掉表单的提交事件
            if (this.error_name == true || this.error_password == true || this.error_password2 == true || this.error_mobile == true ||this.error_sms_code==true|| this.error_allow == true) {
                // 禁用掉表单的提交事件
                window.event.returnValue = false;
            }
        },
    }
});