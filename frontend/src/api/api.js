import axios from 'axios';
var querystring = require('querystring');
var isProduction = process.env.NODE_ENV === 'production';
let base = 'http://localhost:8123';
if (isProduction) {
    base = ""
}

export const requestLogin = params => { return axios.post(`${base}/rest/account/api/login`,  querystring.stringify(params)).then(res => res.data); };

// export const getPictureList = params => { 
//     return axios.get(`${base}/rest/album/api/picture_list?` + querystring.stringify(params)).then(res => res.data); 
// };

// export const downloadPic = params => {
//     console.log(params,"<<<")
//     window.open(`${base}/rest/album/api/picture_download/?`+querystring.stringify(params) , '_blank');
// }