<template>
	<div class="container-fluid p-1 pe-2">
    <DefaultTitle 
      titleText="Orçamentos" 
      titleIcon="bi-briefcase-fill"
    />
    <form class="row g-0 p-3 px-4" @submit="onSubmit">
     <div class="accordion shadow" id="accordionPanelsStayOpenExample">
        <!-- accordion 1 -->
        <div class="accordion-item shadow">
          <h2 class="accordion-header" id="panelsStayOpen-headingOne">
            <button 
              class="accordion-button" 
              type="button" 
              data-bs-toggle="collapse" 
              data-bs-target="#panelsStayOpen-collapseOne" 
              aria-expanded="true" 
              aria-controls="panelsStayOpen-collapseOne"
              :disabled="control.accordion.bu"
            >
              <i class="bi-briefcase-fill pe-2" style="font-size: 20px;" ></i>
              Selecione a BU, Familia de Produto e Aprovador.
            </button>
          </h2>
          <div id="panelsStayOpen-collapseOne" class="accordion-collapse collapse show" aria-labelledby="panelsStayOpen-headingOne">
            <div class="accor-01 accordion-body" style="width: 100%">
              <div class="selected col-12 required">
                <label for="bu" class="form-label">BU</label>
                <select
                  id="bu"
                  v-model="form.bu.name"
                  class="form-select"
                  aria-label="Selecione a BU"
                  @change="listProductFamily()"
                  :disabled="disableForm"
                  required
                >
                  <option :selected="form.bu.name"> {{ form.bu.name }} </option>
                  <option 
                    v-for="b in form.bus_name.filter((b) => b.name !== form.bu.name )" 
                    :key="b.id" 
                    :value="b.name">
                    {{ b.name }}
                  </option>
                </select>
              </div>

              <div class="selected col-12 required">
                <label for="product_family" class="form-label">Familia de Produto</label>
                <select
                  id="product_family"
                  v-model="form.bu.product_family"
                  class="form-select"
                  aria-label="Selecione a BU"
                  @change="accordionOne"
                  :disabled="disableForm"
                  required
                >
                  <option :selected="form.bu.product_family"> {{ form.bu.product_family }} </option>
                  <option 
                    v-for="b in form.product_family.filter((b) => b.product_family !== form.bu.product_family )" 
                    :key="b.id" 
                    :value="b.product_family">
                    {{ b.product_family}}
                  </option>
                </select>
              </div>

              <div class="selected col-12 required">
                <label for="approver" class="form-label">Aprovador</label>
                <select
                  id="approver"
                  v-model="form.bu.approver"
                  class="form-select"
                  aria-label="Selecione o Aprovador"
                  @change="accordionOne"
                  :disabled="disableForm"
                  required
                >
                  <option :selected="form.bu.approver"> {{ form.bu.approver }} </option>
                  <option 
                    v-for="b in form.approvers.filter((b) => b.email !== form.bu.approver )" 
                    :key="b.id" 
                    :value="b.email">
                    {{ b.email }}
                  </option>
                </select>
              </div>

              <div class="btn-next col-12">
                <DefaultButton
                  :disabled="disableForm"
                  @click="collapseAccordion('panelsStayOpen-collapseTwo', 'name')"
                  class="me-0 rounded-3 btn-sm" 
                  buttonText="Próximo"  
                  buttonColor="btn btn-outline-primary" 
                  buttonIcon="bi-arrow-right-circle-fill" 
                  buttonType="button"/>
              </div>
            </div>
          </div>
        </div>
        <!-- accordion 2 -->
        <div class="accordion-item shadow">
          <h2 class="accordion-header" id="panelsStayOpen-headingTwo">
            <button 
              class="accordion-button collapsed" 
              type="button" 
              data-bs-toggle="collapse" 
              data-bs-target="#panelsStayOpen-collapseTwo" 
              aria-expanded="true" 
              aria-controls="panelsStayOpen-collapseTwo"
              :disabled="control.accordion.bu"
            >
              <i class="bi-plus-square-fill pe-2" style="font-size: 20px;"></i>
              Informe o nome e status do seu orçamento.
            </button>
          </h2>
          <div id="panelsStayOpen-collapseTwo" class="accordion-collapse collapse" aria-labelledby="panelsStayOpen-headingTwo">
            <div class="accor-01 accordion-body">
              <div class="name status col-12" :class="field_required ? 'required' : ''">
                <label for="name" class="form-label">Nome</label>
                <input
                  :disabled="disableForm"
                  id="name"
                  v-model="form.status.name"
                  type="text"
                  class="form-control"
                  placeholder="Orçamento referente ao ano de 2022"
                />
              </div>
              <div class="selected col-12 required" :class="field_required ? 'required' : ''">
                <label for="bu" class="form-label">Status</label>
                <!-- <select
                  id="bu"
                  v-model="form.status.status"
                  class="form-select"
                  aria-label="Selecione o status"
                  :disabled="disableForm"
                  required
                >
                  <option :selected="form.status.status"> {{ form.status.status }} </option>
                  <option 
                    v-for="b in status.filter((b) => b.value !== form.status.status )" 
                    :key="b.name" 
                    :value="b.value">
                    {{ b.value }}
                  </option>
                </select> -->

                <select
                  id="bu"
                  v-model="form.status.status"
                  class="form-select"
                  aria-label="Selecione o status"
                  :disabled="disableForm"
                  required
                >
                  <option> {{ form.status.status }} </option>
                </select>
              </div>
              <div class="btn-next col-12">
                <DefaultButton 
                  @click="collapseAccordion('panelsStayOpen-collapseThree', 'year')"
                  :disabled="disableForm"
                  class="me-0 rounded-3 btn-sm" 
                  buttonText="Próximo"  
                  buttonColor="btn btn-outline-primary" 
                  buttonIcon="bi-arrow-right-circle-fill" 
                  buttonType="button"/>
              </div>
            </div>
          </div>
        </div>
        <!-- accordion 3 -->
        <div class="accordion-item">
          <h2 class="accordion-header" id="panelsStayOpen-headingThree">
            <button 
              class="accordion-button collapsed" 
              type="button" 
              data-bs-toggle="collapse" 
              data-bs-target="#panelsStayOpen-collapseThree" 
              aria-expanded="true" 
              aria-controls="panelsStayOpen-collapseThree"
              :disabled="control.accordion.bu"
            >
              <i class="bi-table pe-2" style="font-size: 20px;" ></i>
              Adicionar Orçamento
            </button>
          </h2>
          <div id="panelsStayOpen-collapseThree" class="accordion-collapse collapse" aria-labelledby="panelsStayOpen-headingThree">
            <div class="accor-01 accordion-body" style="width: 100%">
              <div class="d-flex justify-content-between" style="width: 100%">
                <div class="budget col-12 required">
                  <label for="year" class="form-label">Ano</label>
                  <select
                    id="year"
                    v-model="form.month.year"
                    class="form-select"
                    aria-label="Selecione o Ano"
                    :disabled="disableForm"
                    required
                  >
                    <option :selected="form.month.year"> {{ form.month.year }} </option>
                    <option v-if="form.month.year != 2021" value="2021">
                      2021
                    </option>
                    <option v-if="form.month.year != 2022" value="2022">
                      2022
                    </option>
                  </select>
                </div>

                <div class="budget col-12 required">
                  <label for="month" class="form-label">Mês</label>
                  <select
                    id="month"
                    v-model="form.month.month"
                    class="form-select"
                    aria-label="Selecione o mês"
                    :disabled="disableForm"
                    required
                  >
                    <option :selected="form.month.month"> {{ form.month.month }} </option>
                    <option 
                      v-for="b in months.filter((b) => b.name !== form.month.month )" 
                      :key="b.value" 
                      :value="b.name">
                      {{ b.name }}
                    </option>
                  </select>
                </div>

                <div class="budget col-12 required">
                  <label for="type" class="form-label">Tipo</label>
                  <select
                    id="type"
                    v-model="form.month.type"
                    class="form-select"
                    aria-label="Selecione o Tipo"
                    :disabled="disableForm"
                    required
                  >
                    <option :selected="form.month.type"> {{ form.month.type }} </option>
                    <option v-if="form.month.type != 'Gastos'" value="Gastos">
                      Gastos
                    </option>
                    <option v-if="form.month.type != 'Receita'" value="Receita">
                      Receita
                    </option>
                  </select>
                </div>

                <div class="budget col-12" style="margin-right: 0px !important;" :class="field_required ? 'required' : ''">
                  <label for="name_month" class="form-label">Valor R$</label>
                  <input
                    :disabled="disableForm"
                    id="name_month"
                    v-model="form.month.value"
                    type="text"
                    class="form-control"
                    placeholder="120.43"
                  />
                </div>
              </div>
              
              <div class="d-flex flex-column bd-highlight" style="width: 100%">
                <div class="col-12">
                  <label for="description" class="form-label">Descrição</label>
                  <input
                    :disabled="disableForm"
                    id="description"
                    v-model="form.month.description"
                    type="text"
                    class="form-control"
                    placeholder="Gastos com alocação."
                  />
                </div>

                <div class="col-12">
                  <label for="comment">Comentário</label>
                  <textarea 
                    v-model="form.month.comment"
                    :disabled="disableForm" 
                    class="form-control" 
                    placeholder="Adicione um comentário." 
                    id="comment">
                  </textarea>
                </div>
              </div>

              <DefaultButton 
                class="action-button mb-2" 
                buttonText="Adicionar" 
                @click="addBudet" 
                :buttonActive="disableForm" 
                buttonColor="btn btn-secondary rounded-3 btn-sm" 
                buttonIcon="bi bi-file-plus-fill" 
                buttonType="button"/>

              <div class="d-flex flex-column bd-highlight" style="width: 100%">
                <table class="table table-bordered shadow">
                  <thead class="table table-dark border border-white">
                    <tr class="border border-secondary">
                      <th scope="col">Ano</th>
                      <th scope="col">Mês</th>
                      <th scope="col">Tipo</th>
                      <th scope="col">Valor</th>
                      <th scope="col">%</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="month in form.months" :key="month.value">
                      <td>{{ month.year }}</td>
                      <td>{{ month.month }}</td>
                      <td>{{ month.type }}</td>
                      <td>{{ month.value }}</td>
                      <td>{{ month.description }}</td>
                    </tr>
                    <tr class="table-dark border border-dark">
                      <td colspan="1">
                        <i class="bi-dash-circle" style="font-size: 1.2rem;" ></i> 
                        Total de Gastos: 
                        </td>
                      <td colspan="1">
                        <i class="bi bi-plus-circle" style="font-size: 1.2rem;" ></i> 
                        Total de Receitas: </td>
                      <td colspan="2" style="text-align: center">
                        <i class="fa fa-balance-scale" style="font-size: 1.2rem;"></i> 
                        Balanço:
                      </td>
                      <td colspan="1" style="text-align: center">100%</td>
                    </tr>
                   </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="buttons mt-4 d-flex flex-row p-0">
        <DefaultButton 
          class="action-button me-3" 
          buttonText="Novo" 
          @click="onNew" 
          :buttonActive="control.buttons.new" 
          buttonColor="btn btn-primary" 
          buttonIcon="bi bi-plus-circle-fill" 
          buttonType="button"/>
        <DefaultButton 
          buttonType="submit"
          class="action-button me-3" 
          buttonText="Salvar" 
          :buttonActive="control.buttons.save" 
          buttonColor="btn btn-success" 
          buttonIcon="bi bi-check-circle-fill"/>
        <DefaultButton 
          class="action-button me-3" 
          buttonText="Alterar"
          @click="onChange"
          :buttonActive="control.buttons.edit" 
          buttonColor="btn btn-dark" 
          buttonIcon="bi-arrow-up-circle-fill" 
          buttonType="button" />
        <DefaultButton 
          class="action-button me-3" 
          buttonText="Cancelar" 
          @click="onReset" 
          buttonColor="btn btn-danger" 
          buttonIcon="bi-x-circle-fill" 
          buttonType="reset"/>
        <DefaultButton
          style="background-color: #138D75; color: white;"
          class="action-button me-3" 
          buttonText="Enviar para aprovação" 
          @click="onReset" 
          buttonColor="btn" 
          buttonIcon="fa fa-paper-plane" 
          buttonType="reset"/>
      </div>
    </form>

    <div id="budget-table" class="table-func d-flex row g-0 px-4 border border-danger rounded p-3 mt-1 px-4">

      <AlertMessage 
        alertShow="control.events.alerts.table.successShow"  
        alertText="control.events.alerts.table.successText" 
        alertType="alert-success"/>
      <AlertMessage  
        alertShow="control.events.alerts.table.errorShow"
        alertText="control.events.alerts.table.errorText" 
        alertType="alert-danger"/>

      <h5 class="card-title">Listagem de Orçamento</h5>
      <table class="table table-bordered shadow">
        <thead class="table table-dark border border-white">
          <tr class="border border-secondary">
            <th scope="col">Nome</th>
            <th scope="col">Familia de Produto</th>
            <th scope="col">Descrição</th>
            <th scope="col">Criado</th>
            <th scope="col">Atualizado</th>
            <th scope="col">Ações</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            
          </tr>
        </tbody>
      </table>
    </div>
	</div>
</template>


<script>
import checkLogin from '../js/checkLogin.js'
import redirectToLogin from '../js/redirectLogin'
import DefaultButton from "../components/DefaultButton.vue";
import DefaultTitle from "../components/DefaultTitle.vue";
import AlertMessage from "../components/AlertMessage.vue";
import BU from '../services/bu.js'
import Employee from '../services/employee.js'

export default {
  name: 'Orcamento',
  components: {
    DefaultButton,
    DefaultTitle,
    AlertMessage
  },
  methods: {
    collapseAccordion (id_collapse, id_field) {
      console.log("action")
      var collapse = document.getElementById(id_collapse)
      
      window.setTimeout(function() {
        document.getElementById(id_field).focus();
      }, 1);
      return new bootstrap.Collapse(collapse, {show: true})
    },
    listBUs (id) {
      BU.listBu(id)
      .then((resp) => {
        const names = []
        this.form.bus = resp.data.business
        for (var i in this.form.bus) {
          if (!names.includes(this.form.bus[i].name)) {
            this.form.bus_name.push(this.form.bus[i])
            names.push(this.form.bus[i].name)
          }
        }
      }).catch((err) => {
        console.log(err.response.data)
      })
    },
    listProductFamily () {
      this.form.bu.product_family = 'Selecione'
      const data = this.form.bus.filter((b) => b.name === this.form.bu.name)
      this.form.product_family = data
      this.accordionOne()
    },
    listApprovers () {
      Employee.listEmployeeApprover()
      .then((resp) => {
        console.log(resp.data)
        this.form.approvers = resp.data
      }).catch((err) => {
        console.log(err.response.data)
      })
    },
    accordionOne () {
      const sel = "Selecione"
  
      if (this.form.bu.name != sel && this.form.bu.product_family != sel && this.form.bu.approver != sel) {
        //this.control.accordion.status = false
      }else {
        //this.control.accordion.status = true
        //this.control.accordion.budget = true
      }
    },
    onReset (event) {
      this.bu = {
        id: '',
        name: '',
        product_family: '',
        description: ''
      }
      this.control.buttons.new = false
      this.control.buttons.save = true
      this.control.buttons.edit = true
      this.disableForm = true
    },
    onNew (event) {
      this.bu = {
        id: '',
        name: '',
        product_family: '',
        description: ''
      }
      this.control.buttons.new = true
      this.control.buttons.save = false
      this.control.buttons.edit = true
      this.disableForm = false
    },
    onSubmit(event) {
      event.preventDefault();
      const data = {...this.bu}
      data.employee_id = this.localEmployeeId
      BU.createBu(data)
        .then( (resp) => {
          this.listBus(this.localEmployeeId)
          
          this.onReset()

          this.control.events.alerts.form.successShow = true
          this.control.events.alerts.form.successText = 'BU adicionada com sucesso.'
          this.disableAlertForm()
        }).catch( (err) => {
          this.control.events.alerts.form.errorShow = true
          if (err.response.status != 422){
            this.control.events.alerts.form.errorText = err.response.data.detail
          }else {
            his.control.events.alerts.form.errorText = 'Erro ao inserir a nova BU. Por favor, cheque os campos e tente novamente.'
          }
          this.disableAlertForm()
        })
    },
    onChange(event) {
      event.preventDefault();
      const data = {...this.bu}
      data.employee_id = this.localEmployeeId
      console.log(data)
      if (confirm('Você tem certeza que deseja alterar?')) {
        BU.changeBu(this.bu.id, data)
          .then( (resp) => {
            console.log(resp.data)
            this.listBus(this.localEmployeeId)

            this.onReset()

            this.control.events.alerts.form.successShow = true
            this.control.events.alerts.form.successText = 'BU alterada com sucesso.'
            this.disableAlertForm()
          }).catch( (err) => {
            console.log(err.response.data)
            this.control.events.alerts.form.errorShow = true
            if (err.response.status != 422) {
              this.control.events.alerts.form.errorText = err.response.data.detail
            }else {
              this.control.events.alerts.form.errorText = 'Error ao alterar a BU.'
            }
            this.disableAlertForm()
          })
      }
    },
    disableAlertForm () {
      setTimeout( () => {
        this.control.events.alerts.form.successShow = false
        this.control.events.alerts.form.successText = ''
        this.control.events.alerts.form.errorShow = false
        this.control.events.alerts.form.errorText = ''
      }, 15000)
    },
    disableAlertTable () {
      setTimeout( () => {    
        this.control.events.alerts.table.successShow = false
        this.control.events.alerts.table.successText = ''
        this.control.events.alerts.table.errorShow = false
        this.control.events.alerts.table.errorText = ''
      }, 15000)
    },
    addBudet () {
      const data = {...this.form.month}
      this.form.months.push(data)

      this.form.month.month = 'Selecione'
      this.form.month.type = 'Selecione'
      this.form.month.value = 'R$'
      this.form.month.description = ''
    }
  },
  watch: {
    'form.month.value' (v) {
      if (!v.includes("R$")) {
        this.form.month.value = 'R$ ' + this.form.month.value
      }
      this.form.month.value = this.form.month.value.replace(',', '.')
    }
  },
  data () {
    return {
      user: null,
      disableForm: true,
      field_required: true,
      status: [
        {name: "draft", value:  "Rascunho"},
        {name: "approve", value:  "Aguardando aprovação"},
        {name: "denied", value:  "Negado"},
        {name: "remake", value:  "Refazer"},
        {name: "approved", value:  "Aprovado"},
      ],
      months: [
        {name: "Janeiro", value:  1},
        {name: "Fevereiro", value:  2},
        {name: "Março", value:  3},
        {name: "Abril", value:  4},
        {name: "Maio", value:  5},
        {name: "Junho", value:  6},
        {name: "Julho", value:  7},
        {name: "Agosto", value:  8},
        {name: "Setembro", value:  9},
        {name: "Outubro", value:  10},
        {name: "Novembro", value:  11},
        {name: "Dezembro", value:  12},
      ],
      form: {
        bu: {
          name: 'Selecione',
          product_family: 'Selecione',
          approver: 'Selecione'
        },
        status: {
          name: '',
          status: 'Rascunho'
        },
        month: {
          month: 'Selecione',
          year: 'Selecione',
          type: 'Selecione',
          value: 'R$',
          description: '',
          comment: '',
        },
        product_family: [
        ],
        bus: [
        ],
        bus_name: [

        ],
        months: [],
        approvers: [],
      },
      control: {
        accordion: {
          bu: false,
          status: false,
          budget: false,
          collapseOneArea: false,
          collapseTwoArea: true,
          collapseThreeArea: true
        },
        disableForm: true,
        events: {
          alerts: {
            form: {
              successShow: false,
              successText: '',
              errorShow: false,
              errorText:''
            },
            table: {
              successShow: false,
              successText: '',
              errorShow: false,
              errorText:''
            }
          }
        },
        buttons: {
          new: false,
          save: true,
          edit: true,
        }
      },
    }
  },
  async mounted (){
    try {
      const data = await checkLogin()
      if(!data){
        console.log("USER DOES NOT EXISTS.")
        redirectToLogin(this)
        this.user = data
      }else {
        this.listBUs(data.user.id)
        this.listApprovers()
      }
    } catch (error) {
      console.log("REQUEST ERROR")
      redirectToLogin(this)
    }
  }
}
</script>

<style scoped>
.table-func, form, .container, #accordionParent {
  min-width: 100%;
}
.selected, .status {
  width: 25%;
  padding-right: 30px;
}
.btn-next {
  width: 20px;
  flex-grow: 1;
  display: flex;
	flex-direction: row;
	flex-wrap: nowrap;
	justify-content: flex-end;
	align-items: flex-end;
	align-content: flex-end;
  margin-right: 0px !important;
}

table {
  border-collapse: collapse;
  border-radius: 7px;
  overflow: hidden;
}

form {
  border-bottom: red solid 1px;
  border-left: red solid 1px;
  border-right: red solid 1px;
  border-bottom-left-radius: 4px;
  border-bottom-right-radius: 4px;
}
.name {
  width: 45%;
}
.budget {
  max-width: 23%;
}
.col-12 {
  margin-top: 10px;
  margin-bottom: 10px;
}
.accor-01{
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: flex-start;
  align-items: flex-end;
  align-content: space-between;
}
.accordion-button {
  font-size: 18px;
  font-weight: 600;
}

</style>