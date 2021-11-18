import { http } from "./config";

export default {
	createStatusBudget: (data) => { 
		return http.post('/status_budget', data)
	},
	listStatusBudget: (id) => {
		return http.get('/status_budget?employee_id=' + id)
	},
	removeStatusBudget: (id) => {
		return http.delete('/status_budget/' + id)
	},
	changeStatusBudget: (id, data) => {
		return http.patch('/status_budget/' + id, data)
	}
}