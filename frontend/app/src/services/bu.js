import { http } from "./config";

export default {
	listBu: (id) => {
		return http.get('/bu?employee_id=' + id)
	},
	removeBu: (id) => {
		return http.delete('/bu/' + id)
	},
	createBu: (data) => { 
		return http.post('/bu', data, {
			headers: {}
		})
	},
	changeBu: (id, data) => {
		return http.put('/bu/' + id, data)
	}
}