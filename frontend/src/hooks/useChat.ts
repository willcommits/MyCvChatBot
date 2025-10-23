import { useState, useCallback, useEffect } from 'react';
import { Message } from '../types';
import { chatAPI } from '../services/api';

export const useChat = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [sessionId] = useState(() => `session_${Date.now()}`);

  const addMessage = useCallback((content: string, sender: 'user' | 'ai') => {
    const newMessage: Message = {
      id: `msg_${Date.now()}_${Math.random()}`,
      content,
      sender,
      timestamp: new Date(),
    };
    setMessages(prev => [...prev, newMessage]);
    return newMessage;
  }, []);

  const sendMessage = useCallback(async (content: string) => {
    if (!content.trim() || isLoading) return;

    // Add user message
    addMessage(content, 'user');
    setIsLoading(true);

    try {
      const response = await chatAPI.sendMessage(content, sessionId);
      addMessage(response.response, 'ai');
    } catch (error) {
      console.error('Error sending message:', error);
      addMessage('I apologize, but I\'m having trouble responding right now. Please try again in a moment.', 'ai');
    } finally {
      setIsLoading(false);
    }
  }, [addMessage, sessionId, isLoading]);

  const clearMessages = useCallback(() => {
    setMessages([]);
  }, []);

  // Add welcome message on first load
  useEffect(() => {
    if (messages.length === 0) {
      addMessage(
        "Hi! I'm Prosper's CV assistant. I can answer questions about my background, experience, skills, and projects. What would you like to know?",
        'ai'
      );
    }
  }, [messages.length, addMessage]);

  return {
    messages,
    isLoading,
    sendMessage,
    clearMessages,
    sessionId,
  };
};