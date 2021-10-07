<template>
  <div class="container-fluid p-1 pe-2">
    <div  id="form" class="container d-flex justify-content-center">
      <h3 class="card-title pb-0 pt-0">Funcionários</h3>
    </div>
    <form class="row g-0 border border-danger rounded p-3" @submit="onSubmit">
      <div v-show="disableAlert" v-for="al in alertList" :key="al" class="alert alert-danger" role="alert">
        {{ al }}
      </div>
      <h5 class="card-title pb-0 pt-0">Dados</h5>
      <div class="fields shadow border border-1 rounded p-4">
        <div class="col-12 required">
          <label for="email" class="form-label">E-mail</label>
          <input
            :disabled="disableForm"
            id="email"
            v-model="employee.email"
            type="email"
            class="form-control"
            placeholder="seuemail@taimin.com.br"
          />
        </div>

        <div class="col-12" :class="buttonUpdateDisable ? 'required' : ''">
          <label for="password" class="form-label">Senha</label>
          <input
            :disabled="disableForm"
            id="password"
            v-model="employee.password"
            type="password"
            class="form-control"
            placeholder="Senha"
          />
        </div>

        <div class="col-12">
          <label for="first_name" class="form-label">Nome</label>
          <input
            :disabled="disableForm"
            id="first_name"
            v-model="employee.first_name"
            type="text"
            class="form-control"
            placeholder="Ex: Pedro"
          />
        </div>

        <div class="col-12">
          <label for="last_name" class="form-label">Sobrenome</label>
          <input
            :disabled="disableForm"
            id="last_name"
            v-model="employee.last_name"
            type="text"
            class="form-control"
            placeholder="Ex: Silva"
          />
        </div>

        <div id="div-min-len" class="col-12 required">
          <label for="position" class="form-label">Cargo</label>
          <select
            :disabled="disableForm"
            v-model="employee.position"
            class="form-select"
            aria-label="Selecione o cargo."
            required
          >
            <option :selected="position[0].value"> {{ position[0].value }} </option>
            <option v-for="pos in position.filter((posi) => posi.key !== 'analyst')" :key="pos.key" :value="pos.key">{{ pos.value}}</option>
          </select>
        </div>

        <div id="div-min-len" class="col-12">
          <label for="birth_date" class="form-label">Data de nascimento</label>
          <v-date-picker v-model="employee.birth_date" locale="pt-BR">
            <template v-slot="{ inputValue, inputEvents }">
              <input
                class="form-control"
                :disabled="disableForm"
                :value="inputValue"
                v-on="inputEvents"
              />
            </template>
          </v-date-picker>
        </div>
      </div>
      <h5 class="card-title pb-0 pt-4">Permissões</h5>
      <div class="checks d-flex flex-row shadow border border-1 rounded p-2">
        <div class="form-check form-switch">
          <label for="active" class="form-label">Ativo</label>
          <input
            :disabled="disableForm"
            v-model="employee.active"
            type="checkbox"
            class="form-check-input"
          />
        </div>
        <div class="form-check form-switch">
          <label for="is_admin" class="form-label">Administrador</label>
          <input
            :disabled="disableForm"
            v-model="employee.is_admin"
            type="checkbox"
            class="form-check-input"
          />
        </div>
        <div class="form-check form-switch">
          <label for="can_simulate_budget" class="form-label"
            >Simular Orçamento</label
          >
          <input
            :disabled="disableForm"
            v-model="employee.can_simulate_budget"
            type="checkbox"
            class="form-check-input"
          />
        </div>
        <div class="form-check form-switch">
          <label for="can_submit_budget" class="form-label"
            >Criar Orçamento</label
          >
          <input
            :disabled="disableForm"
            v-model="employee.can_submit_budget"
            type="checkbox"
            class="form-check-input"
          />
        </div>
        <div class="form-check form-switch">
          <label for="can_approve_budget" class="form-label"
            >Aprovar Orçamento</label
          >
          <input
            :disabled="disableForm"
            v-model="employee.can_approve_budget"
            type="checkbox"
            class="form-check-input"
          />
        </div>
        <div class="form-check form-switch">
          <label for="can_read_budget" class="form-label">Ver Orçamento</label>
          <input
            :disabled="disableForm"
            v-model="employee.can_read_budget"
            type="checkbox"
            class="form-check-input"
          />
        </div>
      </div>

      <div class="buttons mt-4 d-flex flex-row p-0">
        <DefaultButton class="action-button" buttonText="Novo" @click="enableForm" :buttonActive="buttonNewDisable" buttonColor="btn btn-primary" buttonIcon="bi bi-plus-circle-fill" buttonType="button"/>
        <DefaultButton class="action-button" buttonText="Salvar" :buttonActive="buttonCreateDisable" buttonColor="btn btn-success" buttonIcon="bi bi-check-circle-fill"/>
        <DefaultButton class="action-button" buttonText="Alterar" :buttonActive="buttonUpdateDisable" buttonColor="btn btn-dark" buttonIcon="bi-arrow-up-circle-fill" buttonType="button" />
        <DefaultButton class="action-button" buttonText="Cancelar" @click="onReset" buttonColor="btn btn-danger" buttonIcon="bi-x-circle-fill" buttonType="reset"/>
      </div>
    </form>

    <div class="table-func d-flex row g-0 border border-danger rounded p-3 mt-2">
      <h5 class="card-title">Listagem de Funcionários</h5>
      <table  class="table table-bordered">
        <thead class="table table-dark border border-white">
          <tr class="border border-secondary">
            <th scope="col">E-mail</th>
            <th scope="col">Cargo</th>
            <th scope="col">Nome</th>
            <th scope="col">Ativo</th>
            <th scope="col">Administrador</th>
            <th scope="col">Simular</th>
            <th scope="col">Criar</th>
            <th scope="col">Aprovar</th>
            <th scope="col">Ver</th>
            <th scope="col" style="width: 100px;">Ação</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="empl in employees" :key="empl.id">
            <td>{{ empl.email }}</td>
            <td>{{ position_pt[empl.position] }}</td>
            <td>{{ empl.first_name }} {{ empl.last_name }}</td>
            <td class="active"><i :class="isActive(empl.active)" style="font-size: 1.2rem; color: cornflowerblue;" ></i> </td>
            <td class="active"><i :class="isActive(empl.can_simulate_budget)" style="font-size: 1.2rem; color: cornflowerblue;" ></i> </td>
            <td class="active"><i :class="isActive(empl.can_submit_budget)" style="font-size: 1.2rem; color: cornflowerblue;" ></i> </td>
            <td class="active"><i :class="isActive(empl.can_approve_budget)" style="font-size: 1.2rem; color: cornflowerblue;" ></i> </td>
            <td class="active"><i :class="isActive(empl.can_read_budget)" style="font-size: 1.2rem; color: cornflowerblue;" ></i> </td>
            <td class="active"><i :class="isActive(empl.is_admin)" style="font-size: 1.2rem; color: cornflowerblue;" ></i> </td>
            <td class="d-flex flex-row justify-content-around" style="max-width: 100px;">
              <button @click="loadEmployee(empl.id)" type="button" class="btn btn-primary btn-sm m-0"><i class="bi bi-eye-fill"></i></button>
              <button @click="removeEmployee(empl.id)" type="button" class="btn btn-danger btn-sm m-0" ><i class="far fa-trash-alt"></i></button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

  </div>
</template>

<script>
import checkLogin from "../js/checkLogin.js";
import redirectToLogin from "../js/redirectLogin";
import DefaultButton from "../components/DefaultButton.vue";
import Employee from '../services/employee.js'

const position = {
  list: [
    {key: "analyst", value: "Analista"},
    {key: "manager", value: "Gerente"},
    {key: "director", value: "Diretor"},
  ],
  pt: {
    Analista: "analyst",
    Gerente: "manager",
    Diretor: "director",
  },
  en: {
    analyst: "Analista",
    manager: "Gerente",
    director: "Diretor",
  }
}
const alertMsg = {
  email: 'Email invalido, o e-mail precisa ter @taimin.com.br!',
  password: 'A senha precisa ter mais de 8 caracteres com no minimo 1 letra maiúscula, 1 número e 1 caracter especial.',
  first_name: 'Nome invalido.',
  last_name: 'Sobrenome invalido.',
  birth_date: 'Data de nascimento invalida.',
  position: 'Somente os cargos de Analista, Gerente e Diretor são aceitos.'
}

export default {
  name: "Employee",
  components: {
    DefaultButton,
  },
  methods: {
    isActive: function (value) {
      return value ? 'bi bi-check-circle-fill':'bi bi-check-circle'
    },
    loadEmployee: function (id) {
      this.buttonUpdateDisable = false
      this.employees.forEach(element => {
        if (element.id == id) {
          this.employee = element
          this.disableForm = false
          this.buttonNewDisable = true
          return
        }
      });
    },
    listEmployee: function () {
      Employee.listEmployee().then((resp) => {
          this.employees = resp.data
        }).catch((err) => {
          console.log("ERROR LIST EMPLOYEES")
        })
    },
    createEmployee: function () {
      const data = this.employee
      data.position = position.pt[data.position]
      data.birth_date = data.birth_date.toISOString().split('T')[0]
      
      Employee.createEmployee(data)
        .then((resp) => {
          console.log(resp)
          this.listEmployee()
        }).catch((err) => {
          console.log(err.request)
          console.log(err.response.data)
          if (err.response.status == 422) {
            this.alertList = err.response.data.detail.map((d) => {
              const key = d.loc.slice(-1)[0]
              return alertMsg[key]
            })
          }else if (err.response.status == 400) {
            this.alertList = ['O e-mail informado já existe.']
          }
          this.disableAlert = true
          setTimeout(() => {
            this.alertList = []
            this.disableAlert = false
          }, 10000)
        })
    },
    removeEmployee: function (id) {
      if (confirm("Você tem certeza?")){
        Employee.removeEmployee(id)
          .then(() => {
            console.log("REMOVE EMPLOYEE.")
            this.listEmployee()
          }).catch((err) => {
            console.log("DON'T REMOVE EMPLOYEE.")
          });
      }
      
    },
    onReset: function (event) {
      event.preventDefault();
      this.employee.email = ""
      this.employee.password = ""
      this.employee.first_name = ""
      this.employee.last_name = ""
      this.employee.birth_date = new Date(2000, 1, 1)
      this.employee.position = position.list[0].value
      this.employee.active = false
      this.employee.can_simulate_budget = false
      this.employee.can_submit_budget = false
      this.employee.can_approve_budget = false
      this.employee.can_read_budget = false
      this.employee.is_admin = false
      this.buttonUpdateDisable = true
      this.disableForm = true
      this.buttonNewDisable = false
      this.buttonCreateDisable = true
    },
    onSubmit: function (event) {
      event.preventDefault();
      console.log(this.employee)
      this.createEmployee()
    },
    enableButton: function () {
      if (this.employee.email != '' && this.employee.password != '' && this.employee.position != '' && this.buttonUpdateDisable) {
        this.buttonCreateDisable = true
      }else {
        this.buttonCreateDisable = false
      }
    },
    enableForm: function () {
      this.disableForm = false
      this.buttonCreateDisable = false
      this.buttonNewDisable = true
      this.employees.position = position.list[0].value
    }
  },
  data () {
    return {
      employee: {
        email: "",
        password: "",
        first_name: "",
        last_name: "",
        birth_date: new Date(2000, 1, 1),
        position: position.en.analyst,
        active: false,
        can_simulate_budget: false,
        can_submit_budget: false,
        can_approve_budget: false,
        can_read_budget: false,
        is_admin: false,
      },
      employees: [],
      position: position.list,
      position_pt: position.pt,
      buttonCreateDisable: true,
      buttonUpdateDisable: true,
      buttonNewDisable: false,
      disableForm: true,
      disableAlert: false,
      alertList: []
    };
  },
  async mounted() {
    try {
      const data = await checkLogin();
      if (!data) {
        console.log("USER DOES NOT EXISTS.");
        redirectToLogin(this);
      }
      else {
        this.listEmployee()
      }
    } catch (error) {
      console.log("REQUEST ERROR");
      redirectToLogin(this);
    }
  },
};
</script>

<style scoped>  
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.3.0/font/bootstrap-icons.css");

/* NEW */

/* fields */
.fields {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: flex-start;
  align-items: baseline;
  align-content: space-around;
}
.col-12 {
  max-width: 50%;
  min-width: 30%;
  padding: 5px 3px 5px 3px;
}
.col-12.required .form-label:after {
  content:"*";color:red;
}
#div-min-len {
  max-width: 15% !important;
  min-width: 5%;
}
.action-button{
  margin-right: 20px;
}
.form-check {
  margin: 10px;
  margin-left: 20px;
}

/* tables */
.table-func {
  min-width: 100%;
}

.active {
  text-align: center;
  width: 100px;
}
th {
  text-align: center;
}
</style>