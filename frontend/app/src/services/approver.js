import { http } from "./config";

export default {
	listApprover: () => {
		return http.get('/approver')
	},
	listApproverApprover: () => {
		return http.get('/approver?approver=true')
	},
	removeApprover: (id) => {
		return http.delete('/approver/' + id)
	},
	createApprover: (data) => { 
		return http.post('/approver/', data)
	},
	changeApprover: (id, data) => { 
		return http.patch('/approver/' + id, data)
	}
}