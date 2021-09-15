<template>
  <div id="div-login" class="container border rounded" style="text-align: center;">
    <div>
        <b-alert
          id="alert-login"
          variant="danger"
          dismissible
          fade
          :show="showDismissibleAlert"
          @dismissed="showDismissibleAlert=false"
        >
          E-mail ou senha invalida.
        </b-alert>
    </div>
    <div id="div-image-login">
      <b-img src="https://www.taimin.com.br/images/brand.png?2" v-bind="mainProps" rounded alt="Login"></b-img>
    </div>
      <b-form class="form-login" @submit="onSubmit" @reset="onReset">
        <b-form-group
          class="label-login"
          id="label-email"
          label="E-mail"
          label-for="input-email"
          description="Digite seu email Taimin."
        >
          <b-form-input
            id="input-email"
            v-model="form.email"
            type="email"
            :state="can_access"
            aria-describedby="input-login-feedback"
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
          :state="can_access"
          placeholder="Digite sua senha."
          required
        ></b-form-input>
          <b-form-checkbox
            switch
            v-model="type_password"
            name="checkbox-login"
            unchecked-value="password"
          >
            Mostrar Senha
          </b-form-checkbox>
        </b-form-group>
      <b-button type="submit" pill variant="info"> Acessar </b-button>
    </b-form>
  </div>
</template>

<script>
import axios from "axios"

export default {
  name: "ViewLogin",
  data() {
    return {
      form: {
        email: "",
        password: "",
      },
      showDismissibleAlert: false,
      can_access: true,
      type_password: "password"
    };
  },
  methods: {
    onSubmit:  async function (event) {
      event.preventDefault();
      try {
        const response = await axios.post("http://localhost:8001/v1/auth/login", this.form);
        this.saveTokens(response);
        this.showDismissibleAlert = false
        this.redirectToHome()
      } catch(error){
        this.can_access = false
        this.showDismissibleAlert = true
      }
    },
    onReset: async function (event) {
      event.preventDefault();
      // Reset our form values
      this.form.email = "";
      this.form.password = "";
    },
    saveTokens (response){
      localStorage.setItem("access_token", response.data.access_token);
      localStorage.setItem("refresh_token", response.data.refresh_token);
    },
    getMe: async function () {
      try {
        const url = "http://localhost:8001/v1/auth/get-me?access_token=" +localStorage.getItem("access_token")
        const response = await axios.get(url);
        return response.data
      } catch(error){
        console.error(error)
      }
    },
    redirectToHome: async function () {
      const user = await this.getMe()
      console.log(user)
      this.$router.push({ name: 'Home', path: '/'})
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
  #alert-login {
    margin-top: 3%;
  }
</style>