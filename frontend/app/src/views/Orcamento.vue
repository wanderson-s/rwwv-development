<template>
	<div class="container-fluid p-1 pe-2">
    <DefaultTitle 
      titleText="Orçamentos" 
      titleIcon="bi-briefcase-fill"
    />
    <form class="row g-0 p-3 px-4" @submit="onSubmit">
      <AlertMessage 
        :alertShow="alerts.form.success"  
        :alertText="alerts.form.successText" 
        alertType="alert-success"/>
      <AlertMessage  
        :alertShow="alerts.form.error"
        :alertText="alerts.form.errorText" 
        alertType="alert-danger"/>

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
              <i class="bi-plus-square-fill pe-2" style="font-size: 20px;"></i>
              Informe o nome e status do seu orçamento.
            </button>
          </h2>
          <div id="panelsStayOpen-collapseOne" class="accordion-collapse collapse" :class="accordion.collOne" aria-labelledby="panelsStayOpen-headingOne">
            <div class="accor-01 accordion-body" style="width: 100%">
              <div class="name status col-12" :class="field_required ? 'required' : ''">
                <label for="name" class="form-label">Nome</label>
                <input
                  :disabled="disableFormBudget"
                  id="name"
                  v-model="form.status.name"
                  :class="borders.status_name"
                  type="text"
                  class="form-control"
                  placeholder="Orçamento referente ao ano de 2022"
                  data-bs-toggle="tooltip" 
                  data-bs-placement="bottom" 
                  title="O nome do status precisa ter pelo menos 5 letras."
                />
              </div>

              <div class="selected col-12 required" :class="field_required ? 'required' : ''">
                <label for="status" class="form-label">Status</label>
                <select
                  id="status"
                  v-model="form.status.status"
                  :class="borders.status"
                  class="form-select"
                  aria-label="Selecione o status"
                  :disabled="disableFormBudget"
                  data-bs-toggle="tooltip" 
                  data-bs-placement="bottom" 
                  title="Por padrão o status inicia como rascunho."
                  required
                >
                  <option> {{ form.status.status }} </option>
                </select>
              </div>

              <div class="selected col-12 required">
                <label for="approver" class="form-label">Aprovador</label>
                <select
                  id="approver"
                  v-model="form.bu.approver"
                  :class="borders.approver"
                  class="form-select"
                  aria-label="Selecione o Aprovador"
                  @change="accordionOne"
                  :disabled="disableFormBudget"
                  data-bs-toggle="tooltip" 
                  data-bs-placement="bottom" 
                  title="Selecione o e-mail do aprovador"
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
                  @click="collapseAccordion('panelsStayOpen-collapseTwo', 'business')"
                  :disabled="disableFormBudget"
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
              class="accordion-button" 
              type="button" 
              data-bs-toggle="collapse" 
              data-bs-target="#panelsStayOpen-collapseTwo" 
              aria-expanded="true" 
              aria-controls="panelsStayOpen-collapseTwo"
              :disabled="control.accordion.bu"
            >
              <i class="bi-briefcase-fill pe-2" style="font-size: 20px;" ></i>
              Selecione a BU, Familia de Produto e Aprovador.
            </button>
          </h2>
          <div id="panelsStayOpen-collapseTwo" class="accordion-collapse collapse" :class="accordion.collTwo" aria-labelledby="panelsStayOpen-headingTwo">
            <div class="accor-01 accordion-body" style="width: 100%">
              <div class="selected col-12 required">
                <label for="business" class="form-label">BU</label>
                <select
                  id="business"
                  v-model="form.bu.name"
                  class="form-select"
                  :class="borders.name"
                  aria-label="Selecione a BU"
                  @change="listProductFamily()"
                  :disabled="disableForm"
                  data-bs-toggle="tooltip" 
                  data-bs-placement="bottom" 
                  title="Selecione uma BU"
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
                  :class="borders.product_family"
                  class="form-select"
                  aria-label="Selecione um produto"
                  @change="accordionOne"
                  :disabled="disableForm"
                  data-bs-toggle="tooltip" 
                  data-bs-placement="bottom" 
                  title="Selecione uma familia de produto"
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

              <div class="btn-next col-12">
                <DefaultButton
                  :disabled="disableForm"
                  @click="collapseAccordion('panelsStayOpen-collapseThree', 'year')"
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
        <div class="accordion-item shadow">
          <h2 class="accordion-header" id="panelsStayOpen-headingThree">
            <button 
              class="accordion-button" 
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
          <div id="panelsStayOpen-collapseThree" class="accordion-collapse collapse" :class="accordion.collThree" aria-labelledby="panelsStayOpen-headingThree">
            <div class="accor-01 accordion-body" style="width: 100%">
              <div class="d-flex justify-content-between" style="width: 100%">
                <div class="budget col-12 required">
                  <label for="year" class="form-label">Ano</label>
                  <select
                    id="year"
                    v-model="form.month.year"
                    class="form-select"
                    :class="borders.year"
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
                    :class="borders.month"
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
                    :class="borders.type"
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

                <currency-input 
                  :options="{ currency: 'BRL',currencyDisplay: 'hidden', precision: 2, autoDecimalDigits: false }"
                  :disable="disableForm"
                  :border='borders.value' 
                  v-model="form.month.value"
                />
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
                buttonType="button"
              />

              <div class="d-flex flex-column bd-highlight" style="width: 100%">
                <table class="table table-bordered shadow">
                  <thead class="table table-dark border border-white">
                    <tr class="border border-secondary">
                      <th scope="col">BU</th>
                      <th scope="col">Familia</th>
                      <th scope="col">Ano</th>
                      <th scope="col">Mês</th>
                      <th scope="col">Tipo</th>
                      <th scope="col">Valor</th>
                      <th scope="col">%</th>
                      <th scope="col">Remover</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="month in form.months" :key="month.value">
                      <td class="lines">{{ getBuById(month.bu_id) }}</td>
                      <td class="lines">{{ getFamilyById(month.bu_id) }}</td>
                      <td class="lines">{{ month.year }}</td>
                      <td class="lines">{{ month.month }}</td>
                      <td class="lines">{{ month.type }}</td>
                      <td class="lines">{{ new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(month.value) }}</td>
                      <td class="lines">{{ month.percent }}</td>
                      <td class="lines">
                        <button 
                          @click="removeLine(month.id)" 
                          type="button" 
                          class="btn btn-danger btn-sm m-0"
                          data-bs-toggle="tooltip" 
                          data-bs-placement="left" 
                          title="Remover linha"
                          ><i class="bi-dash-circle-fill"></i>
                        </button>
                      </td>
                    </tr>
                    <tr class="table-dark border border-dark">
                      <td colspan="8">
                        <div class="d-flex justify-content-around" style="width: 100%">
                          <div style="font-size:18px">
                            <i class="bi-dash-circle" style="font-size:20px" ></i> 
                            Total de Gastos: {{ form.totals.gastos }}
                          </div>
                          <div style="font-size:18px">
                            <i class="bi bi-plus-circle" style="font-size:20px"></i> 
                            Total de Receitas: {{ form.totals.receita }}
                          </div>
                          <div style="font-size:18px" >
                            <i class="fa fa-balance-scale" style="font-size:20px"></i> 
                            Balanço: {{ form.totals.balanco }}
                          </div>
                        </div>
                      </td>
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
      <h5 class="card-title">Listagem de Orçamento</h5>
      <table class="table table-bordered shadow">
        <thead class="table table-dark border border-white">
          <tr class="border border-secondary">
            <th scope="col">Nome</th>
            <th scope="col">Status</th>
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
import CurrencyInput from '../components/Money.vue'
import Budget from '../services/budget.js'
import StatusBudget from '../services/status.js'
import Approver from '../services/approver.js'
import Month from '../services/month.js'

export default {
  name: 'Orcamento',
  components: {
    DefaultButton,
    DefaultTitle,
    AlertMessage,
    CurrencyInput 
  },
  methods: {
    collapseAccordion (id_collapse, id_field, coll=true) {
      if (id_field == 'year') {
        this.validationSelector(this.form.bu.name, "name")
        this.validationSelector(this.form.bu.product_family, "product_family")
        setTimeout(() => {
          if (this.validation.name && this.validation.product_family && coll) {
            this.accordion.collTwo = ''
            this.accordion.collThree = 'show'
            window.setTimeout(function() {
              document.getElementById(id_field).focus();
            }, 1);
            this.getBu()
          }
        }, 250)
      } else if (id_field == 'business') {
        this.validationSelector(this.form.status.status, "status")
        this.validationText(this.form.status.name, "status_name")
        this.validationSelector(this.form.bu.approver, "approver")
      
        this.saveBudget()
        console.log(this.budgetStatus)
        setTimeout(() => {
          if (this.validation.status_name && this.validation.status && this.validation.approver && coll && this.budgetStatus) {
            this.disableForm = false
            this.disableFormBudget = true
            this.accordion.collTwo = 'show'
            this.accordion.collOne = ''
            this.borders.approver = ''
            this.borders.status_name = ''
            this.borders.status = ''
            window.setTimeout(function() {
              document.getElementById(id_field).focus();
            }, 1);
          }
        }, 250)
      }
    },
    collapseNow(id_collapse, id_field) {
      var collapse = document.getElementById(id_collapse)
      window.setTimeout(function() {
        document.getElementById(id_field).focus();
      }, 1);
      return new bootstrap.Collapse(collapse, {show: true})
    },
    getBuById (id) {
      const data = this.form.bus.filter((v) => v.id == id)
      return data[0].name
    },
    getFamilyById (id) {
      const data = this.form.bus.filter((v) => v.id == id)
      return data[0].product_family
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
      this.disableFormBudget = true
      this.control.accordion.bu = false
      this.control.accordion.status = false
      this.control.accordion.budget = false
      this.control.accordion.collapseOneArea = false
      this.control.accordion.collapseTwoArea = true
      this.control.accordion.collapseThreeArea = true
      this.control.disableForm = true
      this.validation.name = false
      this.validation.product_family = false
      this.validation.approver = false
      this.validation.status_name = false
      this.validation.status = false
      this.validation.year = false
      this.validation.month = false
      this.validation.type = false
      this.validation.value = false
      this.validation.description = false
      this.validation.comment = false   

      this.borders.bu = ''
      this.borders.product_family = ''
      this.borders.approver = ''
      this.borders.name = ''
      this.borders.status_name = ''
      this.borders.status = ''
      this.borders.year = ''
      this.borders.month = ''
      this.borders.type = ''
      this.borders.value = ''
      this.borders.description = ''
      this.borders.comment = ''
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
      this.disableFormBudget = false
    },
    // Save
    getApprover() {
      Employee.listEmployeeByEmail(this.form.bu.approver)
      .then((resp) => {
        this.dataBudget.bu.approver = resp.data
      }).catch((err) => {
        console.log("Approver", err)
      })
    },
    getBu () {
      const data = this.form.bus.filter((v) => v.name == this.form.bu.name && v.product_family == this.form.bu.product_family)
      this.dataBudget.bu.bu = data[0]
    },
    saveBudget () {
      this.getBu()
      this.getApprover()
      const data = {name: this.form.status.name, employee_id: this.user.id}
      Budget.createBudget(data)
      .then((resp) => {
        this.dataBudget.budget.data = resp.data
        this.saveStatus()
        setTimeout(() => {
          this.saveApprover()
        }, 1000)
        this.alerts.form.success = true
        this.alerts.form.successText = "Orçamento criado com sucesso."
        this.budgetStatus = true
      }).catch((err) => {
        console.log(err)
        this.alerts.form.error = true
        this.alerts.form.errorText = err.response.data.detail
        this.budgetStatus = false
      }).finally(this.disableAlertForm())
    },
    saveStatus() {
      const status = this.status.filter((v) => v.value == this.form.status.status)[0].name
      const data = {status: status, current: true, budget_id: this.dataBudget.budget.data.id}
      StatusBudget.createStatusBudget(data)
      .then((resp) => {
        this.dataBudget.budget.status = resp.data
      }).catch((err) => {
        console.log(err.response.data)
      })
    },
    saveApprover () {
      this.getApprover()
      const data = {
        budget_id:  this.dataBudget.budget.data.id, 
        approver_id: this.dataBudget.bu.approver.id
      }
      Approver.createApprover(data)
      .then((resp) => {
        console.log(resp.data)
      }).catch((err) => {
        console.log(err.response.data)
      })
    },
    onSubmit(event) {
      event.preventDefault();
      if (this.form.months.length < 1) {
        this.alerts.form.error = true
        this.alerts.form.errorText = "O orçamento não pode ser salvo. Verifique se você preencheu todos os campos e adicionou pelo menos um orçamento!"
      } else {
        this.form.months.forEach((item) => {
          const data = {...item}
          data.month = this.months.filter(v => v.name == item.month)[0].value
          data.type = item.type == 'Receita' ? 'income' : 'expenditure'
          Month.createMonth(data)
          .then(resp => {
            console.log(resp.data)
          }).catch(err => {
            console.log(err.response.data)
            console.log(err.request.data)
          })
        }),
        this.alerts.form.success = true
        this.alerts.form.successText = 'Orçamento gerado com sucesso.'
      }
      this.disableAlertForm()
    },
    // =======
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
        this.alerts.form.success = false
        this.alerts.form.successText = ''
        this.alerts.form.error = false
        this.alerts.form.errorText = ''
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
    toReal (value) {
      return Intl.NumberFormat('pt-BR', {
        style: 'currency',
        currency: 'BRL',
      }).format(value)
    },
    validationOneAndTwo() {
      this.validationSelector(this.form.bu.name, "name")
      this.validationSelector(this.form.bu.product_family, "product_family")
      this.validationSelector(this.form.bu.approver, "approver")
      this.validationSelector(this.form.status.status, "status")
      this.validationText(this.form.status.name, "status_name")
    },
    addBudet () {
      this.getBu()
      setTimeout(() => {
        if (this.validateThree() && this.validateTwo()){
          const data = {
            ...this.form.month, 
            bu_id: this.dataBudget.bu.bu.id, 
            budget_id: this.dataBudget.budget.data.id,
          }
          this.form.months.push(data)
          this.form.month.month = 'Selecione'
          this.form.month.type = 'Selecione'
          this.form.month.value = ''
          this.form.month.description = ''

          this.form.totals.receita = 0
          this.form.totals.gastos = 0
          this.form.totals.balanco = 0
          this.form.month.id += 1

          this.form.months.forEach((val) => {
            const value = val.value
            if (val.type == 'Gastos'){
              this.form.totals.gastos += parseFloat(value)
            }else if (val.type == 'Receita'){
              this.form.totals.receita += parseFloat(value)
            }
          })
          
          this.form.months.forEach((val) => {
            const value = val.value
            if (val.type == 'Gastos'){
              val.percent = ((value / this.form.totals.gastos) * 100).toFixed(2) + '%'
            }else if (val.type == 'Receita'){
              val.percent = ((value / this.form.totals.receita) * 100).toFixed(2) + '%'
            }
            console.log(val)
          })
          //this.form.totals.balanco = "R$ " + ((this.form.totals.receita - this.form.totals.gastos).toFixed(2) || 0)
          //this.form.totals.gastos = "R$ " + this.form.totals.gastos.toFixed(2)
          //this.form.totals.receita = "R$ " + this.form.totals.receita.toFixed(2)
          this.form.totals.balanco = new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format((this.form.totals.receita - this.form.totals.gastos).toFixed(2) || 0)
          this.form.totals.gastos = new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(this.form.totals.gastos.toFixed(2))
          this.form.totals.receita = new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(this.form.totals.receita.toFixed(2))
          this.validation.month = false
          this.validation.type = false
          this.validation.value = false
          this.alerts.form.success = true
        } else {
          this.validationOneAndTwo()
          this.alerts.form.error = true
        }
        setTimeout(() => {
          this.alerts.form.success = false
          this.alerts.form.error = false
        }, 10000)
      }, 250)
    },
    removeLine (id) {
      const new_data = this.form.months.filter(val => val.id != id)
      this.form.months = new_data
      this.form.totals.receita = 0
      this.form.totals.gastos = 0
      this.form.totals.balanco = 0

      this.form.months.forEach((val) => {
        const value = val.value
        if (val.type == 'Gastos'){
          this.form.totals.gastos += parseFloat(value)
        }else if (val.type == 'Receita'){
          this.form.totals.receita += parseFloat(value)
        }
      })

      this.form.months.forEach((val) => {
        const value = val.value
        console.log(value)
        if (val.type == 'Gastos'){
          val.percent = ((value / this.form.totals.gastos) * 100).toFixed(2) + '%'
        }else if (val.type == 'Receita'){
          val.percent = ((value / this.form.totals.receita) * 100).toFixed(2) + '%'
        }
        console.log(val)
      })
      this.form.totals.balanco = "R$ " + ((this.form.totals.receita - this.form.totals.gastos).toFixed(2) || 0)
      this.form.totals.gastos = "R$ " + this.form.totals.gastos.toFixed(2)
      this.form.totals.receita = "R$ " + this.form.totals.receita.toFixed(2)
    },
    validationSelector (value, key) {
      if (value != 'Selecione') {
        this.validation[key] = true
        this.borders[key] = 'border border-success border-1 bg-success bg-opacity-10' 
      } else {
        this.validation[key] = false
        this.borders[key] = 'border border-danger border-1 bg-danger bg-opacity-10'
      }
    },
    validationText (value, key, len=null) {
      if (value.length >= (len || 5)) {
        this.validation[key] = true
        this.borders[key] = 'border border-success border-1 bg-success bg-opacity-10' 
      } else {
        this.validation[key] = false
        this.borders[key] = 'border border-danger border-1 bg-danger bg-opacity-10'
      }
    },
    validationNumber (value, key) {
      if (typeof value === 'number') {
        this.validation[key] = true
        this.borders[key] = 'border border-success border-1 bg-success bg-opacity-10'
      } else {
        this.validation[key] = false
        this.borders[key] = 'border border-danger border-1 bg-danger bg-opacity-10'
      }
    },
    validateTwo () {
      this.validationSelector(this.form.bu.name, "name")
      this.validationSelector(this.form.bu.product_family, "product_family")
      if (this.validation.name && this.validation.product_family) {
        return true
      }
      return false
    },
    validateOne () {
      this.validationText(this.form.status.name, 'status_name')
      this.validationSelector(this.form.status.status, "status")
      this.validationSelector(this.form.bu.approver, "approver")
      if (this.validation.status_name && this.validation.status && this.validation.approver) {
        return true
      }
      return false
    },
    validateThree () {
      this.validationSelector(this.form.month.year ,"year")
      this.validationSelector(this.form.month.month ,"month")
      this.validationSelector(this.form.month.type ,"type")
      this.validationNumber(this.form.month.value ,"value")
      if (this.validation.year && this.validation.month && this.validation.type && this.validation.value) {
        return true
      }
      return false
    },
  },
  watch: {
    'form.bu.name' (v) {
      this.validationSelector(v, 'name')
    },
    'form.bu.product_family' (v) {
      this.validationSelector(v, 'product_family')
    },
    'form.bu.approver' (v) {
      this.validationSelector(v, 'approver')
    },
    'form.status.status' (v) {
      this.validationSelector(v, 'status')
    },
    'form.status.name' (v) {
      this.validationText(v, 'status_name')
    },
    'form.month.year' (v) {
      this.validationSelector(v, 'year')
    },
    'form.month.month' (v) {
      this.validationSelector(v, 'month')
    },
    'form.month.type' (v) {
      this.validationSelector(v, 'type')
    },
    'form.month.value' (v) {
      if (this.form.month.value) {
        this.validation.value = true
        this.borders.value = 'border border-success border-1 bg-success bg-opacity-10' 
      } else {
        this.validation.value = false
        this.borders.value = 'border border-light border-1 bg-light bg-opacity-10'
      }
    }
  },
  data () {
    return {
      user: null,
      disableFormBudget: true,
      disableForm: true,
      field_required: true,
      accordion: {
        collOne: 'show',
        collTwo: '',
        collThree: ''
      },
      budgetStatus: false,
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
        totals: {
          receita: 0,
          gastos: 0,
          balanco: 0
        },
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
          year: 'Selecione',
          month: 'Selecione',
          type: 'Selecione',
          value: '',
          description: '',
          comment: '',
          id: 0
        },
        product_family: [],
        bus: [],
        bus_name: [],
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
      validation: {
        name: false,
        product_family: false,
        approver: false,
        status_name: false,
        status: false,
        year: false,
        month: false,
        type: false,
        value: false,
        description: false,
        comment: false
      },
      borders: {
        bu: '',
        product_family: '',
        approver: '',
        name: '',
        status_name: '',
        status: '',
        year: '',
        month: '',
        type: '',
        value: '',
        description: '',
        comment: ''
      },
      alerts: {
        form: {
          success: false,
          successText: '',
          error: false,
          errorText: '',
        }
      },
      dataBudget: {
        bu: {
          bu: {},
          approver: {}
        },
        budget: {
          data: {},
          status: {}
        },
        months: {}
      }
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
        this.user = data.user
      }
    } catch (error) {
      console.log("REQUEST ERROR")
      redirectToLogin(this)
    }
  }
}
</script>

<style scoped>
.input-group .form-control {
    float: none;
}
.input-group .input-buttons {
    position: relative;
    z-index: 3;
}

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
.lines {
  text-align: center;
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
  width: 35%;
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