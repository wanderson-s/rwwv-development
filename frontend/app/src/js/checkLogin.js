import axios from "axios";

const baseUrl = "http://localhost:8001/v1/auth"
const urlGetMe = baseUrl + "/get-me?access_token="

async function checkLogin () {
    const access_token = localStorage.getItem("access_token")
    const refresh_token = localStorage.getItem("refresh_token")

    if (access_token){
        console.log("CHECK ACCESS TOKEN")
        const url =  baseUrl + "/check-token?access_token=" + access_token;
        try {
            const resp = await axios.get(url)
            if (resp.status == 200){
                const uri = urlGetMe + access_token;
                console.log("RETURN ME DATA")
                return (await axios.get(uri)).data
            }
        } catch (error) {
            console.log("ACCESS TOKEN ERROR.")
        }
    }
    if (refresh_token){
        console.log("TRY REFRESH TOKEN")
        const url =  baseUrl + "/refresh-token?refresh_token=" + refresh_token;
        try {
            const resp = await axios.post(url)
            if (resp.status == 201){
                localStorage.setItem("access_token", resp.data.access_token)
                localStorage.setItem("refresh_token", resp.data.refresh_token)
                const uri = urlGetMe + resp.data.access_token;
                console.log("RETURN ME DATA")
                return (await axios.get(uri)).data
            } 
        }catch (error) {
            console.log("REFRESH TOKEN ERROR.")
        }
    }
    return null
}

export default checkLogin;