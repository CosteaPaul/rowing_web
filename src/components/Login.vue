<template>
    <Form ref="formInline" :model="formInline" :rules="ruleInline" inline>
        <FormItem prop="user">
            <Input type="text" v-model="formInline.user" placeholder="Username">
                <Icon type="ios-person-outline" slot="prepend"></Icon>
            </Input>
        </FormItem>
        <FormItem prop="password">
            <Input type="password" v-model="formInline.password" placeholder="Password">
                <Icon type="ios-lock-outline" slot="prepend"></Icon>
            </Input>
        </FormItem>
        <br>
        <FormItem>
            <Button type="primary" @click="handleSubmit('formInline')">Signin</Button>
        </FormItem>
    </Form>
</template>
<script>
    import axios from 'axios';
    import md5 from 'md5';
    export default {
        data () {
            return {
                formInline: {
                    user: '',
                    password: ''
                },
                ruleInline: {
                    user: [
                        { required: true, message: 'Please fill in the user name', trigger: 'blur' }
                    ],
                    password: [
                        { required: true, message: 'Please fill in the password.', trigger: 'blur' },
                        { type: 'string', min: 4, message: 'The password length cannot be less than 4 bits', trigger: 'blur' }
                    ]
                }
            }
        },
        methods: {
            handleSubmit(name) {
                this.$refs[name].validate((valid) => {
                    if (valid) {
                        this.$Message.success('Success!');
                    } else {
                        this.$Message.error('Fail!');
                    }
                });

                var pass = md5(this.formInline.password);
                axios.get(BACKEND_URL+'/token_generation',{
                  params: {
                    'username': this.formInline.user,
                    'password': pass
                  }
                }).then(
                    function(response) {
                      if (response.data.authorized == "True") {
                        window.localStorage.setItem('row_token', response.data.token);
                        axios.get(BACKEND_URL+'/listTables', {
                          headers: {
                            'Authorization' : response.data.token
                          }
                        }).then(
                          function(response) {
                              console.log(response);
                          }
                        );
                      } else {
                        alert('Incorred Username or Password');
                      }
                    }
                 );
            }
        }
    }
</script>
