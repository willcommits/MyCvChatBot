import axios from 'axios';
import { ApiResponse, SuggestionResponse } from '../types';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 30000,
});

export const chatAPI = {
  sendMessage: async (message: string, sessionId: string = 'default'): Promise<ApiResponse> => {
    const response = await api.post('/chat', {
      message,
      session_id: sessionId,
    });
    return response.data;
  },

  getSuggestions: async (): Promise<SuggestionResponse> => {
    const response = await api.get('/suggestions');
    return response.data;
  },

  healthCheck: async (): Promise<boolean> => {
    try {
      await api.get('/health');
      return true;
    } catch {
      return false;
    }
  },
};

export default api;