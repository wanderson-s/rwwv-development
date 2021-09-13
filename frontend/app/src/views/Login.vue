<template>
  <div id="div-login" class="container border rounded" style="text-align: center;">
    <div id="div-image-login">
      <b-img src="https://www.taimin.com.br/images/brand.png?2" v-bind="mainProps" rounded alt="Login"></b-img>
    </div>
    <b-form class="form-login" @submit="onSubmit" @reset="onReset">
      <b-form-group
        class="label-login"
        id="label-email"
        label="Email"
        label-for="input-email"
        description="Digite seu email Taimin."
      >
        <b-form-input
          id="input-email"
          v-model="form.email"
          type="email"
          placeholder="seuemail@taimin.com.br"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group 
      class="label-login"
        id="password" 
        label="Senha" 
        label-for="input-password"
      >
        <b-form-input
          id="input-password"
          v-model="form.password"
          :type="type_password"
          placeholder="Digite sua senha."
          required
        ></b-form-input>
      </b-form-group>
      <b-button type="submit" pill variant="info"> Acessar </b-button>
    </b-form>
  </div>
</template>

<script>
export default {
  name: "ViewLogin",
  data() {
    return {
      form: {
        email: "",
        password: "",
      },
      type_password: "password",
    };
  },
  methods: {
    onSubmit(event) {
      event.preventDefault();
      axios.post('https://localhost:8000/v1/login', {
                username: this.username,
                password: this.pwd1
            }).then(response => {
                localStorage.setItem('token', response.data.token)
            }).catch(error => {
                console.log("Error login")
                console.log(error)
            })
            this.dialog = false
        }
    },
    onReset(event) {
      event.preventDefault();
      // Reset our form values
      this.form.email = "";
      this.form.password = "";
    },
    showPassword() {
      if(this.type_password === 'password') {
          this.type_password = 'text'
       } else {
          this.type_password = 'password'
       }

    }
  }
};
</script>

<style scoped>
  .label-login {
    text-align: left;
  }
  .form-login {
    align-items: center;
    padding: 5%;
  }
  #div-login {
    max-width: 500px;
    min-width: 400px;
    margin-top: 10%;
  }
  #div-image-login {
    margin-top: 5%;
  }
</style>