import axios from 'axios';

//export const BASE_URL = 'http://127.0.0.1:5000/'; // Local
export const BASE_URL = 'https://reto1.herokuapp.com//'; // Production

const https = require('https');

export const GET = async (url) => {
  const response = await axios({
    url,
    method: 'GET',
    httpsAgent: new https.Agent({
      rejectUnauthorized: false,
    }),
  });
  return response;
};

export const POST = async (url, data) => {
  const response = await axios({
    url,
    method: 'POST',
    data,
    httpsAgent: new https.Agent({
      rejectUnauthorized: false,
    }),
  });
  return response;
};

export const PUT = async (url, data) => {
  const response = await axios({
    url,
    method: 'PUT',
    data,
    httpsAgent: new https.Agent({
      rejectUnauthorized: false,
    }),
  });
  return response;
};

export const POST_FILE_DOWNLOAD = async (url, data) => {
  const response = await axios({
    url,
    method: 'POST',
    data,
    responseType: 'blob',
    httpsAgent: new https.Agent({
      rejectUnauthorized: false,
    }),
  }).then((response) => {
    const url = window.URL.createObjectURL(new Blob([response.data]));
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', 'file.pdf');
    document.body.appendChild(link);
    link.click();
  });
  return response;
};

export const GET_FILE_DOWNLOAD = async (url, filename = 'file') => {
  const response = await axios({
    url,
    method: 'GET',
    responseType: 'blob',
    httpsAgent: new https.Agent({
      rejectUnauthorized: false,
    }),
  }).then((response) => {
    const url = window.URL.createObjectURL(new Blob([response.data]));
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', `${filename}.pdf`);
    document.body.appendChild(link);
    link.click();
  });
  return response;
};