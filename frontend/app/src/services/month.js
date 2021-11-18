import { http } from "./config";

export default {
	createMonth: (data) => { 
		return http.post('/month', data)
	},
	listMonth: (id) => {
		return http.get('/month?employee_id=' + id)
	},
	removeMonth: (id) => {
		return http.delete('/month/' + id)
	},
	changeMonth: (id, data) => {
		return http.patch('/month/' + id, data)
	}
}