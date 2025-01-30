import axios from "axios";
const api = axios.create({
  baseURL: 'http://192.168.0.62:9999/api/', // Replace with your API base URL
  timeout: 10000, // Set a timeout (in ms)
  headers: {
    'Content-Type': 'application/json',
  },
});

export default {
  install(app) {
    // Create an Axios instance with default configuration

    api.defaults.validateStatus = (status) => status < 500 && status!==401;
    let tokens = ''
    try{
      tokens = JSON.parse(localStorage.getItem('token'))
    }catch{
      tokens = null
      localStorage.removeItem('token');
      localStorage.removeItem('user');
    }
    // Add interceptors if needed (optional)
    api.interceptors.request.use(
      (config) => {

        // Add any authorization tokens or headers here
        if(tokens){
          config.headers.Authorization = `Bearer ${tokens.access}`;
        }
        return config;
      },
      (error) => Promise.reject(error)
    );
    api.interceptors.response.use(
      response => response,
      async error => {
        const originalRequest = error.config;
        if(error.response){
          originalRequest._retry = true; 
          if (error.response.status === 401 && !originalRequest._retry) {
            try {
              if(tokens){
                const response = await api.post('/token/refresh/', {
                  refresh:tokens.refresh,
                });
                const { access } = response.data;
                if(access.length<=0){
                  throw new Error("No Access Token");
                }
                tokens.access=access
                localStorage.setItem('token', JSON.stringify(tokens));
                api.defaults.headers.common['Authorization'] = `Bearer ${access}`;
                return api(originalRequest); 
              }
            } catch {
              console.log('Token refresh failed');
              localStorage.removeItem('token');
              return Promise.reject(error)
            }
          }
        }
        return Promise.reject(error)
      }
    );

    // Attach the Axios instance to the global Vue app as $api
    app.config.globalProperties.$api = api;
  },
};
export {api}