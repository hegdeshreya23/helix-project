import { Message } from '../types/chat';

const API_URL = 'http://localhost:8080';

export const chatService = {
  async sendMessage(message: string, history: Message[] = []) {
    try {
      console.log('Sending request to:', `${API_URL}/api/chat`);
      console.log('Request payload:', { message, history });

      const response = await fetch(`${API_URL}/api/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          message,
          history: history.map(msg => ({
            role: msg.role,
            content: msg.content
          }))
        })
      });

      if (!response.ok) {
        const errorText = await response.text();
        console.error('API Error:', {
          status: response.status,
          statusText: response.statusText,
          error: errorText
        });
        throw new Error(`API Error: ${errorText}`);
      }

      const data = await response.json();
      console.log('API Response:', data);
      
      return data.content;

    } catch (error) {
      console.error('Error in sendMessage:', error);
      throw error;
    }
  }
};