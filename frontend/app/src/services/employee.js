import { http } from "./config";

export default {
	listEmployee: () => {
		return http.get('/employees')
	},
	removeEmployee: (id) => {
		return http.delete('/employees/' + id)
	},
	createEmployee: (data) => { 
		return http.post('/employees/', data)
	}
}