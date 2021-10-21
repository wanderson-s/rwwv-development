import { http } from '../services/config.js'

async function login (data) {
    try {
        console.log("LOGIN USER")
        const response = await http.post("/auth/login", data);
        console.log(response)
        localStorage.setItem("access_token", response.data.access_token)
        localStorage.setItem("refresh_token", response.data.refresh_token)
        return true
    } catch (error) {
        console.log("USER NO ACCESS")
        return false
    }
}

export default login;