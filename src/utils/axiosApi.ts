import axios from 'axios';
import { refreshTokenOnServer } from '../api/user';

export const axiosApi = axios.create({
  baseURL: 'https://16.16.104.247:8000/api/',
  headers: {
    'Content-Type': 'application/json'
  }
});

axiosApi.interceptors.request.use((config) => {
  if (localStorage.getItem('tokens')) {
    const tokensData = JSON.parse(localStorage.getItem('tokens') || '{}');
    config.headers['Authorization'] = `Bearer ${tokensData.access}`;
  }
  return config;
});

axiosApi.interceptors.response.use(
  (response) => {
    return response;
  },
  async (error) => {
    const originalConfig = error.config;
    if (originalConfig.url !== 'user/token/' && error.response) {
      if (error.response.status === 401) {
        const authData = JSON.parse(localStorage.getItem('tokens') || '{}');
        const payload = {
          refresh: authData.refresh
        };

        try {
          const { data } = await refreshTokenOnServer(payload);
          localStorage.setItem('tokens', JSON.stringify(data));
          originalConfig.headers['Authorization'] = `Bearer ${data.access}`;

          return axios(originalConfig);
        } catch (error) {
          return Promise.reject(error);
        }
      }
    }

    return Promise.reject(error);
  }
);
