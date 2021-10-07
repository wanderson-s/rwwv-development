import { http } from "./config";

export default {
	login: (data) => {
		const resp = false
		http.post('/auth/login', data)
			.then((res) => {
				console.log(res)
				localStorage.setItem("access_token", res.data.access_token)
				localStorage.setItem("refresh_token", res.data.refresh_token)
				resp = true
			}).catch((err) => {
				console.log("USER NO ACCESS")
			})
		return resp
	},
	getMe: (token) => {
		const uri = "/auth/get-me?access_token=" + token;
		const me = null;
		http.get(uri)
			.then((resp) => {
				if (resp.status == 200) {
					console.log("RETURN ME DATA")
					me = resp.data
				}
			})
		return me
	},
	checkLogin: () => {
		const access_token = localStorage.getItem("access_token")
		const refresh_token = localStorage.getItem("refresh_token")
		const me = null;

		if (access_token) {
			console.log("CHECK ACCESS TOKEN")
			const url = "/auth/check-token?access_token=" + access_token;
			http.get(url)
				.then((res) => {
					if (resp.status == 200) {
						me = getMe(access_token)
					}
				}).catch((err) => {
					console.log("ACCESS TOKEN ERROR.")
				})
			if (me) {
				return me
			}
		}
		if (refresh_token) {
			console.log("TRY REFRESH TOKEN")
			const url = "/auth/refresh-token?refresh_token=" + refresh_token;
			http.post(url).then((resp) => {
				if (resp.status == 201) {
					localStorage.setItem("access_token", resp.data.access_token)
					localStorage.setItem("refresh_token", resp.data.refresh_token)
					me = getMe(resp.data.access_token)
				}
			}).catch((err) => {
				console.log("REFRESH TOKEN ERROR.")
			})
		}
		return me
	}
}