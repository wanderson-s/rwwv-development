import axios from "axios"

const baseURL = location.origin + '/v1/'
export const http = axios.create({
    baseURL: baseURL
})