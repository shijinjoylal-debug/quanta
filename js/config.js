const CONFIG = {
    // API_BASE_URL can be overridden by environment variables during build (e.g., in Vercel)
    API_BASE_URL: (typeof import.meta !== 'undefined' && import.meta.env && import.meta.env.VITE_API_BASE_URL) 
        ? import.meta.env.VITE_API_BASE_URL 
        : 'https://quanta-backend-raeq.onrender.com',
};
window.CONFIG = CONFIG;
